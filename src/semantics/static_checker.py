"""
Static Semantic Checker for HLang Programming Language
"""

from functools import reduce
from typing import Dict, List, Set, Optional, Any, Tuple, Union, NamedTuple
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode, Program, ConstDecl, FuncDecl, Param, VarDecl, Assignment, 
    IfStmt, WhileStmt, ForStmt, ReturnStmt, BreakStmt, ContinueStmt, 
    ExprStmt, BlockStmt, IntType, FloatType, BoolType, StringType, 
    VoidType, ArrayType, IdLValue, ArrayAccessLValue, BinaryOp, UnaryOp, 
    FunctionCall, ArrayAccess, Identifier, IntegerLiteral, FloatLiteral, 
    BooleanLiteral, StringLiteral, ArrayLiteral
)
from .static_error import (
    StaticError, Redeclared, Undeclared, TypeMismatchInExpression,
    TypeMismatchInStatement, TypeCannotBeInferred, NoEntryPoint,
    MustInLoop
)

# Import marker classes with different names to avoid conflict  
from .static_error import Identifier as IdentifierMarker, Function as FunctionMarker

class Symbol(NamedTuple):
    name: str
    typ: ASTNode
    kind: str  # 'variable', 'constant', 'function', 'parameter'
    
class UnknownType(ASTNode): # For type inference
    def accept(self, visitor, o: object):
        return super().accept(visitor, o)
    def __str__(self):
        return "UnknownType"

class StaticChecker(ASTVisitor):
    def __init__(self) -> None:
        self.env: List[Dict[str, Symbol]] = [{}]
        self.in_loop: int = 0
        self.has_entry: bool = False
        
    def visit(self, node: ASTNode, o: object):
        return node.accept(self, o)
    
    def check_program(self, ast):
        if isinstance(ast, Program):
            root = ast

        elif isinstance(ast, list):
            if (len(ast) == 2
                and all(isinstance(item, list) for item in ast)):
                consts, funcs = ast
            else:                
                consts = [d for d in ast if isinstance(d, ConstDecl)]
                funcs  = [d for d in ast if isinstance(d, FuncDecl)]
            root = Program(consts, funcs)

        else:
            raise TypeError("Unexpected AST root")

        self.visit(root, None)  


    def _current_scope(self) -> Dict[str, Symbol]:
        """Get the current scope dictionary"""
        return self.env[-1] if self.env else {}
    
    def _lookup(self, name: str) -> Optional[Symbol]:
        """Look up a symbol in the current scope and its enclosing scopes"""
        name = str(name)
        return next((scope[name]  for scope in reversed(self.env) if name in scope), None)
    
    def _declare(self, symbol: Symbol, err: StaticError) -> None:
        """Declare a symbol in the current scope, raise error if already declared"""
        current_scope = self._current_scope()
        if symbol.name in current_scope:
            raise Redeclared(symbol.kind, symbol.name)
        current_scope[symbol.name] = symbol

    def _unify(self, t1: ASTNode, t2: ASTNode, stmt_ctx: bool = False, node: Optional[ASTNode] = None): # Unification algorithm
        if isinstance(t1, UnknownType):
            return t2
        if isinstance(t2, UnknownType):
            return t1
        if isinstance(t1, ArrayType) and isinstance(t2, ArrayType):
            if t1.size != t2.size:
                err = TypeMismatchInStatement if stmt_ctx else TypeMismatchInExpression
                raise err(node)
            elem_type = self._unify(t1.element_type, t2.element_type, stmt_ctx, node)
            return ArrayType(elem_type, t1.size)

        if type(t1) is not type(t2):
            err = TypeMismatchInStatement if stmt_ctx else TypeMismatchInExpression
            raise err(node)
        return t1
        
    def visit_program(self, node: Program, o: object):
        self.env = [{}]
        self.has_entry = False

        for decl in node.const_decls:
            self.visit(decl, o)
            
        for decl in node.func_decls:
            param_type = [param.param_type or UnknownType() for param in decl.params]
            symbol = Symbol(decl.name, (param_type, decl.return_type or VoidType()), "Function")
            self._declare(symbol, Redeclared(FunctionMarker(), decl.name))
            ret_type = decl.return_type or VoidType()
            if decl.name == "main" and len(decl.params) == 0 and isinstance(ret_type, VoidType):
                self.has_entry = True
                
        if not self.has_entry:
            raise NoEntryPoint()
        for decl in node.func_decls:
            self.visit(decl, o)
            
    def visit_const_decl(self, node: ConstDecl, o: object):
        sym = Symbol(node.name, node.type_annotation or UnknownType(), "Constant")
        self._declare(sym, Redeclared(IdentifierMarker(), node.name))
        return None
    
    def visit_param(self, node: Param, o: object):
        sym = Symbol(node.name, node.param_type or UnknownType(), "Parameter")
        self._declare(sym, Redeclared(IdentifierMarker(), node.name))
        return None
    
    def visit_func_decl(self, node: FuncDecl, o: object):
        self.env.append({})

        for param in node.params:
            self.visit(param, o)

        for stmt in node.body:
            if stmt is not None:
                self.visit(stmt, node.return_type or VoidType())
                
        if not isinstance(node.return_type, VoidType):
            def ensure(stmt):
                return (
                    isinstance(stmt, ReturnStmt)
                    or (isinstance(stmt, BlockStmt) and any(ensure(s) for s in stmt.statements))
                    or (isinstance(stmt, IfStmt) and (
                        ensure(stmt.then_stmt)
                        and all(ensure(b) for _, b in stmt.elif_branches)
                        and stmt.else_stmt is not None and ensure(stmt.else_stmt))
                    )
                )
            if not any(ensure(s) for s in node.body):
                raise TypeMismatchInStatement(node)
            

        self.env.pop()
        return None
        
    def visit_int_type(self, node: IntType, o: object):
        return node
    
    def visit_float_type(self, node: FloatType, o: object):
        return node
    
    def visit_bool_type(self, node: BoolType, o: object):
        return node
    
    def visit_string_type(self, node: StringType, o: object):
        return node
    
    def visit_void_type(self, node: VoidType, o: object):
        return node
    
    def visit_array_type(self, node: ArrayType, o: object):
        if not isinstance(node.size, int) or node.size < 0:
            raise TypeCannotBeInferred(node)
        return node

    def visit_var_decl(self, node: VarDecl, o: object):
        if (node.type_annotation is None
                and isinstance(node.value, ArrayLiteral)
                and not node.value.elements):
            raise TypeCannotBeInferred(node)
        sym = Symbol(node.name, node.type_annotation or UnknownType(), "Variable")

        if isinstance(sym.typ, VoidType):
            raise TypeMismatchInStatement(node)

        self._declare(sym, Redeclared(IdentifierMarker(), node.name))

        init_type = self.visit(node.value, o) if node.value else UnknownType()
        
        if node.type_annotation is not None and isinstance(init_type, ArrayType) and isinstance(init_type.element_type, UnknownType):
            raise TypeMismatchInStatement(node)

        if node.type_annotation is not None:
            self.visit(node.type_annotation, o)
            if isinstance(init_type, VoidType):
                raise TypeMismatchInStatement(node)
            if isinstance(init_type, UnknownType):
                return 
            self._unify(node.type_annotation, init_type, stmt_ctx=True, node=node)
            return

        if isinstance(init_type, ArrayType) and isinstance(init_type.element_type, UnknownType):
            raise TypeCannotBeInferred(node)

        if node.type_annotation is not None:
            self.visit(node.type_annotation, o)
            if isinstance(init_type, VoidType):
                raise TypeMismatchInStatement(node)
            if isinstance(init_type, UnknownType):
                return 
            self._unify(node.type_annotation, init_type, stmt_ctx=True, node=node)
            return
        
        if isinstance(init_type, VoidType):
            raise TypeMismatchInStatement(node)
        if isinstance(init_type, UnknownType):
            raise TypeCannotBeInferred(node)

        self._current_scope()[node.name] = sym._replace(typ=init_type)

    
    def visit_assignment(self, node: Assignment, o: object):
        rhs = self.visit(node.value, o)
        
        if isinstance(node.lvalue, IdLValue):
            sym = self._lookup(node.lvalue.name)
            if not sym:
                raise Undeclared(IdentifierMarker(), node.lvalue.name)
            
            if sym.kind == "Constant" or sym.kind == "Parameter":
                raise TypeMismatchInStatement(node)
            lhs_type = sym.typ
            res_type = self._unify(lhs_type, rhs, stmt_ctx=True, node=node)
            if isinstance(sym.typ, UnknownType) and not isinstance(res_type, UnknownType):
                self._current_scope()[node.lvalue.name] = sym._replace(typ=res_type)
        else:
            lhs_type = self.visit(node.lvalue, o)
            self._unify(lhs_type, rhs, stmt_ctx=True, node=node)

    def visit_if_stmt(self, node: IfStmt, o: object):
        condition = self.visit(node.condition, o)
        if not isinstance(condition, BoolType):
            raise TypeMismatchInStatement(node)

        self.visit(node.then_stmt, o)
        for cond, block in node.elif_branches:
            self.visit(cond, o)
            self.visit(block, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)
        return None
            
    def visit_while_stmt(self, node: WhileStmt, o: object):
        condtion_type = self.visit(node.condition, o)
        unified = self._unify(condtion_type, BoolType(), stmt_ctx=True, node=node)
        if (isinstance(node.condition, Identifier)) and isinstance(condtion_type, UnknownType):
            sym = self._lookup(node.condition.name)
            self._current_scope()[node.condition.name] = sym._replace(typ=BoolType())
            
        self.in_loop += 1
        self.visit(node.body, o)
        self.in_loop -= 1
        
        return None
    
    def visit_for_stmt(self, node: ForStmt, o: object):
        self.env.append({}) 

        iterable_type = self.visit(node.iterable, o)
        if not isinstance(iterable_type, ArrayType):
            raise TypeMismatchInStatement(node)

        self._declare(
            Symbol(node.variable, iterable_type.element_type, "Variable"),
            Redeclared("Variable", node.variable)
        )

        self.in_loop += 1
        # self.visit(node.body, o)
        for stmt in node.body.statements:
            self.visit(stmt, o)
        self.in_loop -= 1

        self.env.pop()


    def visit_return_stmt(self, node: ReturnStmt, o: object):
        if isinstance(o, VoidType):
            if node.value is not None:
                raise TypeMismatchInStatement(node)
            return
        if node.value is None:
            raise TypeMismatchInStatement(node)
        return_type = self.visit(node.value, o)
        self._unify(return_type, o, stmt_ctx=True, node=node)

    def visit_break_stmt(self, node: BreakStmt, o: object):
        if self.in_loop == 0:
            raise MustInLoop(node)
        return None
    
    def visit_continue_stmt(self, node: ContinueStmt, o: object):
        if self.in_loop == 0:
            raise MustInLoop(node)
        return None
    
    def visit_expr_stmt(self, node: ExprStmt, o: object):
        if isinstance(node.expr, FunctionCall):
            try:
                expr_type = self.visit_function_call(node.expr, o, stmt_ctx=True)
            except TypeMismatchInStatement as e:
                raise e
            except TypeMismatchInExpression as e:
                raise TypeMismatchInStatement(node.expr)
            return
        else:
            expr_type = self.visit(node.expr, o)
            if not isinstance(expr_type, VoidType):
                raise TypeMismatchInStatement(expr_type)

        
    def visit_block_stmt(self, node: BlockStmt, o: object):
        self.env.append({})
        for stmt in node.statements:
            self.visit(stmt, o)
        self.env.pop()
        return None
    
    def visit_id_lvalue(self, node: IdLValue, o: object) -> ASTNode:
        sym = self._lookup(node.name)
        if not sym:
            raise Undeclared(IdentifierMarker(), node.name)
        if sym.kind == "Constant":
            raise TypeMismatchInExpression(node)
        return sym.typ
    
    def visit_array_access_lvalue(self, node: ArrayAccessLValue, o: object) -> ASTNode:
        array_type = self.visit(node.array, o)

        if not isinstance(array_type, ArrayType):
            raise TypeMismatchInExpression(node)

        index_type = self.visit(node.index, o)
        try:
            self._unify(index_type, IntType(), stmt_ctx=False, node=node)
        except TypeMismatchInExpression:
            raise TypeMismatchInExpression(node)

        return array_type.element_type
    
    def visit_binary_op(self, node: BinaryOp, o: object) -> ASTNode:
        op = node.operator

        if op == '>>':
            left_type = self.visit(node.left, o)
            right = node.right

            if isinstance(right, Identifier):
                func_sym = self._lookup(right.name)
                if not func_sym or func_sym.kind != "Function":
                    raise Undeclared(FunctionMarker(), right.name)
                param_types, ret_type = func_sym.typ
                if len(param_types) != 1:
                    raise TypeMismatchInExpression(node)
                self._unify(left_type, param_types[0], stmt_ctx=False, node=node)
                return ret_type

            elif isinstance(right, FunctionCall):
                if not isinstance(right.function, Identifier):
                    raise TypeMismatchInExpression(node)
                func_sym = self._lookup(right.function.name)
                if not func_sym or func_sym.kind != "Function":
                    raise Undeclared(FunctionMarker(), right.function.name)
                param_types, ret_type = func_sym.typ
                if len(param_types) != len(right.args) + 1:
                    raise TypeMismatchInExpression(node)
                self._unify(left_type, param_types[0], stmt_ctx=False, node=node)
                for arg, expected_type in zip(right.args, param_types[1:]):
                    actual_type = self.visit(arg, o)
                    self._unify(actual_type, expected_type, stmt_ctx=False, node=node)
                return ret_type

            else:
                raise TypeMismatchInExpression(node)

        left_t  = self.visit(node.left,  o)
        right_t = self.visit(node.right, o)

        if op in ('==', '!='):
            self._unify(left_t, right_t, stmt_ctx=False, node=node)
            return BoolType()

        elif op == '+':
            if isinstance(left_t, IntType) and isinstance(right_t, IntType):
                return IntType()
            if isinstance(left_t, (IntType, FloatType)) and isinstance(right_t, (IntType, FloatType)):
                return FloatType()
            if isinstance(left_t, StringType) or isinstance(right_t, StringType):
                return StringType()
            raise TypeMismatchInExpression(node)
        elif op in ('-', '*', '/'):
            if isinstance(left_t, IntType) and isinstance(right_t, IntType):
                return IntType()
            if isinstance(left_t, (IntType, FloatType)) and isinstance(right_t, (IntType, FloatType)):
                return FloatType()
            raise TypeMismatchInExpression(node)
        elif op == '%':
            if isinstance(left_t, IntType) and isinstance(right_t, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)

        elif op in ('&&', '||'):
            self._unify(left_t, BoolType(), stmt_ctx=False, node=node)
            self._unify(right_t, BoolType(), stmt_ctx=False, node=node)
            return BoolType()

        elif op in ('>=', '<=', '>', '<'):
            if isinstance(left_t, (IntType, FloatType)) and isinstance(right_t, (IntType, FloatType)):
                return BoolType()
            raise TypeMismatchInExpression(node)
        

    def visit_unary_op(self, node: UnaryOp, o: object) -> ASTNode:
        operand_type = self.visit(node.operand, o)
        if node.operator == '!' and isinstance(operand_type, BoolType):
            return BoolType()
        if node.operator in ('-', '+') and isinstance(operand_type, (IntType, FloatType)):
            return operand_type
        raise TypeMismatchInExpression(node)

    def visit_function_call(self, node: FunctionCall, o: object, stmt_ctx: bool = False) -> ASTNode:
        if not isinstance(node.function, Identifier):
            err = TypeMismatchInStatement if stmt_ctx else TypeMismatchInExpression
            raise err(node)

        func_sym = self._lookup(node.function.name)
        if func_sym is None:
            raise Undeclared(FunctionMarker(), node.function.name)
        if func_sym.kind != "Function":
            err = TypeMismatchInStatement if stmt_ctx else TypeMismatchInExpression
            raise err(node)

        param_types, ret_type = func_sym.typ
        if len(node.args) != len(param_types):
            err = TypeMismatchInStatement if stmt_ctx else TypeMismatchInExpression
            raise err(node)

        for arg, ptyp in zip(node.args, param_types):
            arg_type = self.visit(arg, o)
            self._unify(arg_type, ptyp, stmt_ctx=stmt_ctx, node=node)

        return ret_type

    def visit_array_access(self, node: ArrayAccess, o: object) -> ASTNode:
        array_typ = self.visit(node.array, o)
        if not isinstance(array_typ, ArrayType):
            raise TypeMismatchInExpression(node)
        idx_typ = self.visit(node.index, o)
        try:
            self._unify(idx_typ, IntType(), stmt_ctx=False, node=node)
        except TypeMismatchInExpression:
            raise TypeMismatchInExpression(node)
        return array_typ.element_type
    
    def visit_array_literal(self, node: ArrayLiteral, o: object) -> ASTNode:
        if not node.elements:
            return ArrayType(UnknownType(), 0)

        element_types = [self.visit(elem, o) for elem in node.elements]

        if any(isinstance(t, UnknownType) for t in element_types):
            return ArrayType(UnknownType(), len(element_types))

        element_type = element_types[0]

        try:
            for t in element_types[1:]:
                element_type = self._unify(t, element_type, stmt_ctx=False, node=node)
            return ArrayType(element_type, len(node.elements))
        except TypeMismatchInExpression:
            return ArrayType(UnknownType(), len(node.elements))

        
    def visit_identifier(self, node: Identifier, o: object) -> ASTNode:
        sym = self._lookup(node.name)
        if not sym:
            raise Undeclared(IdentifierMarker(), node.name)
        return sym.typ
    
    def visit_integer_literal(self, node: IntegerLiteral, o: object) -> ASTNode:
        return IntType()
    
    def visit_float_literal(self, node: FloatLiteral, o: object) -> ASTNode:
        return FloatType()
    
    def visit_boolean_literal(self, node: BooleanLiteral, o: object) -> ASTNode:
        return BoolType()
    
    def visit_string_literal(self, node: StringLiteral, o: object) -> ASTNode:
        return StringType()

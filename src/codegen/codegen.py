"""
Code Generator for HLang programming language.
This module implements a code generator that traverses AST nodes and generates
Java bytecode using the Emitter and Frame classes.
"""

from ast import Sub
from typing import Any, List, Optional
from ..utils.visitor import ASTVisitor
from ..utils.nodes import *
from .emitter import Emitter
from .frame import Frame
from .error import IllegalOperandException, IllegalRuntimeException
from .io import IO_SYMBOL_LIST
from .utils import *
from functools import *


class CodeGenerator(ASTVisitor):
    def __init__(self):
        self.class_name = "HLang"
        self.emit = Emitter(self.class_name + ".j")
        self.consts = {}

    def visit_program(self, node: "Program", o: Any = None):
        self.emit.print_out(self.emit.emit_prolog(self.class_name, "java/lang/Object"))

        for const_decl in node.const_decls:
            self.visit(const_decl, None)
        
        global_env = SubBody(None, IO_SYMBOL_LIST)
        for func_decl in node.func_decls:
            param_types = list(map(lambda x: x.param_type, func_decl.params))
            global_env.sym.append(Symbol(
                func_decl.name,
                FunctionType(param_types, func_decl.return_type),
                CName(self.class_name)
            ))
        for func_decl in node.func_decls:
            self.visit_func_decl(func_decl, global_env)

        self.generate_method(
            FuncDecl("<init>", [], VoidType(), []),
            SubBody(Frame("<init>", VoidType()), []),
        )
        self.emit.emit_epilog()

    def generate_method(self, node: "FuncDecl", o: SubBody = None):
        frame = o.frame

        is_init = node.name == "<init>"
        is_main = node.name == "main"

        param_types = list(map(lambda x: x.param_type, node.params))
        if is_main:
            param_types = [ArrayType(StringType(), 0)]
        else:
            param_types = [p.param_type for p in node.params]
        return_type = node.return_type

        self.emit.print_out(
            self.emit.emit_method(
                node.name, FunctionType(param_types, return_type), not is_init
            )
        )

        frame.enter_scope(True)

        from_label = frame.get_start_label()
        to_label = frame.get_end_label()

        # Generate code for parameters
        if is_init:
            this_idx = frame.get_new_index()

            self.emit.print_out(
                self.emit.emit_var(
                    this_idx, "this", ClassType(self.class_name), from_label, to_label
                )
            )
        elif is_main:
            args_idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    args_idx, "args", ArrayType(StringType(), 0), from_label, to_label
                )
            )
        else:
            o = reduce(lambda acc, cur: self.visit(cur, acc), node.params, o)

        self.emit.print_out(self.emit.emit_label(from_label, frame))

        # Generate code for body

        if is_init:
            self.emit.print_out(
                self.emit.emit_read_var(
                    "this", ClassType(self.class_name), this_idx, frame
                )
            )
            self.emit.print_out(self.emit.emit_invoke_special(frame))

        o = reduce(lambda acc, cur: self.visit(cur, acc), node.body, o)

        if type(return_type) is VoidType:
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))

        self.emit.print_out(self.emit.emit_label(to_label, frame))

        self.emit.print_out(self.emit.emit_end_method(frame))

        frame.exit_scope()

    def visit_const_decl(self, node: "ConstDecl", o: Any = None):
        self.consts[node.name] = node.value
        if not isinstance(node.type_annotation, ArrayType):
            const_type = self.visit(node.type_annotation)
            # jvm_desc   = self.emit.get_jvm_type(const_type)
            # self.emit.print_out(
            #     self.emit.jvm.emitSTATICFIELD(node.name, jvm_desc, True)
            # )
            self.emit.print_out(self.emit.emit_attribute(node.name, const_type, True))
        return o

    def visit_func_decl(self, node: "FuncDecl", o: SubBody = None):
        frame = Frame(node.name, node.return_type)
        self.generate_method(node, SubBody(frame, o.sym))
        param_types = list(map(lambda x: x.param_type, node.params))
        return SubBody(
            None,
            [
                Symbol(
                    node.name,
                    FunctionType(param_types, node.return_type),
                    CName(self.class_name),
                )
            ]
            + o.sym,
        )

    def visit_param(self, node: "Param", o: Any = None):
        idx = o.frame.get_new_index()
        self.emit.print_out(
            self.emit.emit_var(
                idx,
                node.name,
                node.param_type,
                o.frame.get_start_label(),
                o.frame.get_end_label(),
            )
        )

        return SubBody(
            o.frame,
            [Symbol(node.name, node.param_type, Index(idx))] + o.sym,
        )

    # Type system

    def visit_int_type(self, node: "IntType", o: Any = None):
        return IntType()

    def visit_float_type(self, node: "FloatType", o: Any = None):
        return FloatType()

    def visit_bool_type(self, node: "BoolType", o: Any = None):
        return BoolType()

    def visit_string_type(self, node: "StringType", o: Any = None):
        return StringType()

    def visit_void_type(self, node: "VoidType", o: Any = None):
        return VoidType()

    def visit_array_type(self, node: "ArrayType", o: Any = None):
        element_type = self.visit(node.element_type, o)
        return ArrayType(element_type, node.size)

    # Statements

    def visit_var_decl(self, node: "VarDecl", o: SubBody = None):
        idx = o.frame.get_new_index()
        self.emit.print_out(
            self.emit.emit_var(
                idx,
                node.name,
                node.type_annotation,
                o.frame.get_start_label(),
                o.frame.get_end_label(),
            )
        )

        if node.value is not None:
            self.visit(
                Assignment(IdLValue(node.name), node.value),
                SubBody(
                    o.frame,
                    [Symbol(node.name, node.type_annotation, Index(idx))] + o.sym,
                ),
            )
        return SubBody(
            o.frame,
            [Symbol(node.name, node.type_annotation, Index(idx))] + o.sym,
        )

    def visit_assignment(self, node: "Assignment", o: SubBody = None):
        if isinstance(node.lvalue, ArrayAccessLValue):
            arr_node = node.lvalue.array
            arr_name = arr_node.name if isinstance(arr_node, Identifier) else arr_node
            sym = next((s for s in o.sym if s.name == arr_name), None)
            if sym is None:
                raise IllegalRuntimeException(f"Array '{arr_name}' not defined")

            self.emit.print_out(
                self.emit.emit_read_var(sym.name, sym.type, sym.value.value, o.frame)
            )
            icode, _ = self.visit(node.lvalue.index, Access(o.frame, o.sym))
            self.emit.print_out(icode)
            vcode, _ = self.visit(node.value, Access(o.frame, o.sym))
            self.emit.print_out(vcode)
            self.emit.print_out(self.emit.emit_astore(sym.type.element_type, o.frame))
            return o

        value_code, _ = self.visit(node.value, Access(o.frame, o.sym))
        self.emit.print_out(value_code)
        lvalue_code, _ = self.visit(node.lvalue, Access(o.frame, o.sym))
        self.emit.print_out(lvalue_code)
        return o

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        frame = o.frame
        false_label = frame.get_new_label()  
        end_label = frame.get_new_label()    
        
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(false_label, frame))

        self.visit(node.then_stmt, o)
        
        has_then_return = self._has_terminal_return(node.then_stmt)
        if not has_then_return and (node.elif_branches or node.else_stmt is not None):
            self.emit.print_out(self.emit.emit_goto(end_label, frame))
    

        self.emit.print_out(self.emit.emit_label(false_label, frame))

        if node.elif_branches:
            for i, (elif_cond, elif_stmt) in enumerate(node.elif_branches):
                next_label = frame.get_new_label()
                
                elif_cond_code, _ = self.visit(elif_cond, Access(frame, o.sym))
                self.emit.print_out(elif_cond_code)
                self.emit.print_out(self.emit.emit_if_false(next_label, frame))
                
                self.visit(elif_stmt, o)
                has_elif_return = self._has_terminal_return(elif_stmt)
                if not has_elif_return and (i < len(node.elif_branches) - 1 or node.else_stmt is not None):
                    self.emit.print_out(self.emit.emit_goto(end_label, frame))

                self.emit.print_out(self.emit.emit_label(next_label, frame))

        if node.else_stmt is not None:
            self.visit(node.else_stmt, o)

        self.emit.print_out(self.emit.emit_label(end_label, frame))
        return o
    
    def _has_terminal_return(self, stmt):
        if isinstance(stmt, ReturnStmt):
            return True
        elif isinstance(stmt, BlockStmt) and stmt.statements:
            return isinstance(stmt.statements[-1], ReturnStmt) or self._has_terminal_return(stmt.statements[-1])
        return False

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        frame = o.frame
        sym = o.sym

        frame.enter_loop()
        continue_label = frame.get_continue_label()
        break_label = frame.get_break_label()

        self.emit.print_out(self.emit.emit_label(continue_label, frame))

        cond_code, cond_type = self.visit(node.condition, Access(frame, sym))
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(break_label, frame))

        self.visit(node.body, o)

        self.emit.print_out(self.emit.emit_goto(continue_label, frame))

        self.emit.print_out(self.emit.emit_label(break_label, frame))
        frame.exit_loop()
        return o

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        frame = o.frame
        base_sym = o.sym

        idx_slot  = frame.get_new_index()
        lim_slot  = frame.get_new_index()
        arr_slot  = frame.get_new_index()

        start_lbl = frame.get_start_label()
        end_lbl   = frame.get_end_label()

        self.emit.print_out(self.emit.emit_var(idx_slot, "$idx", IntType(), start_lbl, end_lbl))
        self.emit.print_out(self.emit.emit_var(lim_slot, "$lim", IntType(), start_lbl, end_lbl))

        self.emit.print_out(self.emit.emit_push_iconst(0, frame))
        self.emit.print_out(self.emit.emit_write_var("$idx", IntType(), idx_slot, frame))

        array_code, array_type = self.visit(node.iterable, Access(frame, base_sym))
        self.emit.print_out(array_code)
        self.emit.print_out(self.emit.emit_var(arr_slot, "$arr", array_type, start_lbl, end_lbl))
        self.emit.print_out(self.emit.emit_write_var("$arr", array_type, arr_slot, frame))

        self.emit.print_out(self.emit.emit_read_var("$arr", array_type, arr_slot, frame))
        self.emit.print_out(self.emit.emit_array_length(frame))
        self.emit.print_out(self.emit.emit_write_var("$lim", IntType(), lim_slot, frame))

        element_type = array_type.element_type
        iter_slot = frame.get_new_index()
        self.emit.print_out(self.emit.emit_var(iter_slot, node.variable, element_type, start_lbl, end_lbl))
        var_sym = Symbol(node.variable, element_type, Index(iter_slot))

        frame.enter_loop()
        loop_head = frame.get_new_label()
        break_label = frame.get_break_label()
        continue_label = frame.get_continue_label()

        self.emit.print_out(self.emit.emit_label(loop_head, frame))

        self.emit.print_out(self.emit.emit_read_var("$idx", IntType(), idx_slot, frame))
        self.emit.print_out(self.emit.emit_read_var("$lim", IntType(), lim_slot, frame))
        self.emit.print_out(self.emit.emit_ificmpge(break_label, frame))

        self.emit.print_out(self.emit.emit_read_var("$arr", array_type, arr_slot, frame))
        self.emit.print_out(self.emit.emit_read_var("$idx", IntType(), idx_slot, frame))
        self.emit.print_out(self.emit.emit_aload(element_type, frame))
        self.emit.print_out(self.emit.emit_write_var(node.variable, element_type, iter_slot, frame))

        body_env = SubBody(frame,
            [var_sym,
             Symbol("$arr", array_type, Index(arr_slot)),
             Symbol("$lim", IntType(), Index(lim_slot)),
             Symbol("$idx", IntType(), Index(idx_slot))] + base_sym)

        self.visit(node.body, body_env)

        self.emit.print_out(self.emit.emit_label(continue_label, frame))
        self.emit.print_out(self.emit.emit_read_var("$idx", IntType(), idx_slot, frame))
        self.emit.print_out(self.emit.emit_push_iconst(1, frame))
        self.emit.print_out(self.emit.emit_add_op("+", IntType(), frame))
        self.emit.print_out(self.emit.emit_write_var("$idx", IntType(), idx_slot, frame))
        self.emit.print_out(self.emit.emit_goto(loop_head, frame))

        self.emit.print_out(self.emit.emit_label(break_label, frame))
        frame.exit_loop()
        return o

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        frame = o.frame
        if node.value is not None:
            code, typ = self.visit(node.value, Access(frame, o.sym))
            self.emit.print_out(code)
            self.emit.print_out(
                self.emit.emit_return(typ, frame)
            )
        else:
            self.emit.print_out(
                self.emit.emit_return(VoidType(), frame)
            )
        return o

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        self.emit.print_out(
            self.emit.emit_goto(o.frame.get_break_label(), o.frame)
        )
        return o

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        self.emit.print_out(
            self.emit.emit_goto(o.frame.get_continue_label(), o.frame)
        )
        return o

    def visit_expr_stmt(self, node: "ExprStmt", o: SubBody = None):
        code, typ = self.visit(node.expr, Access(o.frame, o.sym))
        self.emit.print_out(code)
        return o

    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        frame = o.frame
        frame.enter_scope(False)
        
        self.emit.print_out(self.emit.emit_label(frame.get_start_label(), frame))
        
        for stmt in node.statements:
            o = self.visit(stmt, SubBody(frame, o.sym))
        self.emit.print_out(self.emit.emit_label(frame.get_end_label(), frame))

        frame.exit_scope()
        return o

    # Left-values

    def visit_id_lvalue(self, node: "IdLValue", o: Access = None):
        sym = next(
            filter(lambda x: x.name == node.name, o.sym),
            False,
        )

        if type(sym.value) is Index:
            code = self.emit.emit_write_var(
                sym.name, sym.type, sym.value.value, o.frame
            )

        return code, sym.type

    def visit_array_access_lvalue(self, node: "ArrayAccessLValue", o: Any = None):
        array_code = ""
        array_type = None
        
        if isinstance(node.array, str):
            sym = next((sym for sym in o.sym if sym.name == node.array), None)
            if sym is not None:
                array_code = self.emit.emit_read_var(
                    sym.name, sym.type, sym.value.value, o.frame
                )
                array_type = sym.type
            else:
                raise IllegalRuntimeException(f"Array '{node.array}' not defined")
        else:
            array_code, array_type = self.visit(node.array, Access(o.frame, o.sym))
                
        index_code, index_type = self.visit(node.index, Access(o.frame, o.sym))
        return array_code + index_code, array_type.element_type

    # Expressions

    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        left_code, left_type = self.visit(node.left, Access(o.frame, o.sym))
        right_code, right_type = self.visit(node.right, Access(o.frame, o.sym))
        code = ""
        op = node.operator
        if op == "+" and (isinstance(left_type, StringType) or isinstance(right_type, StringType)):

            code += left_code
            if not isinstance(left_type, StringType):
                code += self.emit.emit_invoke_static(
                    "java/lang/String/valueOf",
                    FunctionType([left_type], StringType()),
                    o.frame
                )

            code += right_code
            if not isinstance(right_type, StringType):
                code += self.emit.emit_invoke_static(
                    "java/lang/String/valueOf",
                    FunctionType([right_type], StringType()),
                    o.frame
                )

            code += self.emit.emit_invoke_virtual(
                "java/lang/String/concat",
                FunctionType([StringType()], StringType()),
                o.frame
            )
            return code, StringType()
    
        if op in ["+", "-", "*", "/"]:
            is_int = isinstance(left_type, IntType) and isinstance(right_type, IntType)
            result_type = IntType() if is_int else FloatType()

            code = left_code
            if not is_int and isinstance(left_type, IntType):
                code += self.emit.emit_i2f(o.frame)
            code += right_code
            if not is_int and isinstance(right_type, IntType):
                code += self.emit.emit_i2f(o.frame)

            if op in ["+", "-"]:
                code += self.emit.emit_add_op(op, result_type, o.frame)
            elif op in ["*", "/"]:
                code += self.emit.emit_mul_op(op, result_type, o.frame)

            return code, result_type
        
        elif op == "%":
            if isinstance(left_type, IntType) or isinstance(right_type, IntType):
                code = left_code + right_code + self.emit.emit_mod(o.frame)
                return code, IntType()
            else:
                raise IllegalOperandException("Illegal operand for '%' operator")
            
        elif op in ["==", "!="]:
            allow_type = (IntType, FloatType, BoolType, StringType)
            if type(left_type) is not type(right_type) or not isinstance(left_type, allow_type):
                raise IllegalOperandException(
                    f"Illegal operator '{op}' for types {left_type} and {right_type}"
                )

            code = left_code + right_code
            if isinstance(left_type, (IntType, FloatType)):
                code += self.emit.emit_re_op(op, left_type, o.frame)
                return code, BoolType()

            if isinstance(left_type, BoolType):
                code += self.emit.emit_re_op(op, IntType(), o.frame)
                return code, BoolType()

            if isinstance(left_type, StringType):
                code += self.emit.emit_invoke_virtual(
                    "java/lang/String/equals",
                    FunctionType([ClassType("java/lang/Object")], BoolType()),  
                    o.frame
                )
                label_true = o.frame.get_new_label()
                label_false = o.frame.get_new_label()
                if op == "==":
                    code += self.emit.emit_if_true(label_true, o.frame)
                    code += self.emit.emit_push_iconst(0, o.frame)
                    code += self.emit.emit_goto(label_false, o.frame)
                    code += self.emit.emit_label(label_true, o.frame)
                    code += self.emit.emit_push_iconst(1, o.frame)
                    code += self.emit.emit_label(label_false, o.frame)
                else:
                    code += self.emit.emit_if_true(label_true, o.frame)
                    code += self.emit.emit_push_iconst(1, o.frame)
                    code += self.emit.emit_goto(label_false, o.frame)
                    code += self.emit.emit_label(label_true, o.frame)
                    code += self.emit.emit_push_iconst(0, o.frame)
                    code += self.emit.emit_label(label_false, o.frame)
                return code, BoolType()

        elif op in ["<", "<=", ">", ">="]:
            code = ""
            if isinstance(left_type, FloatType) and isinstance(right_type, IntType):
                code += left_code
                code += right_code
                code += self.emit.emit_i2f(o.frame)   
                code += self.emit.emit_re_op(op, FloatType(), o.frame)
                return code, BoolType()

            if isinstance(left_type, IntType) and isinstance(right_type, FloatType):
                code += left_code
                code += self.emit.emit_i2f(o.frame)
                code += right_code
                code += self.emit.emit_re_op(op, FloatType(), o.frame)
                return code, BoolType()

            code += left_code + right_code
            optype = FloatType() if isinstance(left_type, FloatType) else IntType()
            code += self.emit.emit_re_op(op, optype, o.frame)
            return code, BoolType()
        elif op in ["&&"]:
            new_label = o.frame.get_new_label() 
            end_label = o.frame.get_new_label()
            
            code = left_code
            code += self.emit.emit_if_false(new_label, o.frame)
            
            code += right_code
            code += self.emit.emit_if_false(new_label, o.frame)
            
            code += self.emit.emit_push_iconst(1, o.frame)
            code += self.emit.emit_goto(end_label, o.frame)
            
            code += self.emit.emit_label(new_label, o.frame)
            code += self.emit.emit_push_iconst(0, o.frame)
            
            code += self.emit.emit_label(end_label, o.frame)
            return code, BoolType()
        elif op == "||":
            new_label = o.frame.get_new_label()
            end_label = o.frame.get_new_label()
            
            code = left_code
            code += self.emit.emit_if_true(new_label, o.frame)
            
            code += right_code
            code += self.emit.emit_if_true(new_label, o.frame)
            
            code += self.emit.emit_push_iconst(0, o.frame)
            code += self.emit.emit_goto(end_label, o.frame)
            
            code += self.emit.emit_label(new_label, o.frame)
            code += self.emit.emit_push_iconst(1, o.frame)
            
            code += self.emit.emit_label(end_label, o.frame)
            return code, BoolType()
        elif op == ">>":
            code = left_code
            if isinstance(node.right, Identifier):
                function_name = node.right.name
                function_symbol = next(filter(lambda x: x.name == function_name, o.sym), False)
                class_name = function_symbol.value.value
                code += self.emit.emit_invoke_static(
                    f"{class_name}/{function_name}", function_symbol.type, o.frame
                )
                return code, function_symbol.type.return_type
            elif isinstance(node.right, FunctionCall):
                for arg in node.right.args:
                    arg_code, arg_type = self.visit(arg, Access(o.frame, o.sym))
                    code += arg_code
                function_name = node.right.function.name
                function_symbol = next(filter(lambda x: x.name == function_name, o.sym), False)
                class_name = function_symbol.value.value
                code += self.emit.emit_invoke_static(
                    f"{class_name}/{function_name}", function_symbol.type, o.frame
                )
                return code, function_symbol.type.return_type
    
        raise IllegalOperandException(f"Illegal operator '{op}' for types {left_type} and {right_type}")

    def visit_unary_op(self, node: "UnaryOp", o: Any = None):
        opcode, optype = self.visit(node.operand, o)
        op = node.operator
        if op == "-":
            opcode += self.emit.emit_neg_op(optype, o.frame)
            return opcode, optype
        elif op == "!":
            if not isinstance(optype, BoolType):
                raise IllegalOperandException("Illegal operand for '!' operator")
            opcode += self.emit.emit_not(BoolType(), o.frame)
            return opcode, optype
        
        else:
            raise IllegalOperandException(op)

    def visit_function_call(self, node: "FunctionCall", o: Access = None):
        function_name = node.function.name
        
        if function_name == "len" and len(node.args) == 1:
            arg = node.args[0]
            arg_code, arg_type = self.visit(arg, Access(o.frame, o.sym))
            
            if isinstance(arg_type, StringType):
                return (
                    arg_code + 
                    self.emit.emit_invoke_virtual(
                        "java/lang/String/length",  
                        FunctionType([], IntType()), 
                        o.frame
                    ),
                    IntType()
                )
            elif isinstance(arg_type, ArrayType):
                return (
                    arg_code + self.emit.emit_array_length(o.frame),
                    IntType()
                )
        
        function_symbol = next((x for x in o.sym if x.name == function_name), None)
        if function_symbol is None:
            raise IllegalRuntimeException(f"Function '{function_name}' not defined")
            
        class_name = function_symbol.value.value
        argument_codes = []
        for argument in node.args:
            ac, at = self.visit(argument, Access(o.frame, o.sym))
            argument_codes += [ac]

        return (
            "".join(argument_codes)
            + self.emit.emit_invoke_static(
                class_name + "/" + function_name, function_symbol.type, o.frame
            ),
            function_symbol.type.return_type
        )

    def visit_array_access(self, node: "ArrayAccess", o: Any = None):
        array_code, array_type = self.visit(node.array, Access(o.frame, o.sym))
        index_code, index_type = self.visit(node.index, Access(o.frame, o.sym))
        code = array_code + index_code
        code += self.emit.emit_aload(
            array_type.element_type, o.frame
        )
        return code, array_type.element_type

    def visit_array_literal(self, node: "ArrayLiteral", o: Any = None):
        elems = node.elements
        first_code, elem_type = self.visit(elems[0], Access(o.frame, o.sym))
        size = len(elems)
        code = self.emit.emit_push_iconst(size, o.frame)
        code += self.emit.emit_new_array(self.emit.get_full_type(elem_type), o.frame)
        for i, e in enumerate(elems):
            ec, et = self.visit(e, Access(o.frame, o.sym))
            code += self.emit.emit_dup(o.frame)
            code += self.emit.emit_push_iconst(i, o.frame)
            code += ec
            code += self.emit.emit_astore(elem_type, o.frame)
        return code, ArrayType(elem_type, size)

    def visit_identifier(self, node: "Identifier", o: Any = None):
        if node.name in self.consts:
            return self.visit(self.consts[node.name], o)
        
        sym = next((x for x in o.sym if x.name == node.name), None)
        if sym is None:
            raise IllegalRuntimeException(f"Identifier '{node.name}' not defined")
            
        if isinstance(sym.value, Index):
            code = self.emit.emit_read_var(
                sym.name, sym.type, sym.value.value, o.frame
            )
            return code, sym.type
        elif isinstance(sym.value, CName):
            return "", sym.type
        else:
            raise IllegalRuntimeException(f"Unsupported identifier type: {type(sym.value)}")

    # Literals

    def visit_integer_literal(self, node: "IntegerLiteral", o: Access = None):
        return self.emit.emit_push_iconst(node.value, o.frame), IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return self.emit.emit_push_fconst(node.value, o.frame), FloatType()

    def visit_boolean_literal(self, node: "BooleanLiteral", o: Any = None):
        return self.emit.emit_push_iconst(1 if node.value else 0, o.frame), BoolType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return (
            self.emit.emit_push_const('"' + node.value + '"', StringType(), o.frame),
            StringType(),
        )

"""
AST Generation module for HLang programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.HLangVisitor import HLangVisitor
from build.HLangParser import HLangParser
from src.utils.nodes import *

class ASTGeneration(HLangVisitor):
    @staticmethod
    def _cat(head, tail):
        return ([head] if head is not None else []) + tail

    def _fold_tail(self, left, tail_ctx, op_lexeme, rhs_getter, next_tail_getter):
        while tail_ctx is not None and tail_ctx.getChildCount() > 0:
            right = self.visit(rhs_getter(tail_ctx))
            left  = BinaryOp(left, op_lexeme, right)
            tail_ctx = next_tail_getter(tail_ctx)
        return left

    def visitProgram(self, ctx: HLangParser.ProgramContext):
        decls  = self.visit(ctx.decl_list())    
        consts = [d for d in decls if isinstance(d, ConstDecl)]
        funcs  = [d for d in decls if isinstance(d, FuncDecl)]
        return Program(consts, funcs)

    def visitDecl_list(self, ctx: HLangParser.Decl_listContext):
        if ctx is None or ctx.getChildCount() == 0:
            return []
        head_ctx = ctx.decl()
        head = self.visit(head_ctx) if head_ctx else None
        tail = []
        tail_ctx = ctx.decl_list() 
        if (tail_ctx                        
            and tail_ctx is not ctx):  
            tail = self.visit(tail_ctx)
        return self._cat(head, tail)       
    
    def visitDecl(self, ctx: HLangParser.DeclContext):
        if ctx.const_decl(): 
            return self.visit(ctx.const_decl())
        elif ctx.func_decl(): 
            return self.visit(ctx.func_decl())
        return None           

    def visitStmt_list_opt(self, ctx: HLangParser.Stmt_list_optContext):
        return [] if ctx is None or ctx.stmt_list() is None else self.visit(ctx.stmt_list())

    def visitStmt_list(self, ctx: HLangParser.Stmt_listContext):
        return self._cat(self.visit(ctx.stmt()), self.visit(ctx.stmt_list_tail()))

    def visitStmt_list_tail(self, ctx: HLangParser.Stmt_list_tailContext):
        return [] if ctx is None or ctx.getChildCount() == 0 else self._cat(self.visit(ctx.stmt()), self.visit(ctx.stmt_list_tail()))

    def visitParam_list_opt(self, ctx: HLangParser.Param_list_optContext):
        return [] if ctx is None or ctx.param_list() is None else self.visit(ctx.param_list())

    def visitParam_list(self, ctx: HLangParser.Param_listContext):
        return self._cat(self.visit(ctx.param()), self.visit(ctx.param_list_tail()))

    def visitParam_list_tail(self, ctx: HLangParser.Param_list_tailContext):
        return [] if ctx is None or ctx.getChildCount() == 0 else self._cat(self.visit(ctx.param()), self.visit(ctx.param_list_tail()))

    def visitElse_if_list(self, ctx: HLangParser.Else_if_listContext):
        return [] if ctx is None or ctx.getChildCount() == 0 else self._cat(self.visit(ctx.else_if_clause()), self.visit(ctx.else_if_list()))

    def visitExpr_list_opt(self, ctx: HLangParser.Expr_list_optContext):
        return [] if ctx is None or ctx.expr_list() is None else self.visit(ctx.expr_list())

    def visitExpr_list(self, ctx: HLangParser.Expr_listContext):
        return self._cat(self.visit(ctx.expression()), self.visit(ctx.expr_list_tail()))

    def visitExpr_list_tail(self, ctx: HLangParser.Expr_list_tailContext):
        return [] if ctx is None or ctx.getChildCount() == 0 else self._cat(self.visit(ctx.expression()), self.visit(ctx.expr_list_tail()))           

    def visitConst_decl(self, ctx: HLangParser.Const_declContext):
        type_node = self.visit(ctx.type_opt()) if ctx.type_opt() else None
        return ConstDecl(ctx.ID().getText(), type_node, self.visit(ctx.expression()))

    def visitVar_decl_stmt(self, ctx: HLangParser.Var_decl_stmtContext):
        type_node = self.visit(ctx.type_opt()) if ctx.type_opt() else None
        return VarDecl(ctx.ID().getText(), type_node, self.visit(ctx.expression()))

    def visitParam(self, ctx: HLangParser.ParamContext):   
        return Param(ctx.ID().getText(), self.visit(ctx.type_spec()))

    def visitType_opt(self, ctx: HLangParser.Type_optContext):
        return None if ctx is None or ctx.type_spec() is None else self.visit(ctx.type_spec())

    def visitType_spec(self, ctx: HLangParser.Type_specContext):
        return self.visit(ctx.primitive_type()) if ctx.primitive_type() else self.visit(ctx.array_type())
    
    def visitPrimitive_type(self, ctx: HLangParser.Primitive_typeContext):
        if ctx.INT(): 
            return IntType()
        elif ctx.FLOAT():  
            return FloatType()
        elif ctx.BOOL(): 
            return BoolType()
        elif ctx.STRING(): 
            return StringType()
        elif ctx.VOID(): 
            return VoidType()
        raise ValueError("Unknown primitive type")

    def visitArray_type(self, ctx: HLangParser.Array_typeContext):
        return ArrayType(self.visit(ctx.type_spec()), int(ctx.INTEGER_LITERAL().getText()))

    def visitFunc_decl(self, ctx: HLangParser.Func_declContext):
        return FuncDecl(ctx.ID().getText(),
                        self.visit(ctx.param_list_opt()),
                        self.visit(ctx.type_spec()),
                        self.visit(ctx.block_stmt()).statements)

    def visitBlock_stmt(self, ctx: HLangParser.Block_stmtContext):
        return BlockStmt(self.visitStmt_list_opt(ctx.stmt_list_opt()))
    
    def visitExpr_stmt(self, ctx: HLangParser.Expr_stmtContext):
        return None if ctx.expression() is None else self.visit(ctx.expression())

    def visitStmt(self, ctx: HLangParser.StmtContext):
        if ctx.var_decl_stmt(): return self.visit(ctx.var_decl_stmt())
        if ctx.assign_stmt():   return self.visit(ctx.assign_stmt())
        if ctx.if_stmt():       return self.visit(ctx.if_stmt())
        if ctx.while_stmt():    return self.visit(ctx.while_stmt())
        if ctx.for_stmt():      return self.visit(ctx.for_stmt())
        if ctx.break_stmt():    return BreakStmt()
        if ctx.continue_stmt(): return ContinueStmt()
        if ctx.return_stmt():   return self.visit(ctx.return_stmt())
        if ctx.expr_stmt():
            expr = self.visit(ctx.expr_stmt())
            return ExprStmt(expr) if expr is not None else None
        if ctx.block_stmt():    return self.visit(ctx.block_stmt())
        return None

    def visitAssign_stmt(self, ctx: HLangParser.Assign_stmtContext):
        return Assignment(self.visit(ctx.lvalue()), self.visit(ctx.expression()))

    def visitReturn_stmt(self, ctx: HLangParser.Return_stmtContext):
        return ReturnStmt(self.visit(ctx.expression_opt()))

    def visitIf_stmt(self, ctx: HLangParser.If_stmtContext):
        condition = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.block_stmt())
        elif_branches = self.visit(ctx.else_if_list()) if ctx.else_if_list() else []
        else_stmt = self.visit(ctx.else_clause_opt())
        return IfStmt(condition, then_stmt, elif_branches, else_stmt)

    def visitElse_if_clause(self, ctx: HLangParser.Else_if_clauseContext):
        return (self.visit(ctx.expression()),
                self.visit(ctx.block_stmt()))

    def visitElse_clause_opt(self, ctx: HLangParser.Else_clause_optContext):
        return None if ctx is None or ctx.block_stmt() is None else self.visit(ctx.block_stmt())

    def visitWhile_stmt(self, ctx: HLangParser.While_stmtContext):
        return WhileStmt(self.visit(ctx.expression()),
                         self.visit(ctx.block_stmt()))

    def visitFor_stmt(self, ctx: HLangParser.For_stmtContext):
        return ForStmt(ctx.ID().getText(),
                       self.visit(ctx.expression()),
                       self.visit(ctx.block_stmt()))

    def visitExpression(self, ctx: HLangParser.ExpressionContext):
        return self.visit(ctx.pipe_expr())
    
    def visitExpression_opt(self, ctx: HLangParser.Expression_optContext):
        return None if ctx is None or ctx.expression() is None else self.visit(ctx.expression())

    def visitOr_expr(self, ctx: HLangParser.Or_exprContext):
        parts = ctx.and_expr()
        node = self.visit(parts[0])
        for and_ctx in parts[1:]:
            node = BinaryOp(node, "||", self.visit(and_ctx))
        return node

    def visitAnd_expr(self, ctx: HLangParser.And_exprContext):
        parts = ctx.equality_expr()
        node = self.visit(parts[0])
        for eq_ctx in parts[1:]:
            node = BinaryOp(node, "&&", self.visit(eq_ctx))
        return node

    def visitEquality_expr(self, ctx: HLangParser.Equality_exprContext):
        node = self.visit(ctx.relational_expr(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText() 
            right = self.visit(ctx.relational_expr((i+1)//2))
            node = BinaryOp(node, op, right)
        return node

    def visitRelational_expr(self, ctx: HLangParser.Relational_exprContext):
        node = self.visit(ctx.additive_expr(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.additive_expr((i+1)//2))
            node = BinaryOp(node, op, right)
        return node

    def visitAdditive_expr(self, ctx: HLangParser.Additive_exprContext):
        node = self.visit(ctx.multiplicative_expr(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText() 
            right = self.visit(ctx.multiplicative_expr((i+1)//2))
            node = BinaryOp(node, op, right)
        return node

    def visitMultiplicative_expr(self, ctx: HLangParser.Multiplicative_exprContext):
        node = self.visit(ctx.unary_expr(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.unary_expr((i+1)//2))
            node = BinaryOp(node, op, right)
        return node


    def visitUnary_expr(self, ctx: HLangParser.Unary_exprContext):
        if ctx.NOT() or ctx.MINUS() or ctx.PLUS():
            op = "!" if ctx.NOT() else "-" if ctx.MINUS() else "+"
            return UnaryOp(op, self.visit(ctx.unary_expr()))
        return self.visit(ctx.postfix_expr())

    def visitPipe_expr(self, ctx: HLangParser.Pipe_exprContext):
        parts = ctx.or_expr()
        left = self.visit(parts[0])
        for or_ctx in parts[1:]:
            right = self.visit(or_ctx)
            left = BinaryOp(left, ">>", right)
        return left

    def visitPostfix_expr(self, ctx: HLangParser.Postfix_exprContext):
        node = self.visit(ctx.primary_expr()) if ctx.primary_expr() else None
        for expr_ctx in ctx.expression():
            node = ArrayAccess(node, self.visit(expr_ctx))
        if ctx.func_call():
            node = self.visit(ctx.func_call())
        return node

    def visitPrimary_expr(self, ctx: HLangParser.Primary_exprContext):
        if ctx.INTEGER_LITERAL(): 
            return IntegerLiteral(int(ctx.getText()))
        elif ctx.FLOAT_LITERAL():   
            return FloatLiteral(ctx.getText())
        elif ctx.STRING_LITERAL(): 
            return StringLiteral(ctx.getText()) 
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.ID():            
            return Identifier(ctx.getText())
        elif ctx.LEFT_PAREN():      
            return self.visit(ctx.expression())
        elif ctx.array_literal():                   
            return self.visit(ctx.array_literal())

    def visitFunc_call(self, ctx: HLangParser.Func_callContext):
        return FunctionCall(Identifier(ctx.ID().getText()) if ctx.ID() else Identifier(ctx.primitive_type().getText()),
                            self.visit(ctx.expr_list_opt()))

    def visitArray_literal(self, ctx: HLangParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.expr_list_opt()))

    def visitLvalue(self, ctx: HLangParser.LvalueContext):
        if ctx.ID():
            return IdLValue(ctx.ID().getText())
        base = self.visit(ctx.primary_expr())
        idxs = [self.visit(expr) for expr in ctx.expression()]
        arr = base
        for i in idxs[:-1]:
            arr = ArrayAccess(arr, i)
        return ArrayAccessLValue(arr, idxs[-1]) if idxs else base
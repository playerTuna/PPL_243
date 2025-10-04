grammar HLang;

options {
	language = Python3;
}

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    token = super().emit()
    if tk == HLangLexer.UNCLOSE_STRING:
        raise UncloseString(token.text[1:])
    elif tk == HLangLexer.ILLEGAL_ESCAPE:
        raise IllegalEscape(token.text[1:-1])
    elif tk == HLangLexer.ILLEGAL_CHAR_IN_STRING:
        content = token.text[1:-1]
        bad = next(ch for ch in content if ord(ch) < 32 or ord(ch) >= 127)
        raise ErrorToken(bad)
    elif tk == HLangLexer.ERROR_CHAR:
        raise ErrorToken(token.text)
    return token
}

// ───────────── Parser rules ─────────────

program
    : decl_list EOF
    ;

decl_list
    : decl decl_list
    |     // empty
    ;

decl
    : const_decl
    | func_decl SEMICOLON?
    ;


// constants / variables
const_decl: CONST ID type_opt ASSIGN expression SEMICOLON;
const_decl_opt:
	const_decl
	| ; // empty
var_decl_stmt: LET ID type_opt ASSIGN expression SEMICOLON;
type_opt:
	COLON type_spec
	| ; // empty

// functions
func_decl_opt:
	func_decl
	| ; // empty
func_decl:
	FUNC ID LEFT_PAREN param_list_opt RIGHT_PAREN ARROW type_spec block_stmt;

param_list_opt:
	param_list
	| ; // empty

param_list: param param_list_tail;
param_list_tail:
	COMMA param param_list_tail
	| ; // end

param: ID COLON type_spec;

// types
type_spec: primitive_type | array_type;

primitive_type: INT | FLOAT | BOOL | STRING | VOID;
array_type:
	LEFT_BRACKET type_spec SEMICOLON INTEGER_LITERAL RIGHT_BRACKET;

// block & statements
block_stmt: LEFT_BRACE stmt_list_opt RIGHT_BRACE;
stmt_list_opt:
	stmt_list
	| ; // empty
stmt_list: stmt stmt_list_tail;
stmt_list_tail:
	stmt stmt_list_tail
	| ; // end

stmt:
	var_decl_stmt
	| assign_stmt
	| if_stmt
	| while_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| expr_stmt
	| block_stmt
;

// control flow
if_stmt:
	IF LEFT_PAREN expression RIGHT_PAREN block_stmt else_if_list else_clause_opt;

else_if_list:
	else_if_clause else_if_list
	| ; // empty

else_if_clause:
	ELSE IF LEFT_PAREN expression RIGHT_PAREN block_stmt;
else_clause_opt:
	ELSE block_stmt
	| ; // none

while_stmt: WHILE LEFT_PAREN expression RIGHT_PAREN block_stmt;
for_stmt:
	FOR LEFT_PAREN ID IN expression RIGHT_PAREN block_stmt;

break_stmt: BREAK SEMICOLON;
continue_stmt: CONTINUE SEMICOLON;
return_stmt: RETURN expression_opt SEMICOLON;
expression_opt:
	expression
	| ; // empty

// assignment & expression statement
assign_stmt: lvalue ASSIGN expression SEMICOLON;
expr_stmt: expression SEMICOLON;

// expression precedence
expression
    : pipe_expr
    ;

pipe_expr
    : or_expr (PIPE or_expr)*
    ;

or_expr
    : and_expr (OR and_expr)*
    ;

and_expr
    : equality_expr (AND equality_expr)*
    ;

equality_expr
    : relational_expr ((EQUAL | NOT_EQUAL) relational_expr)*
    ;

relational_expr
    : additive_expr ((LESS | LESS_EQUAL | GREATER | GREATER_EQUAL) additive_expr)*
    ;

additive_expr
    : multiplicative_expr ((PLUS | MINUS) multiplicative_expr)*
    ;

multiplicative_expr
    : unary_expr ((MUL | DIV | MOD) unary_expr)*
    ;

unary_expr
    : (NOT | PLUS | MINUS) unary_expr
    | postfix_expr
    ;

postfix_expr
    : primary_expr (LEFT_BRACKET expression RIGHT_BRACKET)* | // array access
      func_call (LEFT_BRACKET expression RIGHT_BRACKET)* // function call with array access
    ;

primary_expr
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | TRUE
    | FALSE
    | ID
    | LEFT_PAREN expression RIGHT_PAREN
    | array_literal
    ;

// calls & array literals
func_call: (ID | primitive_type) LEFT_PAREN expr_list_opt RIGHT_PAREN;
expr_list_opt:
	expr_list
	| ; // empty
expr_list: expression expr_list_tail;
expr_list_tail:
	COMMA expression expr_list_tail
	| ; // end

array_literal: LEFT_BRACKET expr_list_opt RIGHT_BRACKET;

// l-values
lvalue
    : ID
    | primary_expr '[' expression ']' ( '[' expression ']' )*   // only array access on primary (for lvalues)
    ;

// ───────────────────── Lexer rules ─────────────────────
WS: [ \t\r]+ -> skip;
NEWLINE: [\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

BOOL: 'bool';
BREAK: 'break';
CONST: 'const';
CONTINUE: 'continue';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNC: 'func';
IF: 'if';
IN: 'in';
INT: 'int';
LET: 'let';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
VOID: 'void';
WHILE: 'while';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
COLON: ':';
ARROW: '->';
PIPE: '>>';

LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
COMMA: ',';
SEMICOLON: ';';
DOT: '.';

INTEGER_LITERAL: [0-9]+;

fragment INT_PART: [0-9]+;
fragment DECIMAL: '.' [0-9]*;
fragment EXPONENT: [eE][+-]? [0-9]+;


FLOAT_LITERAL: INT_PART DECIMAL EXPONENT? | INT_PART '.' EXPONENT;

fragment ESC_SEQ: '\\' [ntr"\\];
fragment ASCII_SYMBOL:
	[\u0020-\u0021\u0023-\u005B\u005D-\u007E];
fragment BAD_ESCAPE: '\\' ~[ntr"\\];
fragment CONTROL_CHAR: [\u0000-\u001F\u007F];
fragment UNICODE_CHAR: [\u0080-\uFFFF];
fragment STRING_CHAR: ASCII_SYMBOL | ESC_SEQ;

STRING_LITERAL:
	'"' (ESC_SEQ | ASCII_SYMBOL)* '"' { self.text = self.text[1:-1] };

ILLEGAL_ESCAPE:
	'"' (ESC_SEQ | ASCII_SYMBOL)* BAD_ESCAPE { raise IllegalEscape(self.text[1:self.text.rfind('\\') + 2]) 
		};

ILLEGAL_CHAR_IN_STRING:
	'"' (ESC_SEQ | ASCII_SYMBOL | BAD_ESCAPE)* (
		CONTROL_CHAR
		| UNICODE_CHAR
	) .*? '"';

UNCLOSE_STRING: '"' ~["\r\n]* EOF;

ID: [a-zA-Z_][a-zA-Z0-9_]*;

ERROR_CHAR: . { raise ErrorToken(self.text) };
from math import exp
from utils import ASTGenerator


# def test_001():
#     """Test basic constant declaration AST generation"""
#     source = "const x: int = 42;"
#     expected = "Program(consts=[ConstDecl(x, int, IntegerLiteral(42))])"
#     # Just check that it doesn't return an error
#     assert str(ASTGenerator(source).generate()) == expected


# def test_002():
#     """Test function declaration AST generation"""
#     source = "func main() -> void {}"
#     expected = "Program(funcs=[FuncDecl(main, [], void, [])])"
#     assert str(ASTGenerator(source).generate()) == expected


# def test_003():
#     """Test function with parameters AST generation"""
#     source = "func add(a: int, b: int) -> int { return a + b; }"
#     expected = "Program(funcs=[FuncDecl(add, [Param(a, int), Param(b, int)], int, [ReturnStmt(BinaryOp(Identifier(a), +, Identifier(b)))])])"
#     assert str(ASTGenerator(source).generate()) == expected


# def test_004():
#     """Test multiple declarations AST generation"""
#     source = """const PI: float = 3.14;
#     func square(x: int) -> int { return x * x; }"""
#     expected = "Program(consts=[ConstDecl(PI, float, FloatLiteral(3.14))], funcs=[FuncDecl(square, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), *, Identifier(x)))])])"
#     assert str(ASTGenerator(source).generate()) == expected


# def test_005():
#     """Test variable declaration with type inference"""
#     source = """func main() -> void { let name = "Alice"; }"""
#     expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(name, StringLiteral('Alice'))])])"
#     assert str(ASTGenerator(source).generate()) == expected


# def test_006():
#     """Test if-else statement AST generation"""
#     source = """func main() -> void { 
#         if (x > 0) { 
#             return x;
#         } else { 
#             return 0;
#         }
#     }"""
#     expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(0))]))])])"
#     assert str(ASTGenerator(source).generate()) == expected


# def test_007():
#     """Test while loop AST generation"""
#     source = """func main() -> void { 
#         while (i < 10) { 
#             i = i + 1; 
#         }
#     }"""
#     expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(10)), BlockStmt([Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
#     assert str(ASTGenerator(source).generate()) == expected


# def test_008():
#     """Test array operations AST generation"""
#     source = """func main() -> void { 
#         let arr = [1, 2, 3];
#         let first = arr[0];
#     }"""
#     expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(first, ArrayAccess(Identifier(arr), IntegerLiteral(0)))])])"
#     assert str(ASTGenerator(source).generate()) == expected


# def test_009():
#     """Test pipeline operator AST generation"""
#     source = """func main() -> void { 
#         let result = data >> process;
#     }"""
#     expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(Identifier(data), >>, Identifier(process)))])])"
#     assert str(ASTGenerator(source).generate()) == expected


# 1. Constant Declarations (10 test cases)
def test_001():
    """Test basic integer constant declaration"""
    source = "const x: int = 42;"
    expected = "Program(consts=[ConstDecl(x, int, IntegerLiteral(42))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_002():
    """Test float constant declaration with type inference"""
    source = "const PI = 3.14;"
    expected = "Program(consts=[ConstDecl(PI, FloatLiteral(3.14))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_003():
    """Test boolean constant declaration"""
    source = "const FLAG: bool = true;"
    expected = "Program(consts=[ConstDecl(FLAG, bool, BooleanLiteral(True))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_004():
    """Test string constant declaration"""
    source = "const NAME: string = \"Alice\";"
    expected = "Program(consts=[ConstDecl(NAME, string, StringLiteral('Alice'))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_005():
    """Test array constant declaration"""
    source = "const NUMS: [int; 3] = [1, 2, 3];"
    expected = "Program(consts=[ConstDecl(NUMS, [int; 3], ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_006():
    """Test empty array constant declaration"""
    source = "const EMPTY: [int; 0] = [];"
    expected = "Program(consts=[ConstDecl(EMPTY, [int; 0], ArrayLiteral([]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_007():
    """Test negative integer constant"""
    source = "const NEGGA: int = -10;"
    expected = "Program(consts=[ConstDecl(NEGGA, int, UnaryOp(-, IntegerLiteral(10)))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_008():
    """Test float constant with exponent"""
    source = "const EXP: float = 1.23e2;"
    expected = "Program(consts=[ConstDecl(EXP, float, FloatLiteral(1.23e2))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_009():
    """Test multiple constant declarations"""
    source = "const A = 1; const B: int = 2;"
    expected = "Program(consts=[ConstDecl(A, IntegerLiteral(1)), ConstDecl(B, int, IntegerLiteral(2))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_010():
    """Test string constant with escape sequence"""
    source = "const MSG: string = \"Hello World\\n\";"
    expected = "Program(consts=[ConstDecl(MSG, string, StringLiteral('Hello World\\\\n'))])"
    assert str(ASTGenerator(source).generate()) == expected

# 2. Function Declarations (15 test cases)
def test_011():
    """Test function with no parameters and void return"""
    source = "func main() -> void {}"
    expected = "Program(funcs=[FuncDecl(main, [], void, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_012():
    """Test function with single parameter"""
    source = "func square(x: int) -> int { return x * x; }"
    expected = "Program(funcs=[FuncDecl(square, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), *, Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_013():
    """Test function with multiple parameters"""
    source = "func add(a: int, b: int) -> int { return a + b; }"
    expected = "Program(funcs=[FuncDecl(add, [Param(a, int), Param(b, int)], int, [ReturnStmt(BinaryOp(Identifier(a), +, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_014():
    """Test function with array parameter"""
    source = "func sum(arr: [int; 3]) -> int { return arr[0] + arr[1] + arr[2]; }"
    expected = "Program(funcs=[FuncDecl(sum, [Param(arr, [int; 3])], int, [ReturnStmt(BinaryOp(BinaryOp(ArrayAccess(Identifier(arr), IntegerLiteral(0)), +, ArrayAccess(Identifier(arr), IntegerLiteral(1))), +, ArrayAccess(Identifier(arr), IntegerLiteral(2))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_015():
    """Test function with float return"""
    source = "func pi() -> float { return 3.14; }"
    expected = "Program(funcs=[FuncDecl(pi, [], float, [ReturnStmt(FloatLiteral(3.14))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_016():
    """Test function with boolean return"""
    source = "func isZero(x: int) -> bool { return x == 0; }"
    expected = "Program(funcs=[FuncDecl(isZero, [Param(x, int)], bool, [ReturnStmt(BinaryOp(Identifier(x), ==, IntegerLiteral(0)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_017():
    """Test function with string parameter"""
    source = "func greet(name: string) -> void { print(name); }"
    expected = "Program(funcs=[FuncDecl(greet, [Param(name, string)], void, [ExprStmt(FunctionCall(Identifier(print), [Identifier(name)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_018():
    """Test function with if-else statements"""
    source = """func check(x: int) -> int {
        if (x < 0) { 
            return -1;
        } else if (x == 0) { 
            return 0; 
        } else { 
            return 2 * x;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(check, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), <, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(UnaryOp(-, IntegerLiteral(1)))]), elif_branches=[(BinaryOp(Identifier(x), ==, IntegerLiteral(0)), BlockStmt([ReturnStmt(IntegerLiteral(0))]))], else_stmt=BlockStmt([ReturnStmt(BinaryOp(IntegerLiteral(2), *, Identifier(x)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_019():
    """Test recursive function"""
    source = "func factorial(n: int) -> int { if (n <= 1) { return 1; } return n * factorial(n - 1); }"
    expected = "Program(funcs=[FuncDecl(factorial, [Param(n, int)], int, [IfStmt(condition=BinaryOp(Identifier(n), <=, IntegerLiteral(1)), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1))])), ReturnStmt(BinaryOp(Identifier(n), *, FunctionCall(Identifier(factorial), [BinaryOp(Identifier(n), -, IntegerLiteral(1))])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_020():
    """Test function with no return statement (void)"""
    source = "func nop() -> void { let x = 1; }"
    expected = "Program(funcs=[FuncDecl(nop, [], void, [VarDecl(x, IntegerLiteral(1))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_021():
    """Test function with multiple statements"""
    source = "func compute(x: int) -> int { let y = x * 2; return y + 1; }"
    expected = "Program(funcs=[FuncDecl(compute, [Param(x, int)], int, [VarDecl(y, BinaryOp(Identifier(x), *, IntegerLiteral(2))), ReturnStmt(BinaryOp(Identifier(y), +, IntegerLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_022():
    """Test function with array return"""
    source = "func getArray() -> [int; 2] { return [1, 2]; }"
    expected = "Program(funcs=[FuncDecl(getArray, [], [int; 2], [ReturnStmt(ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_023():
    """Test function with mixed parameter types"""
    source = "func mix(a: int, b: float) -> float { return cast_Float(a) + b; }"
    expected = "Program(funcs=[FuncDecl(mix, [Param(a, int), Param(b, float)], float, [ReturnStmt(BinaryOp(FunctionCall(Identifier(cast_Float), [Identifier(a)]), +, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_024():
    """Test function with nested block"""
    source = "func nested(x: int) -> int { { let y = x; return y; } }"
    expected = "Program(funcs=[FuncDecl(nested, [Param(x, int)], int, [BlockStmt([VarDecl(y, Identifier(x)), ReturnStmt(Identifier(y))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_025():
    """Test function with multiple return paths"""
    source = "func max(a: int, b: int) -> int { if (a > b) { return a; } return b; }"
    expected = "Program(funcs=[FuncDecl(max, [Param(a, int), Param(b, int)], int, [IfStmt(condition=BinaryOp(Identifier(a), >, Identifier(b)), then_stmt=BlockStmt([ReturnStmt(Identifier(a))])), ReturnStmt(Identifier(b))])])"
    assert str(ASTGenerator(source).generate()) == expected

# 3. Variable Declarations (10 test cases)
def test_026():
    """Test variable declaration with type inference"""
    source = "func main() -> void { let x = 42; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(42))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_027():
    """Test variable declaration with explicit type"""
    source = "func main() -> void { let x: int = 100; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, int, IntegerLiteral(100))])])"
    assert str (ASTGenerator(source).generate()) == expected

def test_028():
    """Test array variable declaration"""
    source = "func main() -> void { let arr = [1, 2, 3]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_029():
    """Test string variable declaration"""
    source = "func main() -> void { let s = \"test\"; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(s, StringLiteral('test'))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_030():
    """Test boolean variable declaration"""
    source = "func main() -> void { let b = true; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BooleanLiteral(True))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_031():
    """Test float variable declaration"""
    source = "func main() -> void { let f = 2.5; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(f, FloatLiteral(2.5))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_032():
    """Test variable shadowing in block"""
    source = "func main() -> void { let x = 1; { let x = 2; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(1)), BlockStmt([VarDecl(x, IntegerLiteral(2))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_033():
    """Test multiple variable declarations"""
    source = "func main() -> void { let x = 1; let y = 2; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(1)), VarDecl(y, IntegerLiteral(2))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_034():
    """Test array variable with explicit type"""
    source = "func main() -> void { let arr: [int; 2] = [1, 2]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, [int; 2], ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_035():
    """Test variable declaration with expression"""
    source = "func main() -> void { let x = 1 + 2; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

# 4. Arithmetic and Comparison Expressions (15 test cases)
def test_036():
    """Test addition expression"""
    source = "func main() -> void { let x = 1 + 2; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_037():
    """Test subtraction expression"""
    source = "func main() -> void { let x = 5 - 3; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(5), -, IntegerLiteral(3)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_038():
    """Test multiplication expression"""
    source = "func main() -> void { let x = 4 * 2; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(4), *, IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_039():
    """Test division expression"""
    source = "func main() -> void { let x = 10 / 2; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(10), /, IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_040():
    """Test modulo expression"""
    source = "func main() -> void { let x = 10 % 3; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(10), %, IntegerLiteral(3)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_041():
    """Test unary minus expression"""
    source = "func main() -> void { let x = -5; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, UnaryOp(-, IntegerLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_042():
    """Test equality comparison"""
    source = "func main() -> void { let b = 5 == 5; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(IntegerLiteral(5), ==, IntegerLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_043():
    """Test inequality comparison"""
    source = "func main() -> void { let b = 5 != 3; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(IntegerLiteral(5), !=, IntegerLiteral(3)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_044():
    """Test less than comparison"""
    source = "func main() -> void { let b = 3 < 5; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(IntegerLiteral(3), <, IntegerLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_045():
    """Test greater than or equal comparison"""
    source = "func main() -> void { let b = 5 >= 5; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(IntegerLiteral(5), >=, IntegerLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_046():
    """Test string concatenation"""
    source = "func main() -> void { let s = \"a\" + \"b\"; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(s, BinaryOp(StringLiteral('a'), +, StringLiteral('b')))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_047():
    """Test complex arithmetic expression"""
    source = "func main() -> void { let x = (1 + 2) * 3; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)), *, IntegerLiteral(3)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_048():
    """Test mixed int and float arithmetic"""
    source = "func main() -> void { let x = 2 + 3.5; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(2), +, FloatLiteral(3.5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_049():
    """Test string comparison"""
    source = "func main() -> void { let b = \"abc\" < \"def\"; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(StringLiteral('abc'), <, StringLiteral('def')))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_050():
    """Test arithmetic with variables"""
    source = "func main() -> void { let x = 5; let y = x * 2; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(5)), VarDecl(y, BinaryOp(Identifier(x), *, IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

# 5. Logical Expressions (10 test cases)
def test_051():
    """Test logical AND expression"""
    source = "func main() -> void { let b = true && false; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BooleanLiteral(True), &&, BooleanLiteral(False)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_052():
    """Test logical OR expression"""
    source = "func main() -> void { let b = true || false; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BooleanLiteral(True), ||, BooleanLiteral(False)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_053():
    """Test logical NOT expression"""
    source = "func main() -> void { let b = !true; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, UnaryOp(!, BooleanLiteral(True)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_054():
    """Test complex logical expression"""
    source = "func main() -> void { let b = (x > 0) && (y < 10); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, BinaryOp(Identifier(y), <, IntegerLiteral(10))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_055():
    """Test nested logical expression"""
    source = "func main() -> void { let b = !(true || false); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, UnaryOp(!, BinaryOp(BooleanLiteral(True), ||, BooleanLiteral(False))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_056():
    """Test logical with comparison"""
    source = "func main() -> void { let b = (x == 0) || (y != 0); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BinaryOp(Identifier(x), ==, IntegerLiteral(0)), ||, BinaryOp(Identifier(y), !=, IntegerLiteral(0))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_057():
    """Test logical AND with variables"""
    source = "func main() -> void { let a = true; let b = a && false; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(a, BooleanLiteral(True)), VarDecl(b, BinaryOp(Identifier(a), &&, BooleanLiteral(False)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_058():
    """Test short-circuit AND"""
    source = "func main() -> void { let b = (x > 0) && isValid(x); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, FunctionCall(Identifier(isValid), [Identifier(x)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_059():
    """Test short-circuit OR"""
    source = "func main() -> void { let b = (x == 0) || isValid(x); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BinaryOp(Identifier(x), ==, IntegerLiteral(0)), ||, FunctionCall(Identifier(isValid), [Identifier(x)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_060():
    """Test logical expression with function call"""
    source = "func main() -> void { let b = !isValid(x); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, UnaryOp(!, FunctionCall(Identifier(isValid), [Identifier(x)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

# 6. Array Operations (10 test cases)
def test_061():
    """Test array access"""
    source = "func main() -> void { let arr = [1, 2, 3]; let x = arr[0]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(x, ArrayAccess(Identifier(arr), IntegerLiteral(0)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_062():
    """Test array assignment"""
    source = "func main() -> void { let arr = [1, 2, 3]; arr[1] = 5; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), Assignment(ArrayAccessLValue(Identifier(arr), IntegerLiteral(1)), IntegerLiteral(5))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_063():
    """Test multi-dimensional array declaration"""
    source = "func main() -> void { let matrix = [[1, 2], [3, 4]]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(matrix, ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_064():
    """Test multi-dimensional array access"""
    source = "func main() -> void { let matrix = [[1, 2], [3, 4]]; let x = matrix[0][1]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(matrix, ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])])), VarDecl(x, ArrayAccess(ArrayAccess(Identifier(matrix), IntegerLiteral(0)), IntegerLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_065():
    """Test array with type annotation"""
    source = "func main() -> void { let arr: [int; 3] = [1, 2, 3]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, [int; 3], ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_066():
    """Test empty array declaration"""
    source = "func main() -> void { let arr: [int; 0] = []; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, [int; 0], ArrayLiteral([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_067():
    """Test array with expressions"""
    source = "func main() -> void { let arr = [x + 1, x * 2]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([BinaryOp(Identifier(x), +, IntegerLiteral(1)), BinaryOp(Identifier(x), *, IntegerLiteral(2))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_068():
    """Test array length function"""
    source = "func main() -> void { let arr = [1, 2, 3]; let len = len(arr); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(len, FunctionCall(Identifier(len), [Identifier(arr)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_069():
    """Test array with string elements"""
    source = "func main() -> void { let arr = [\"a\", \"b\"]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([StringLiteral('a'), StringLiteral('b')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_070():
    """Test array with boolean elements"""
    source = "func main() -> void { let arr = [true, false]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

# 7. Conditional Statements (10 test cases)
def test_071():
    """Test simple if statement"""
    source = "func main() -> void { if (x > 0) { print(\"positive\"); } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(print), [StringLiteral('positive')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_072():
    """Test if-else statement"""
    source = "func main() -> void { if (x > 0) { x = 1; } else { x = 0; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]), else_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(0))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_073():
    """Test if-else-if statement"""
    source = "func main() -> void { if (x > 0) { x = 1; } else if (x < 0) { x = -1; } else { x = 0; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]), elif_branches=[(BinaryOp(Identifier(x), <, IntegerLiteral(0)), BlockStmt([Assignment(IdLValue(x), UnaryOp(-, IntegerLiteral(1)))]))], else_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(0))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_074():
    """Test nested if statement"""
    source = "func main() -> void { if (x > 0) { if (y > 0) { x = 1; } } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([IfStmt(condition=BinaryOp(Identifier(y), >, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_075():
    """Test if with complex condition"""
    source = "func main() -> void { if (x > 0 && y < 10) { x = 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, BinaryOp(Identifier(y), <, IntegerLiteral(10))), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_076():
    """Test if with function call condition"""
    source = "func main() -> void { if (isValid(x)) { x = 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=FunctionCall(Identifier(isValid), [Identifier(x)]), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_077():
    """Test else-if chain"""
    source = "func main() -> void { if (x == 1) { x = 10; } else if (x == 2) { x = 20; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), ==, IntegerLiteral(1)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(10))]), elif_branches=[(BinaryOp(Identifier(x), ==, IntegerLiteral(2)), BlockStmt([Assignment(IdLValue(x), IntegerLiteral(20))]))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_078():
    """Test if with block statement"""
    source = "func main() -> void { if (x > 0) { { let y = 1; } } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([BlockStmt([VarDecl(y, IntegerLiteral(1))])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_079():
    """Test if with return statement"""
    source = "func main() -> int { if (x > 0) { return 1; } return 0; }"
    expected = "Program(funcs=[FuncDecl(main, [], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1))])), ReturnStmt(IntegerLiteral(0))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_080():
    """Test if with multiple statements"""
    source = "func main() -> void { if (x > 0) { x = 1; y = 2; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1)), Assignment(IdLValue(y), IntegerLiteral(2))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

# 8. Loop Statements (10 test cases)
def test_081():
    """Test while loop with assignment"""
    source = "func main() -> void { let i = 0; while (i < 5) { i = i + 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(i, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(5)), BlockStmt([Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_082():
    """Test for loop over array"""
    source = "func main() -> void { let arr = [1, 2, 3]; for (x in arr) { print(str(x)); } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), ForStmt(x, Identifier(arr), BlockStmt([ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(x)])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_083():
    """Test while loop with break"""
    source = "func main() -> void { let i = 0; while (i < 10) { if (i == 5) { break; } i = i + 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(i, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(10)), BlockStmt([IfStmt(condition=BinaryOp(Identifier(i), ==, IntegerLiteral(5)), then_stmt=BlockStmt([BreakStmt()])), Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_084():
    """Test for loop with continue"""
    source = "func main() -> void { for (x in [1, 2, 3]) { if (x == 2) { continue; } print(str(x)); } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(x, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), BlockStmt([IfStmt(condition=BinaryOp(Identifier(x), ==, IntegerLiteral(2)), then_stmt=BlockStmt([ContinueStmt()])), ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(x)])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_085():
    """Test nested while loop"""
    source = "func main() -> void { let i = 0; while (i < 3) { let j = 0; while (j < 2) { j = j + 1; } i = i + 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(i, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(3)), BlockStmt([VarDecl(j, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(j), <, IntegerLiteral(2)), BlockStmt([Assignment(IdLValue(j), BinaryOp(Identifier(j), +, IntegerLiteral(1)))])), Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_086():
    """Test for loop with array modification"""
    source = "func main() -> void { let arr = [1, 2, 3]; for (x in arr) { arr[0] = x; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), ForStmt(x, Identifier(arr), BlockStmt([Assignment(ArrayAccessLValue(Identifier(arr), IntegerLiteral(0)), Identifier(x))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_087():
    """Test while loop with complex condition"""
    source = "func main() -> void { let i = 0; while (i < 5 && isValid(i)) { i = i + 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(i, IntegerLiteral(0)), WhileStmt(BinaryOp(BinaryOp(Identifier(i), <, IntegerLiteral(5)), &&, FunctionCall(Identifier(isValid), [Identifier(i)])), BlockStmt([Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_088():
    """Test for loop with empty body"""
    source = "func main() -> void { for (x in [1, 2, 3]) {} }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(x, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_089():
    """Test while loop with return"""
    source = "func main() -> int { let i = 0; while (i < 5) { return i; } return 0; }"
    expected = "Program(funcs=[FuncDecl(main, [], int, [VarDecl(i, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(5)), BlockStmt([ReturnStmt(Identifier(i))])), ReturnStmt(IntegerLiteral(0))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_090():
    """Test for loop with nested if"""
    source = "func main() -> void { for (x in [1, 2, 3]) { if (x > 1) { print(str(x)); } } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(x, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), BlockStmt([IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(1)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(x)])]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

# 9. Pipeline Operator (10 test cases)
def test_091():
    """Test simple pipeline operator"""
    source = "func main() -> void { let x = 5 >> add(3); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(5), >>, FunctionCall(Identifier(add), [IntegerLiteral(3)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_092():
    """Test chained pipeline operator"""
    source = "func main() -> void { let x = 5 >> add(3) >> multiply(2); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(BinaryOp(IntegerLiteral(5), >>, FunctionCall(Identifier(add), [IntegerLiteral(3)])), >>, FunctionCall(Identifier(multiply), [IntegerLiteral(2)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_093():
    """Test pipeline with string processing"""
    source = "func main() -> void { let s = \"hello\" >> uppercase(s); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(s, BinaryOp(StringLiteral('hello'), >>, FunctionCall(Identifier(uppercase), [Identifier(s)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_094():
    """Test pipeline with array processing"""
    source = "func main() -> void { let arr = [1, 2, 3] >> map(square); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, BinaryOp(ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), >>, FunctionCall(Identifier(map), [Identifier(square)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_095():
    """Test pipeline with multiple arguments"""
    source = "func main() -> void { let s = \"hello\" >> format(\"[\", \"]\"); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(s, BinaryOp(StringLiteral('hello'), >>, FunctionCall(Identifier(format), [StringLiteral('['), StringLiteral(']')])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_096():
    """Test pipeline with complex expression"""
    source = "func main() -> void { let x = (1 + 2) >> add(3); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)), >>, FunctionCall(Identifier(add), [IntegerLiteral(3)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_097():
    """Test pipeline with type conversion"""
    source = "func main() -> void { let s = 42 >> str(s); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(s, BinaryOp(IntegerLiteral(42), >>, FunctionCall(Identifier(str), [Identifier(s)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_098():
    """Test pipeline with nested function calls"""
    source = "func main() -> void { let x = 5 >> add(3 >> multiply(2)); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(IntegerLiteral(5), >>, FunctionCall(Identifier(add), [BinaryOp(IntegerLiteral(3), >>, FunctionCall(Identifier(multiply), [IntegerLiteral(2)]))])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_099():
    """Test pipeline with array length"""
    source = "func main() -> void { let arr = [1, 2, 3] >> getLen(arr); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, BinaryOp(ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), >>, FunctionCall(Identifier(getLen), [Identifier(arr)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_100():
    """Test pipeline with multiple transformations"""
    source = "func main() -> void { let result = data >> filter(isValid) >> map(transform); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(Identifier(data), >>, FunctionCall(Identifier(filter), [Identifier(isValid)])), >>, FunctionCall(Identifier(map), [Identifier(transform)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

# 10. Complex Programs (10 test cases)
def test_101():
    """Test factorial program"""
    source = """func factorial(n: int) -> int {
        if (n <= 1) { return 1; }
        return n * factorial(n - 1);
    }
    func main() -> void {
        let result = factorial(5);
        print("Result: " + str(result));
    }"""
    expected = "Program(funcs=[FuncDecl(factorial, [Param(n, int)], int, [IfStmt(condition=BinaryOp(Identifier(n), <=, IntegerLiteral(1)), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1))])), ReturnStmt(BinaryOp(Identifier(n), *, FunctionCall(Identifier(factorial), [BinaryOp(Identifier(n), -, IntegerLiteral(1))])))]), FuncDecl(main, [], void, [VarDecl(result, FunctionCall(Identifier(factorial), [IntegerLiteral(5)])), ExprStmt(FunctionCall(Identifier(print), [BinaryOp(StringLiteral('Result: '), +, FunctionCall(Identifier(str), [Identifier(result)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_102():
    """Test array sum with loop"""
    source = """func sum_array(arr: [int; 5]) -> int {
        let total = 0;
        for (x in arr) { total = total + x; }
        return total;
    }
    func main() -> void {
        let arr = [1, 2, 3, 4, 5];
        print(str(sum_array(arr)));
    }"""
    expected = "Program(funcs=[FuncDecl(sum_array, [Param(arr, [int; 5])], int, [VarDecl(total, IntegerLiteral(0)), ForStmt(x, Identifier(arr), BlockStmt([Assignment(IdLValue(total), BinaryOp(Identifier(total), +, Identifier(x)))])), ReturnStmt(Identifier(total))]), FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)])), ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [FunctionCall(Identifier(sum_array), [Identifier(arr)])])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_103():
    """Test conditional array processing"""
    source = """func count_evens(arr: [int; 3]) -> int {
        let count = 0;
        for (x in arr) { if (x % 2 == 0) { count = count + 1; } }
        return count;
    }
    func main() -> void {
        let arr = [1, 2, 4];
        print(str(count_evens(arr)));
    }"""
    expected = "Program(funcs=[FuncDecl(count_evens, [Param(arr, [int; 3])], int, [VarDecl(count, IntegerLiteral(0)), ForStmt(x, Identifier(arr), BlockStmt([IfStmt(condition=BinaryOp(BinaryOp(Identifier(x), %, IntegerLiteral(2)), ==, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(count), BinaryOp(Identifier(count), +, IntegerLiteral(1)))]))])), ReturnStmt(Identifier(count))]), FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(4)])), ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [FunctionCall(Identifier(count_evens), [Identifier(arr)])])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_104():
    """Test pipeline with conditional"""
    source = """func process(x: int) -> int { return x * 2; }
    func main() -> void {
        let x = 5;
        if (x > 0) { x = x >> process(x); }
        print(str(x));
    }"""
    expected = "Program(funcs=[FuncDecl(process, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), *, IntegerLiteral(2)))]), FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(5)), IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(x), BinaryOp(Identifier(x), >>, FunctionCall(Identifier(process), [Identifier(x)])))])), ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(x)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_105():
    """Test nested loop with conditional"""
    source = """func main() -> void {
        let matrix = [[1, 2], [3, 4]];
        for (row in matrix) {
            for (x in row) {
                if (x > 2) { print(str(x)); }
            }
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(matrix, ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])])), ForStmt(row, Identifier(matrix), BlockStmt([ForStmt(x, Identifier(row), BlockStmt([IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(2)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(x)])]))]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_106():
    """Test function with loop and return"""
    source = """func find_first_even(arr: [int; 3]) -> int {
        for (x in arr) { if (x % 2 == 0) { return x; } }
        return 0;
    }
    func main() -> void {
        let arr = [1, 2, 3];
        print(str(find_first_even(arr)));
    }"""
    expected = "Program(funcs=[FuncDecl(find_first_even, [Param(arr, [int; 3])], int, [ForStmt(x, Identifier(arr), BlockStmt([IfStmt(condition=BinaryOp(BinaryOp(Identifier(x), %, IntegerLiteral(2)), ==, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]))])), ReturnStmt(IntegerLiteral(0))]), FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [FunctionCall(Identifier(find_first_even), [Identifier(arr)])])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_107():
    """Test program with input and output"""
    source = """func main() -> void {
        let input = input();
        let num = to_int(input);
        print("You entered: " + str(num));
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(input, FunctionCall(Identifier(input), [])), VarDecl(num, FunctionCall(Identifier(to_int), [Identifier(input)])), ExprStmt(FunctionCall(Identifier(print), [BinaryOp(StringLiteral('You entered: '), +, FunctionCall(Identifier(str), [Identifier(num)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_108():
    """Test program with while and conditional"""
    source = """func main() -> void {
        let i = 0;
        while (i < 5) {
            if (i % 2 == 0) { print(str(i)); }
            i = i + 1;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(i, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(5)), BlockStmt([IfStmt(condition=BinaryOp(BinaryOp(Identifier(i), %, IntegerLiteral(2)), ==, IntegerLiteral(0)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(i)])]))])), Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_109():
    """Test program with pipeline and loop"""
    source = """func double(x: int) -> int { return x * 2; }
    func main() -> void {
        let arr = [1, 2, 3];
        let result = arr >> map(double);
        for (x in result) { print(str(x)); }
    }"""
    expected = "Program(funcs=[FuncDecl(double, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), *, IntegerLiteral(2)))]), FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(result, BinaryOp(Identifier(arr), >>, FunctionCall(Identifier(map), [Identifier(double)]))), ForStmt(x, Identifier(result), BlockStmt([ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(x)])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_110():
    """Test complex program with multiple features"""
    source = """const MAX = 10;
    func isEven(x: int) -> bool { return x % 2 == 0; }
    func main() -> void {
        let arr = [1, 2, 3, 4, 5];
        let filtered = arr >> filter(isEven);
        let count = len(filtered);
        if (count > 0) {
            print("Found " + str(count) + " even numbers");
        }
    }"""
    expected = "Program(consts=[ConstDecl(MAX, IntegerLiteral(10))], funcs=[FuncDecl(isEven, [Param(x, int)], bool, [ReturnStmt(BinaryOp(BinaryOp(Identifier(x), %, IntegerLiteral(2)), ==, IntegerLiteral(0)))]), FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)])), VarDecl(filtered, BinaryOp(Identifier(arr), >>, FunctionCall(Identifier(filter), [Identifier(isEven)]))), VarDecl(count, FunctionCall(Identifier(len), [Identifier(filtered)])), IfStmt(condition=BinaryOp(Identifier(count), >, IntegerLiteral(0)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(print), [BinaryOp(BinaryOp(StringLiteral('Found '), +, FunctionCall(Identifier(str), [Identifier(count)])), +, StringLiteral(' even numbers'))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    
def test_111():
    """Test function without parameters"""
    source = """func greet() -> void {
        print("Hello, World!");
    }
    func main() -> void {
        greet();
    }"""
    expected = "Program(funcs=[FuncDecl(greet, [], void, [ExprStmt(FunctionCall(Identifier(print), [StringLiteral('Hello, World!')]))]), FuncDecl(main, [], void, [ExprStmt(FunctionCall(Identifier(greet), []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_112():
    """Tests a constant declaration with a nested array containing mixed literal types (integers and floats) to verify type inference and nested array handling."""
    source = "const MATRIX = [[1, 2.5], [3.0, 4]];"
    expected = "Program(consts=[ConstDecl(MATRIX, ArrayLiteral([ArrayLiteral([IntegerLiteral(1), FloatLiteral(2.5)]), ArrayLiteral([FloatLiteral(3.0), IntegerLiteral(4)])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_113():
    """Tests a constant declaration with a complex arithmetic expression involving multiple operators and parentheses."""
    source = "const RESULT: float = (1 + 2) * 3.5 / 2.0;"
    expected = "Program(consts=[ConstDecl(RESULT, float, BinaryOp(BinaryOp(BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)), *, FloatLiteral(3.5)), /, FloatLiteral(2.0)))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_114():
    """Tests multiple constant declarations with string concatenation and escape sequences."""
    source = "const GREET = \"Hello\" + \" \" + \"World\"; const MSG = GREET + \"\\n!\";"
    expected = "Program(consts=[ConstDecl(GREET, BinaryOp(BinaryOp(StringLiteral('Hello'), +, StringLiteral(' ')), +, StringLiteral('World'))), ConstDecl(MSG, BinaryOp(Identifier(GREET), +, StringLiteral('\\\\n!')))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_115():
    """Tests an empty array constant with an explicit type annotation."""
    source = "const EMPTY: [[int; 0]; 2] = [[], []];"
    expected = "Program(consts=[ConstDecl(EMPTY, [[int; 0]; 2], ArrayLiteral([ArrayLiteral([]), ArrayLiteral([])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_116():
    """Tests a constant declaration with a negative float literal using scientific notation."""
    source = "const SMALL: float = 1.23e-4;"
    expected = "Program(consts=[ConstDecl(SMALL, float, FloatLiteral(1.23e-4))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_117():
    """Tests a function with a nested array parameter and complex array access."""
    source = "func matrix_sum(mat: [[int; 2]; 2]) -> int { return mat[0][0] + mat[1][1]; }"
    expected = "Program(funcs=[FuncDecl(matrix_sum, [Param(mat, [[int; 2]; 2])], int, [ReturnStmt(BinaryOp(ArrayAccess(ArrayAccess(Identifier(mat), IntegerLiteral(0)), IntegerLiteral(0)), +, ArrayAccess(ArrayAccess(Identifier(mat), IntegerLiteral(1)), IntegerLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_118():
    """Tests a recursive function using the pipeline operator within its body."""
    source = "func fib(n: int) -> int { if (n <= 1) { return n; } return n >> add(fib(n - 1)); }"
    expected = "Program(funcs=[FuncDecl(fib, [Param(n, int)], int, [IfStmt(condition=BinaryOp(Identifier(n), <=, IntegerLiteral(1)), then_stmt=BlockStmt([ReturnStmt(Identifier(n))])), ReturnStmt(BinaryOp(Identifier(n), >>, FunctionCall(Identifier(add), [FunctionCall(Identifier(fib), [BinaryOp(Identifier(n), -, IntegerLiteral(1))])])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_119():
    """Tests a function returning different types based on a condition (though HLang enforces consistent return types, this tests parser robustness)."""
    source = "func choose_type(flag: bool) -> float { if (flag) { return 1.0; } return float(2); }"
    expected = "Program(funcs=[FuncDecl(choose_type, [Param(flag, bool)], float, [IfStmt(condition=Identifier(flag), then_stmt=BlockStmt([ReturnStmt(FloatLiteral(1.0))])), ReturnStmt(FunctionCall(Identifier(float), [IntegerLiteral(2)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_120():
    """Tests a void function with an empty body."""
    source = "func nop() -> void {}"
    expected = "Program(funcs=[FuncDecl(nop, [], void, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_121():
    """Tests a function with a mix of parameter types, including arrays and strings."""
    source = "func process_data(arr: [int; 3], name: string, scale: float) -> string { return name + str(len(arr) * scale); }"
    expected = "Program(funcs=[FuncDecl(process_data, [Param(arr, [int; 3]), Param(name, string), Param(scale, float)], string, [ReturnStmt(BinaryOp(Identifier(name), +, FunctionCall(Identifier(str), [BinaryOp(FunctionCall(Identifier(len), [Identifier(arr)]), *, Identifier(scale))])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_122():
    """Tests a variable declaration initialized with a nested array access."""
    source = "func main() -> void { let matrix = [[1, 2], [3, 4]]; let x = matrix[1][0]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(matrix, ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])])), VarDecl(x, ArrayAccess(ArrayAccess(Identifier(matrix), IntegerLiteral(1)), IntegerLiteral(0)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_123():
    """Tests a variable declaration initialized with a pipeline expression."""
    source = "func main() -> void { let result = 10 >> add(5) >> multiply(2); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(IntegerLiteral(10), >>, FunctionCall(Identifier(add), [IntegerLiteral(5)])), >>, FunctionCall(Identifier(multiply), [IntegerLiteral(2)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_124():
    """Tests variable shadowing across multiple nested blocks."""
    source = "func main() -> void { let x = 1; { let x = \"str\"; { let x = true; } } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(1)), BlockStmt([VarDecl(x, StringLiteral('str')), BlockStmt([VarDecl(x, BooleanLiteral(True))])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_125():
    """Tests a variable declaration with a complex logical expression involving function calls."""
    source = "func main() -> void { let valid = (x > 0) && isValid(x) || !isEmpty(y); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(valid, BinaryOp(BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, FunctionCall(Identifier(isValid), [Identifier(x)])), ||, UnaryOp(!, FunctionCall(Identifier(isEmpty), [Identifier(y)]))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_126():
    """Tests a variable declaration with a three-dimensional array literal."""
    source = "func main() -> void { let cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(cube, ArrayLiteral([ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])]), ArrayLiteral([ArrayLiteral([IntegerLiteral(5), IntegerLiteral(6)]), ArrayLiteral([IntegerLiteral(7), IntegerLiteral(8)])])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_127():
    """Tests a complex arithmetic expression with mixed int and float types and parentheses."""
    source = "func main() -> void { let x = (1 + 2.5) * (3 - float(1)) / 2.0; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(BinaryOp(BinaryOp(IntegerLiteral(1), +, FloatLiteral(2.5)), *, BinaryOp(IntegerLiteral(3), -, FunctionCall(Identifier(float), [IntegerLiteral(1)]))), /, FloatLiteral(2.0)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_128():
    """Tests a comparison expression involving strings and a function call."""
    source = "func main() -> void { let b = \"abc\" < str(123); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(StringLiteral('abc'), <, FunctionCall(Identifier(str), [IntegerLiteral(123)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_129():
    """Tests nested arithmetic expressions with unary operators."""
    source = "func main() -> void { let x = -(1 + -2) * +3; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(UnaryOp(-, BinaryOp(IntegerLiteral(1), +, UnaryOp(-, IntegerLiteral(2)))), *, UnaryOp(+, IntegerLiteral(3))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_130():
    """Tests a comparison expression involving the len built-in function."""
    source = "func main() -> void { let arr = [1, 2, 3]; let b = len(arr) > 2; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(b, BinaryOp(FunctionCall(Identifier(len), [Identifier(arr)]), >, IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_131():
    """Tests a mixed arithmetic and logical expression with multiple operators."""
    source = "func main() -> void { let b = (x + 1 > y) && (z * 2 <= 10); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BinaryOp(BinaryOp(Identifier(x), +, IntegerLiteral(1)), >, Identifier(y)), &&, BinaryOp(BinaryOp(Identifier(z), *, IntegerLiteral(2)), <=, IntegerLiteral(10))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_132():
    """Tests a deeply nested logical expression with multiple function calls."""
    source = "func main() -> void { let b = !(isValid(x) && (y > 0 || isEmpty(z))); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, UnaryOp(!, BinaryOp(FunctionCall(Identifier(isValid), [Identifier(x)]), &&, BinaryOp(BinaryOp(Identifier(y), >, IntegerLiteral(0)), ||, FunctionCall(Identifier(isEmpty), [Identifier(z)])))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_133():
    """Tests a logical expression combined with pipeline operations."""
    source = "func main() -> void { let b = (x > 0) && (data >> isValid); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, BinaryOp(Identifier(data), >>, Identifier(isValid))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_134():
    """Tests a logical expression with type conversion functions."""
    source = "func main() -> void { let b = (int(\"42\") > 40) || !str(true) == \"false\"; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BinaryOp(FunctionCall(Identifier(int), [StringLiteral('42')]), >, IntegerLiteral(40)), ||, BinaryOp(UnaryOp(!, FunctionCall(Identifier(str), [BooleanLiteral(True)])), ==, StringLiteral('false'))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_135():
    """Tests a logical expression involving array access."""
    source = "func main() -> void { let arr = [true, false]; let b = arr[0] && !arr[1]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])), VarDecl(b, BinaryOp(ArrayAccess(Identifier(arr), IntegerLiteral(0)), &&, UnaryOp(!, ArrayAccess(Identifier(arr), IntegerLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_136():
    """Tests short-circuit evaluation with nested logical conditions."""
    source = "func main() -> void { let b = (x > 0) && (y < 10 && isValid(z)); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(b, BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, BinaryOp(BinaryOp(Identifier(y), <, IntegerLiteral(10)), &&, FunctionCall(Identifier(isValid), [Identifier(z)]))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_137():
    """Tests assignment to a multi-dimensional array element."""
    source = "func main() -> void { let matrix = [[1, 2], [3, 4]]; matrix[1][0] = 5; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(matrix, ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])])), Assignment(ArrayAccessLValue(ArrayAccess(Identifier(matrix), IntegerLiteral(1)), IntegerLiteral(0)), IntegerLiteral(5))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_138():
    """Tests an array literal with complex expressions as elements."""
    source = "func main() -> void { let arr = [x + 1, y * 2, z - 3]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([BinaryOp(Identifier(x), +, IntegerLiteral(1)), BinaryOp(Identifier(y), *, IntegerLiteral(2)), BinaryOp(Identifier(z), -, IntegerLiteral(3))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_139():
    """Tests array access with a variable index."""
    source = "func main() -> void { let arr = [1, 2, 3]; let i = 1; let x = arr[i]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(i, IntegerLiteral(1)), VarDecl(x, ArrayAccess(Identifier(arr), Identifier(i)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_140():
    """Tests a nested array processed through a pipeline."""
    source = "func main() -> void { let matrix = [[1, 2], [3, 4]] >> map(sum); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(matrix, BinaryOp(ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])]), >>, FunctionCall(Identifier(map), [Identifier(sum)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_141():
    """Tests array element assignment with a complex expression."""
    source = "func main() -> void { let arr = [1, 2, 3]; arr[1] = arr[0] + arr[2]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), Assignment(ArrayAccessLValue(Identifier(arr), IntegerLiteral(1)), BinaryOp(ArrayAccess(Identifier(arr), IntegerLiteral(0)), +, ArrayAccess(Identifier(arr), IntegerLiteral(2))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_142():
    """Tests a deeply nested if statement with multiple else if branches."""
    source = "func main() -> void { if (x > 0) { if (y < 10) { x = 1; } else if (y == 10) { x = 2; } } else if (x == 0) { x = 3; } else { x = 4; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([IfStmt(condition=BinaryOp(Identifier(y), <, IntegerLiteral(10)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]), elif_branches=[(BinaryOp(Identifier(y), ==, IntegerLiteral(10)), BlockStmt([Assignment(IdLValue(x), IntegerLiteral(2))]))])]), elif_branches=[(BinaryOp(Identifier(x), ==, IntegerLiteral(0)), BlockStmt([Assignment(IdLValue(x), IntegerLiteral(3))]))], else_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(4))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_143():
    """Tests an if statement with a pipeline expression as the condition."""
    source = "func main() -> void { if (data >> isValid) { print(\"Valid\"); } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(data), >>, Identifier(isValid)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(print), [StringLiteral('Valid')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_144():
    """Tests an if statement with a complex logical condition involving multiple operators."""
    source = "func main() -> void { if ((x > 0 || y < 5) && !isEmpty(z)) { x = 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), ||, BinaryOp(Identifier(y), <, IntegerLiteral(5))), &&, UnaryOp(!, FunctionCall(Identifier(isEmpty), [Identifier(z)]))), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_145():
    """Tests an if statement with a nested block containing a return statement."""
    source = "func main() -> int { if (x > 0) { { return 1; } } return 0; }"
    expected = "Program(funcs=[FuncDecl(main, [], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([BlockStmt([ReturnStmt(IntegerLiteral(1))])])), ReturnStmt(IntegerLiteral(0))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_146():
    """Tests an if statement with an empty else block."""
    source = "func main() -> void { if (x > 0) { x = 1; } else {} }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]), else_stmt=BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_147():
    """Tests nested for loops with a break statement in the inner loop."""
    source = "func main() -> void { for (i in [1, 2, 3]) { for (j in [4, 5, 6]) { if (j == 5) { break; } print(str(i * j)); } } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(i, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), BlockStmt([ForStmt(j, ArrayLiteral([IntegerLiteral(4), IntegerLiteral(5), IntegerLiteral(6)]), BlockStmt([IfStmt(condition=BinaryOp(Identifier(j), ==, IntegerLiteral(5)), then_stmt=BlockStmt([BreakStmt()])), ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [BinaryOp(Identifier(i), *, Identifier(j))])]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_148():
    """Tests a while loop with a nested conditional and continue statement."""
    source = "func main() -> void { let i = 0; while (i < 5) { if (i % 2 == 0) { i = i + 1; continue; } print(str(i)); i = i + 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(i, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(5)), BlockStmt([IfStmt(condition=BinaryOp(BinaryOp(Identifier(i), %, IntegerLiteral(2)), ==, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1))), ContinueStmt()])), ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(i)])])), Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_149():
    """Tests a for loop iterating over a pipeline expression."""
    source = "func main() -> void { for (x in [1, 2, 3] >> map(double)) { print(str(x)); } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(x, BinaryOp(ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), >>, FunctionCall(Identifier(map), [Identifier(double)])), BlockStmt([ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(x)])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_150():
    """Tests a while loop containing a for loop with complex conditions."""
    source = "func main() -> void { let i = 0; while (i < 3) { for (x in [1, 2, 3]) { if (x * i > 2) { print(str(x)); } } i = i + 1; } }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(i, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(3)), BlockStmt([ForStmt(x, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), BlockStmt([IfStmt(condition=BinaryOp(BinaryOp(Identifier(x), *, Identifier(i)), >, IntegerLiteral(2)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(x)])]))]))])), Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_151():
    """Tests a for loop with an early return statement in a non-void function."""
    source = "func main() -> int { for (x in [1, 2, 3]) { if (x == 2) { return x; } } return 0; }"
    expected = "Program(funcs=[FuncDecl(main, [], int, [ForStmt(x, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), BlockStmt([IfStmt(condition=BinaryOp(Identifier(x), ==, IntegerLiteral(2)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]))])), ReturnStmt(IntegerLiteral(0))])])"
    assert str(ASTGenerator(source).generate()) == expected
    
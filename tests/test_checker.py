# from utils import Checker


# def test_001():
#     """Test a valid program that should pass all checks"""
#     source = """
# const PI: float = 3.14;
# func main() -> void {
#     let x: int = 5;
#     let y = x + 1;
# };
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_002():
#     """Test redeclared variable error"""
#     source = """
# func main() -> void {
#     let x: int = 5;
#     let x: int = 10;
# };
# """
#     expected = "Redeclared Variable: x"
#     assert Checker(source).check_from_source() == expected


# def test_003():
#     """Test undeclared identifier error"""
#     source = """
# func main() -> void {
#     let x = y + 1;
# };
# """
#     expected = "Undeclared Identifier: y"
#     assert Checker(source).check_from_source() == expected


# def test_004():
#     """Test type mismatch error"""
#     source = """
# func main() -> void {
#     let x: int = "hello";
# };
# """
#     expected = "Type Mismatch In Statement: VarDecl(x, int, StringLiteral('hello'))"
#     assert Checker(source).check_from_source() == expected


# def test_005():
#     """Test no main function error"""
#     source = """
# func hello() -> void {
#     let x: int = 5;
# };
# """
#     expected = "No Entry Point"
#     assert Checker(source).check_from_source() == expected


# def test_006():
#     """Test break not in loop error"""
#     source = """
# func main() -> void {
#     break;
# };
# """
#     expected = "Must In Loop: BreakStmt()"
#     assert Checker(source).check_from_source() == expected


# def test_007():
#     """Type inference success: y and z inferred as int; valid arithmetic operations"""
#     source = """
# func main() -> void {
#     let x: int = 10;
#     let y = x * 2;
#     let z = y + 3;
#     let result = x + y + z;
# };
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_008():
#     """Redeclared parameter in the same prototype"""
#     source = """
# func dupParam(x: int, x: float) -> void {
# };
# func main() -> void {
#     dupParam(5, 3.14);
# };
# """
#     expected = "Redeclared Parameter: x"
#     assert Checker(source).check_from_source() == expected


# def test_009():
#     """Call to an undeclared function"""
#     source = """
# func main() -> void {
#     let x: int = unknownFunc();
# };
# """
#     expected = "Undeclared Function: unknownFunc"
#     assert Checker(source).check_from_source() == expected


# def test_010():
#     """Type mismatch in expression (int + bool)"""
#     source = """
# func main() -> void {
#     let flag: bool = true;
#     let result = 1 + flag;
# };
# """
#     expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(1), +, Identifier(flag))"
#     assert Checker(source).check_from_source() == expected


# def test_011():
#     """Assigning a float to an int variable"""
#     source = """
# func main() -> void {
#     let x: int = 5;
#     x = 3.14;
# };
# """
#     expected = "Type Mismatch In Statement: Assignment(IdLValue(x), FloatLiteral(3.14))"
#     assert Checker(source).check_from_source() == expected


# def test_012():
#     """Array size mismatch"""
#     source = """
# func main() -> void {
#     let a: [int; 2] = [1, 2];
#     let b: [int; 3] = [1, 2, 3];
#     a = b;  // This should raise an error
# };
# """
#     expected = "Type Mismatch In Statement: Assignment(IdLValue(a), Identifier(b))"
#     assert Checker(source).check_from_source() == expected


# def test_013():
#     """Incorrect number of arguments in function call"""
#     source = """
# func add(a: int, b: int) -> int { return a + b; }
# func main() -> void {
#     let x = add(1);
# };
# """
#     expected = "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(1)])"
#     assert Checker(source).check_from_source() == expected


# def test_014():
#     """'continue' outside of a loop"""
#     source = """
# func main() -> void {
#     continue;
# };
# """
#     expected = "Must In Loop: ContinueStmt()"
#     assert Checker(source).check_from_source() == expected


# def test_015():
#     """Invalid main: wrong return type"""
#     source = """
# func main() -> int {
#     return 0;
# };
# """
#     expected = "No Entry Point"
#     assert Checker(source).check_from_source() == expected


# def test_016():
#     """Valid program with nested arrays and indexing"""
#     source = """
# func main() -> void {
#     let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
#     let row = matrix[0];
#     let elem = row[1];
# };
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_017():
#     """Empty array literal without type annotation leads to TypeCannotBeInferred"""
#     source = """
# func main() -> void {
#     let a = [];
# };
# """
#     expected = "Type Cannot Be Inferred: VarDecl(a, ArrayLiteral([]))"
#     assert Checker(source).check_from_source() == expected


# def test_018():
#     """Pipeline operator with wrong input type"""
#     source = """
# func main() -> void {
#     let x: int = 5;
#     let s = "hello" >> 5;
# };
# """
#     expected = "Type Mismatch In Expression: BinaryOp(StringLiteral('hello'), >>, IntegerLiteral(5))"
#     assert Checker(source).check_from_source() == expected


# def test_019():
#     """Non-void function used as a statement is valid"""
#     source = """
# func id(x: int) -> int { return x; }

# func main() -> void {
#     id(10);
# };
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_020():
#     """Test if statement"""
#     source = """
# func test() -> string {
#     let x = 5;
#     if (x == 5) {
#         return "ok";
#     } else {
#         return "not ok";
#     }
# };
# func main() -> void {
#     test();
# };
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_021():
#     """Shadowing variable in inner block is allowed"""
#     source = """
# func main() -> void {
#     let x: int = 1;
#     {
#         let x: string = "ok";
#     };
# };
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_022():
#     """Redeclared variable in same block"""
#     source = """
# func main() -> void {
#     {
#         let y: int = 1;
#         let y: int = 2;
#     };
# };
# """
#     expected = "Redeclared Variable: y"
#     assert Checker(source).check_from_source() == expected


# def test_023():
#     """Array index with wrong type (bool index)"""
#     source = """
# func main() -> void {
#     let m: [[int; 2]; 2] = [[1,2],[3,4]];
#     let k = m[1][true];
# };
# """
#     expected = "Type Mismatch In Expression: ArrayAccess(ArrayAccess(Identifier(m), IntegerLiteral(1)), BooleanLiteral(True))"
#     assert Checker(source).check_from_source() == expected


# def test_024():
#     """Heterogeneous array literal types"""
#     source = """
# func main() -> void {
#     let bad = [1, 2.0, 3];
# };
# """
#     expected = "Type Mismatch In Expression: ArrayLiteral([IntegerLiteral(1), FloatLiteral(2.0), IntegerLiteral(3)])"
#     assert Checker(source).check_from_source() == expected


# def test_025():
#     """Assign array of different size"""
#     source = """
# func main() -> void {
#     let a: [int; 3] = [1,2,3];
#     let b: [int; 2] = [4,5];
#     a = b;
# };
# """
#     expected = "Type Mismatch In Statement: Assignment(IdLValue(a), Identifier(b))"
#     assert Checker(source).check_from_source() == expected


# def test_026():
#     """Call function with missing argument"""
#     source = """
# func add(a:int, b:int) -> int { return a+b; }

# func main() -> void {
#     let x = add(1);
# };
# """
#     expected = "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(1)])"
#     assert Checker(source).check_from_source() == expected


# def test_027():
#     """Break statement outside of any loop (inside helper function)"""
#     source = """
# func helper() -> void {
#     break;
# }

# func main() -> void {
#     helper();
# };
# """
#     expected = "Must In Loop: BreakStmt()"
#     assert Checker(source).check_from_source() == expected


# def test_028():
#     source = """
# const LIMIT: float = 1.e9 + 7;
# func test(x: int, y: string) -> string {
#     if (x < LIMIT) {
#         return "within limit";
#     } else {
#         return "out of limit";
#     }
# }

# func main() -> void {
#     test(5, "test");
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected
    
# def test_029():
#     source = """
# func test(x: int) -> void {
#     let a: int = x;
# }
# func main() -> void {
#     let a = test(5);
# }
# """
#     expected = "Type Mismatch In Expression: VarDecl(a, FunctionCall(Identifier(test), [IntegerLiteral(5)]))"
#     assert Checker(source).check_from_source() == expected


# def test_029():
#     """Void function returning a value"""
#     source = """
# func bad() -> void {
#     return 1;
# }

# func main() -> void {
#     bad();
# };
# """
#     expected = "Type Mismatch In Statement: ReturnStmt(IntegerLiteral(1))"
#     assert Checker(source).check_from_source() == expected


# def test_030():
#     """Non-void function without a return statement"""
#     source = """
# func give() -> bool {
#     // missing return
# }

# func main() -> void {
#     give();
# };
# """
#     expected = "Type Mismatch In Statement: FuncDecl(give, [], bool, [])"
#     assert Checker(source).check_from_source() == expected


# def test_031():
#     """Call to undeclared function"""
#     source = """
# func main() -> void {
#     unknown(1,2);
# };
# """
#     expected = "Undeclared Function: unknown"
#     assert Checker(source).check_from_source() == expected


# def test_032():
#     """Recursive function call"""
#     source = """
# func a() -> void {
#     a();
# }
# func main() -> void {
#     a();
# };
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_033():
#     """Forward reference in initialization"""
#     source = """
# func processValue(x: int) -> int {
#     return x * 2;
# }
# func getValue() -> int {
#     return 10;  
# }
# func forwardRef() -> void {
#     let result = processValue(undefined);
#     let undefined = getValue();
# }
# func main() -> void {
#     forwardRef();
# }
# """
#     expected = "Undeclared Identifier: undefined"
#     assert Checker(source).check_from_source() == expected


# def test_034():
#     """Test array access"""
#     source = """
# func main() -> void {
#     let arr: [int; 5] = [1, 2, 3, 4, 5];
#     arr[3] = 10; 
#     let value = arr[3];
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_035():
#     """Valid program with break/continue in loops"""
#     source = """
# const PI: float = 3.14;
# func validWhile() -> void {
#     let i = 0;
#     while (i < 10) {
#         if (i == 5) {
#             break;
#         }
#         if (i % 2 == 0) {
#             i = i + 1;
#             continue;
#         }
#         i = i + 1;
#     }
# }

# func validFor() -> void {
#     let numbers = [1, 2, 3, 4, 5];
#     for (num in numbers) {
#         if (num == 3) {
#             break;
#         }
#         if (num % 2 == 0) {
#             continue;
#         }
#     }
# }

# func nestedLoops() -> void {
#     let i = 0;
#     while (i < 5) {
#         let j = 0;
#         while (j < 5) {
#             if (i == j) {
#                 break;
#             }
#             if (j == 2) {
#                 j = j + 1;
#                 continue;
#             }
#             j = j + 1;
#         }
#         i = i + 1;
#     }
# }

# func conditionalInLoop() -> void {
#     let i = 0;
#     while (i < 10) {
#         if (i == 5) {
#             break;
#         }
#         if (i % 2 == 0) {
#             i = i + 1;
#             continue;
#         }
#         i = i + 1;
#     }
# }

# func main() -> void {
#     let a = true;
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# def test_036():
#     """Function returning wrong type"""
#     source = """
# func foo() -> int {
#     return 3.14;
# }
# func main() -> void {
#     foo();
# }
# """
#     expected = 'Type Mismatch In Statement: ReturnStmt(FloatLiteral(3.14))'
#     assert Checker(source).check_from_source() == expected


# def test_037():
#     """While condition type mismatch"""
#     source = """
# func main() -> void {
#     let x: int = 5;
#     while (x) {
#         x = x - 1;
#     }
# }
# """
#     expected = 'Type Mismatch In Statement: WhileStmt(Identifier(x), BlockStmt([Assignment(IdLValue(x), BinaryOp(Identifier(x), -, IntegerLiteral(1)))]))'
#     assert Checker(source).check_from_source() == expected


# def test_038():
#     """For loop with non-iterable type"""
#     source = """
# func main() -> void {
#     let n: int = 5;
#     for (x in n) {
#     }
# }
# """
#     expected = 'Type Mismatch In Statement: ForStmt(x, Identifier(n), BlockStmt([]))'
#     assert Checker(source).check_from_source() == expected


# def test_039():
#     """Array access with string index"""
#     source = """
# func main() -> void {
#     let a: [int; 3] = [1,2,3];
#     let x = a["1"];
# }
# """
#     expected = 'Type Mismatch In Expression: ArrayAccess(Identifier(a), StringLiteral(\'1\'))'
#     assert Checker(source).check_from_source() == expected


# def test_040():
#     """Function call with wrong number of arguments"""
#     source = """
# func echo(x: int, y: string) -> string {
#     return y;
# }
# func main() -> void {
#     echo(5);
# }
# """
#     expected = 'Type Mismatch In Expression: FunctionCall(Identifier(echo), [IntegerLiteral(5)])'
#     assert Checker(source).check_from_source() == expected


# def test_041():
#     """Function missing return statement"""
#     source = """
# func check(x: int) -> bool {
#     if (x > 0) {
#         return true;
#     } // Missing return for the false case
# }
# func main() -> void {
#     let x = check(5);
# }
# """
#     expected = "Type Mismatch In Statement: FuncDecl(check, [Param(x, int)], bool, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(BooleanLiteral(True))]))])"
#     assert Checker(source).check_from_source() == expected


# def test_042():
#     """Pipeline operator type mismatch"""
#     source = """
# func main() -> void {
#     let s = "hello";
#     let x = s >> 3;
# }
# """
#     expected = "Type Mismatch In Expression: BinaryOp(Identifier(s), >>, IntegerLiteral(3))"
#     assert Checker(source).check_from_source() == expected


# def test_043():
#     """Array access with float index"""
#     source = """
# func main() -> void {
#     let arr: [int; 3] = [1, 2, 3];
#     let x = arr[1.5];
# }
# """
#     expected = 'Type Mismatch In Expression: ArrayAccess(Identifier(arr), FloatLiteral(1.5))'
#     assert Checker(source).check_from_source() == expected


# def test_044():
#     """Variable shadowing parameter"""
#     source = """
# func shadow(x: int) -> void {
#     let x: string = "hidden";
# }
# func main() -> void {
#     let x = shadow(5);
# }
# """
#     expected = 'Redeclared Variable: x'
#     assert Checker(source).check_from_source() == expected


# def test_045():
#     """Array type mismatch assignment"""
#     source = """
# func main() -> void {
#     let a: [int; 2] = [1, 2];
#     let b: [float; 2] = [1.0, 2.0];
#     a = b;
# }
# """
#     expected = 'Type Mismatch In Statement: Assignment(IdLValue(a), Identifier(b))'
#     assert Checker(source).check_from_source() == expected


# def test_046():
#     """Void function returning non-void"""
#     source = """
# func test() -> void {
#     return "oops";
# }
# func main() -> void {
    
# }
# """
#     expected = 'Type Mismatch In Statement: ReturnStmt(StringLiteral(\'oops\'))'
#     assert Checker(source).check_from_source() == expected


# def test_047():
#     """Heterogeneous array literal"""
#     source = """
# func main() -> void {
#     let a = [1, "2", 3];
# }
# """
#     expected = 'Type Mismatch In Expression: ArrayLiteral([IntegerLiteral(1), StringLiteral(\'2\'), IntegerLiteral(3)])'
#     assert Checker(source).check_from_source() == expected


# def test_048():
#     """Redeclared constant"""
#     source = """
# const MAX = 10;
# const MAX = 20;
# func main() -> void {}
# """
#     expected = 'Redeclared Constant: MAX'
#     assert Checker(source).check_from_source() == expected


# def test_049():
#     """Empty array type inference failure"""
#     source = """
# func main() -> void {
#     let a = [];
# }
# """
#     expected = 'Type Cannot Be Inferred: VarDecl(a, ArrayLiteral([]))'
#     assert Checker(source).check_from_source() == expected


# def test_050():
#     """Using void function in expression"""
#     source = """
# func test() -> void {
#     return;
# }
# func main() -> void {
#     let x = test();
# }
# """
#     expected = 'Type Mismatch In Expression: VarDecl(x, FunctionCall(Identifier(test), []))'
#     assert Checker(source).check_from_source() == expected


# def test_051():
#     """Test string concatenation with boolean"""
#     source = """
# func main() -> void {
#     let x = true + "yes";
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected

# def test_052():
#     """Test valid pipeline operator"""
#     source = """
# func shift(x: int) -> int {
#     return x + 1;
# }
# func main() -> void {
#     let result = 5 >> shift;
# }    
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected
    
# def test_053():
#     """Test pipeline operator with function call"""
#     source = """
# func wrap(x: int, y: int) -> int {
#     return x + y;
# }
# func main() -> void {
#     let result = 1 >> wrap(2);  // wrap(1, 2) = 3
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected
    
# def test_054():
#     """Test constant declaration but not in global scope"""
#     source = """
# const x: int = 10;
# func main() -> void {
#     x = 5;
# }
# """
#     expected = "Cannot Assign To Constant: Assignment(IdLValue(x), IntegerLiteral(5))"
#     assert Checker(source).check_from_source() == expected
    
# def test_055():
#     """Test mixed conditional and loop statements"""
#     source = """
#     func chatGPTsinhrathixaithoi() -> void {
#         let i = 0; // initialization
#         let msg: string = "Continue";
#         while (i < 106 && msg == "Continue") {
#             if (i % 4 == 0) {
#                 msg = "Stop"; // Break condition
#             }
#         }
#     }
# func main() -> void {
#     chatGPTsinhrathixaithoi();
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected
    
# def test_056():
#     source = """
# func dactaPPLnoqualabuachungtaphailamsaoday() -> void {
#     let i = 0;
#     let msg: string = "Continue";
#     while (i < 106 && msg) {
#         if (i % 4 == 0) {
#             msg = "Stop";
#         }
#     }
# }
# func main() -> void {
#     dactaPPLnoqualabuachungtaphailamsaoday();
# }
# """
#     expected = "Type Mismatch In Expression: BinaryOp(BinaryOp(Identifier(i), <, IntegerLiteral(106)), &&, Identifier(msg))"
#     assert Checker(source).check_from_source() == expected
    
# def test_057():
#     """Test return type mismatch"""
#     source = """
# func testReturn() -> int {
#     return "test";
# }
# func main() -> void {
#     testReturn();
# }
# """
#     expected = "Type Mismatch In Statement: ReturnStmt(StringLiteral('test'))"
#     assert Checker(source).check_from_source() == expected 

# def test_058():
#     """Test main function without body"""
#     source = """
# func main() -> void {

# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected
    
# def test_059():
#     source = """
# func a() -> string {
#     let x: int = 10;
#     if (x > 5) {
#         return "Greater than 5";
#     }
#     return "Test func";
# }

# func main() -> void {
#     a();
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected
    
# def test_060():
#     """Test forward reference in function call"""
#     source = """
# func main() -> void {
#     let x = a();
# }
# func a() -> int {
#     return 5;
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected
    
# def test_061():
#     """Test redeclared function"""
#     source = """
# func a() -> void {
# }
# func a() -> void {
# }
# func main() -> void {
# }
# """
#     expected = "Redeclared Function: a"
#     assert Checker(source).check_from_source() == expected 

# def test_062():
#     """Test concatenation with non-string type"""
#     source = """
# func main() -> void {
#     let x = "const" + 5;  // Concatenating string with integer
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected
    
# def test_063():
#     """Test concatenation with string and float"""
#     source = """
# func main() -> void {
#     let value: float = 10.5
#     let str: string = "";
#     if (value == 10.5) {
#         str = "Value is " + value;  // Concatenating string with float
#     } else {
#         str = "Value is not " + value;  // Concatenating string with float
#     }
# }
# """
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected  
    
# def test_064():
#     """Pipeline passes an extra implicit argument -> function call arity mismatch"""
#     source = """
# func add(a: int, b: int) -> int { 
#     return a + b; 
# }

# func main() -> void {
#     let result = 5 >> add(10, 15);
# };
# """
#     expected = "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(5), IntegerLiteral(10), IntegerLiteral(15)])"
#     assert Checker(source).check_from_source() == expected


# def test_065():
#     """Assigning row of wrong size into 2×2 int matrix"""
#     source = """
# func main() -> void {
#     let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
#     matrix[0] = [5, 6, 7];   // size 3 vs 2
# };
# """
#     expected = "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(matrix), IntegerLiteral(0)), ArrayLiteral([IntegerLiteral(5), IntegerLiteral(6), IntegerLiteral(7)]))"
#     assert Checker(source).check_from_source() == expected


# def test_066():
#     """Void‑returning function used as while condition"""
#     source = """
# func log() -> void { 
#     return; 
# }

# func main() -> void {
#     while (log()) {
#         // unreachable
#     }
# };
# """
#     expected = "Type Mismatch In Statement: WhileStmt(FunctionCall(Identifier(log), []), BlockStmt([]))"
#     assert Checker(source).check_from_source() == expected


# def test_067():
#     """Passing jagged 2‑D array literal to function expecting rectangular 2×3 int matrix"""
#     source = """
# func sum(arr: [[int; 3]; 2]) -> int {
#     return arr[0][0];
# }

# func main() -> void {
#     let bad = sum([[1, 2], [4, 5]]);
# };
# """
#     expected = "Type Mismatch In Expression: FunctionCall(Identifier(sum), [ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(4), IntegerLiteral(5)])])])"
#     assert Checker(source).check_from_source() == expected


# def test_068():
#     """Return array literal of wrong size from function"""
#     source = """
# func getRow() -> [int; 3] {
#     return [1, 2];   // missing one element
# };

# func main() -> void {
#     getRow();
# };
# """
#     expected = "Type Mismatch In Statement: ReturnStmt(ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]))"
#     assert Checker(source).check_from_source() == expected


# def test_069():
#     """Modulo with a float operand is illegal"""
#     source = """
# func main() -> void {
#     let x = 5.5 % 2;
# };
# """
#     expected = "Type Mismatch In Expression: BinaryOp(FloatLiteral(5.5), %, IntegerLiteral(2))"
#     assert Checker(source).check_from_source() == expected


# def test_070():
#     """Equality comparison between arrays of different sizes"""
#     source = """
# func main() -> void {
#     let ok = [1, 2] == [3, 4, 5];
# };
# """
#     expected = "Type Mismatch In Expression: BinaryOp(ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ==, ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)]))"
#     assert Checker(source).check_from_source() == expected


# def test_071():
#     """Negative array size in type annotation cannot be inferred"""
#     source = """
# func main() -> void {
#     let bad: [int; 5] = [];
# };
# """
#     expected = "Type Mismatch In Statement: VarDecl(bad, [int; 5], ArrayLiteral([]))"
#     assert Checker(source).check_from_source() == expected


# def test_072():
#     """Pipeline feeds void value to function expecting int"""
#     source = """
# func printSomething() -> void { return; }
# func inc(x: int) -> int { return x + 1; }

# func main() -> void {
#     let y = printSomething() >> inc;
# };
# """
#     expected = "Type Mismatch In Expression: FunctionCall(Identifier(inc), [FunctionCall(Identifier(printSomething), [])])"
#     assert Checker(source).check_from_source() == expected


# def test_073():
#     """Jagged literal inside variable declaration"""
#     source = """
# func main() -> void {
#     let jagged = [[1, 2], [3, 4, 5]];
# };
# """
#     expected = "Type Mismatch In Expression: ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]), ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)])])"
#     assert Checker(source).check_from_source() == expected


# def test_074():
#     """Equality between int and float"""
#     source = """
# func main() -> void {
#     let cmp = 3 == 3.14;
# };
# """
#     expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(3), ==, FloatLiteral(3.14))"
#     assert Checker(source).check_from_source() == expected


# def test_075():
#     """Logical AND between int and bool"""
#     source = """
# func main() -> void {
#     let val = 5 && true;
# };
# """
#     expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(5), &&, BooleanLiteral(True))"
#     assert Checker(source).check_from_source() == expected


# def test_076():
#     """Assign float into int array element"""
#     source = """
# func main() -> void {
#     let arr: [int; 3] = [1, 2, 3];
#     arr[0] = 3.14;
# };
# """
#     expected = "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(arr), IntegerLiteral(0)), FloatLiteral(3.14))"
#     assert Checker(source).check_from_source() == expected


# def test_077():
#     """Arithmetic + with two bool operands"""
#     source = """
# func main() -> void {
#     let bad = true + false;
# };
# """
#     expected = "Type Mismatch In Expression: BinaryOp(BooleanLiteral(True), +, BooleanLiteral(False))"
#     assert Checker(source).check_from_source() == expected


# def test_078(): # chưa xác định 
#     """Variable declared with void type"""
#     source = """
# func main() -> void {
#     let x: void = 0;
# };
# """
#     expected = "Type Mismatch In Statement: VarDecl(x, void, IntegerLiteral(0))"
#     assert Checker(source).check_from_source() == expected


# def test_079():
#     """Return without value in non‑void function"""
#     source = """
# func foo() -> int {
#     return;
# };

# func main() -> void {
#     foo();
# };
# """
#     expected = "Type Mismatch In Statement: ReturnStmt()"
#     assert Checker(source).check_from_source() == expected


# def test_080():
#     """Redeclare variable with same name as constant in the same scope""" # Const cannot declare within a function
#     source = """
# func main() -> void {
#     const val: int = 1;
#     let val: int = 2;
# };
# """
#     expected = "Redeclared Variable: val"
#     assert Checker(source).check_from_source() == expected

from utils import Checker
def test_000():
    """Pipeline lồng với biểu thức tính toán"""
    source = """
    func double(x: int) -> int { return x * 2; }
    func toStr(x: int) -> string { return "v=" + "x"; }

    func main() -> void {
        let result = (1 + 2 * 3) >> double >> toStr;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_001():
    """Nested if-else if-else with shadowed return"""
    source = """
    func check(x: int) -> int {
        if (x > 0) {
            if (x > 100) {
                return 1;
            } else if (x > 50) {
                return 2;
            } else {
                return 3;
            }
        } else {
            return 0;
        }
    }

    func main() -> void {
        let r = check(99);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_002():
    """Pipeline nested in another function call"""
    source = """
    func inc(x: int) -> int { return x + 1; }
    func add(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let r = add(inc(1 >> inc), 5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_003():
    """Function with early returns in loops"""
    source = """
    func firstEven(arr: [int; 5]) -> int {
        for (x in arr) {
            if (x % 2 == 0) {
                return x;
            }
        }
        return -1;
    }

    func main() -> void {
        let a = [1, 3, 5, 8, 9];
        let r = firstEven(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_004():
    """Function with recursive call in loop"""
    source = """
    func fact(n: int) -> int {
        if (n == 0) { return 1; }
        return n * fact(n - 1);
    }

    func main() -> void {
        for (i in [1, 2, 3]) {
            let x = fact(i);
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_005():
    """Pipeline with function returning array"""
    source = """
    func build() -> [int; 3] { return [4, 5, 6]; }
    func sum3(arr: [int; 3]) -> int { return arr[0] + arr[1] + arr[2]; }

    func main() -> void {
        let r = build() >> sum3;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_006():
    """Shadow const with variable"""
    source = """
    const PI: float = 3.14;
    func main() -> void {
        let PI: int = 10;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_007():
    """Variable declared then shadowed inside if"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            let x = 2;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_008():
    """Pipeline with return inside loop body"""
    source = """
    func shout(s: string) -> string { return s + "!"; }
    func toUpper(s: string) -> string { return s; }

    func process(words: [string; 3]) -> string {
        for (w in words) {
            return w >> toUpper >> shout;
        }
        return "";
    }

    func main() -> void {
        let w = ["a", "b", "c"];
        let result = process(w);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_009():
    """Using break to skip return in some path"""
    source = """
    func f(x: int) -> int {
        while (true) {
            break;
        }
        return x;
    }
    func main() -> void {
        let x = f(1);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_010():
    """Nested pipeline with mixed arguments"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func double(x: int) -> int { return x * 2; }

    func main() -> void {
        let r = 5 >> add(3) >> double;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_011():
    """Recursive fibonacci with if-else return"""
    source = """
    func fib(n: int) -> int {
        if (n <= 1) { return n; }
        return fib(n-1) + fib(n-2);
    }

    func main() -> void {
        let x = fib(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_012():
    """Return only in some if branches"""
    source = """
    func check(x: int) -> int {
        if (x == 0) {
            return 0;
        } else if (x == 1) {
            return 1;
        } else {
            return 2;
        }
    }

    func main() -> void {
        let r = check(2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_013():
    """Nested function definitions and calls"""
    source = """
    func square(x: int) -> int { return x * x; }
    func add(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let result = square(add(2, 3));
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_014():
    """Pipeline with function returning float"""
    source = """
    func toFloat(x: int) -> float { return 1.0 * x; }
    func half(x: float) -> float { return x / 2.0; }

    func main() -> void {
        let result = 10 >> toFloat >> half;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_015():
    """Function returning array passed to another"""
    source = """
    func gen() -> [int; 3] { return [1, 2, 3]; }
    func sum(a: [int; 3]) -> int { return a[0] + a[1] + a[2]; }

    func main() -> void {
        let s = gen() >> sum;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_016():
    """Early return inside while loop with condition"""
    source = """
    func findEven(arr: [int; 4]) -> int {
        let i = 0;
        while (i < 4) {
            if (arr[i] % 2 == 0)  { return arr[i]; }
            i = i + 1;
        }
        return -1;
    }

    func main() -> void {
        let a = [1, 3, 5, 6];
        let r = findEven(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_017():
    """Multiple shadowing in different scopes"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            let x = 2;
            if (true) {
                let x = 3;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_018():
    """Break and return inside nested loop"""
    source = """
    func find() -> int {
        for (x in [1,2,3]) {
            while (true) {
                break;
            }
        }
        return 0;
    }

    func main() -> void {
        let r = find();
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_019():
    """Pipeline with string transformation chain"""
    source = """
    func trim(s: string) -> string { return s; }
    func upper(s: string) -> string { return s; }
    func addDot(s: string) -> string { return s + "."; }

    func main() -> void {
        let s = " hello " >> trim >> upper >> addDot;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_020():
    """Function with all return in nested if/else"""
    source = """
    func complex(x: int) -> int {
        if (x < 0) {
            return -1;
        } else {
            if (x == 0) {
                return 0;
            } else {
                return 1;
            }
        }
    }

    func main() -> void {
        let r = complex(10);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_021():
    """Pipeline using function call with multiple params"""
    source = """
    func join(a: string, b: string) -> string { return a + b; }

    func main() -> void {
        let result = "Hi" >> join("!");
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_022():
    """Array access with type match and bounds check"""
    source = """
    func main() -> void {
        let a = [10, 20, 30];
        let x: int = a[1];
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_023():
    """Return only in else branch should raise error""" 
    source = """
    func f(x: int) -> int {
        if (x > 0) {
        } else {
            return x;
        }
    }

    func main() -> void {
        let r = f(3);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([]), else_stmt=BlockStmt([ReturnStmt(Identifier(x))]))]" 
    assert Checker(source).check_from_source().startswith("Type Mismatch In Statement")

def test_024():
    """Function returning void used in pipeline should fail"""
    source = """
    func say(x: string) -> void {}

    func main() -> void {
        let r = "hi" >> say;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(r, BinaryOp(StringLiteral('hi'), >>, Identifier(say)))"
    assert Checker(source).check_from_source() == expected

def test_025():
    """Array element assign with wrong type"""
    source = """
    func main() -> void {
        let a: [int; 3] = [1, 2, 3];
        a[1] = "hello";
    }
    """
    expected = "Type Mismatch In Statement: Assignment(..."
    assert Checker(source).check_from_source().startswith("Type Mismatch In Statement")

def test_026():
    """Recursive even check with modulo"""
    source = """
    func even(x: int) -> bool {
        if (x == 0) { return true; }
        if (x == 1) { return false; }
        return even(x - 2);
    }

    func main() -> void {
        let r = even(4);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_027():
    """Pipeline chain with inferred types"""
    source = """
    func plus1(x: int) -> int { return x + 1; }
    func times3(x: int) -> int { return x * 3; }

    func main() -> void {
        let result = 4 >> plus1 >> times3;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_028():
    """Deeply nested if-else with returns"""
    source = """
    func classify(x: int) -> string {
        if (x > 0) {
            if (x < 10) { return "small"; }
            else { return "large"; }
        } else {
            return "non-positive";
        }
    }

    func main() -> void {
        let c = classify(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_029():
    """Array passed into pipeline function"""
    source = """
    func sum3(arr: [int; 3]) -> int { return arr[0] + arr[1] + arr[2]; }

    func main() -> void {
        let x = [10, 20, 30] >> sum3;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_030():
    """Pipeline with nested calls and binary op"""
    source = """
    func mul(x: int, y: int) -> int { return x * y; }
    func inc(x: int) -> int { return x + 1; }
    func main() -> void {
        let r = (2 + 3) >> inc >> mul(2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_031():
    """Recursive factorial with condition"""
    source = """
    func fact(n: int) -> int {
        if (n <= 1) {
            return 1;
        } else {
            return n * fact(n - 1);
        }
    }

    func main() -> void {
        let x = fact(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_032():
    """Pipeline with function expecting array as 1st param"""
    source = """
    func get(arr: [int; 3], idx: int) -> int { return arr[idx]; }

    func main() -> void {
        let arr = [1,2,3];
        let x = arr >> get(2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_033():
    """Early return from nested while with if"""
    source = """
    func find5(arr: [int; 5]) -> int {
        let i = 0;
        while (i < 5) {
            if (arr[i] == 5) {
                return 5;
            }
            i = i + 1;
        }
        return -1;
    }

    func main() -> void {
        let a = [1,2,3,4,5];
        let r = find5(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_034():
    """Nested loop, break, and return"""
    source = """
    func main() -> void {
        for (x in [1,2,3]) {
            while (true) {
                break;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_035():
    """Multiple if-else returns"""
    source = """
    func classify(n: int) -> string {
        if (n < 0) {
            return "negative";
        } else if (n == 0) {
            return "zero";
        } else {
            return "positive";
        }
    }

    func main() -> void {
        let s = classify(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_036():
    """Deep pipeline with mix of types"""
    source = """
    func toStr(x: int) -> string { return "v=" + "x"; }
    func addDot(s: string) -> string { return s + "."; }

    func main() -> void {
        let r = 100 >> toStr >> addDot;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_037():
    """Shadow parameter in inner block"""
    source = """
    func f(x: int) -> int {
        if (true) {
            let x = 10;
            return x;
        } else {
            return 0;
        }
    }

    func main() -> void {
        let r = f(1);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_038():
    """If-else chain with only one return (should fail)"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
            return x;
        }
    }

    func main() -> void {
        let x = f(2);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, ..."
    assert Checker(source).check_from_source().startswith("Type Mismatch In Statement")

def test_039():
    """Function with no return (should fail)"""
    source = """
    func f(x: int) -> int {}

    func main() -> void {
        let x = f(1);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, ..."
    assert Checker(source).check_from_source().startswith("Type Mismatch In Statement")

def test_040():
    """Function with return inside for loop with condition"""
    source = """
    func containsZero(arr: [int; 3]) -> bool {
        for (x in arr) {
            if (x == 0) {
                return true;
            }
        }
        return false;
    }

    func main() -> void {
        let result = containsZero([0,1,2]);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_041():
    """Multiple function calls with correct args"""
    source = """
    func f(x: int) -> int { return x * 2; }
    func g(x: int) -> int { return f(x) + 1; }

    func main() -> void {
        let r = g(3);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_042():
    """Pass function return into pipeline"""
    source = """
    func base() -> int { return 5; }
    func double(x: int) -> int { return x * 2; }

    func main() -> void {
        let r = base() >> double;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_043():
    """Invalid pipeline target (not function)"""
    source = """
    func main() -> void {
        let x = 5 >> 10;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(5), >>, IntegerLiteral(10))"
    assert Checker(source).check_from_source() == expected

def test_044():
    """Function with inferred return from nested ifs"""
    source = """
    func f(x: int) -> int {
        if (x > 10) {
            if (x < 20) {
                return x;
            } else {
                return x * 2;
            }
        } else {
            return -1;
        }
    }

    func main() -> void {
        let y = f(15);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_045():
    """Function using multiple return types (should fail)"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
            return x;
        } else {
            return "wrong";
        }
    }

    func main() -> void {
        let y = f(1);
    }
    """
    expected = "Type Mismatch In Statement: ReturnStmt(StringLiteral('wrong'))"
    assert Checker(source).check_from_source() == expected

def test_046():
    """Pipeline chain with functions of different return types"""
    source = """
    func intToStr(x: int) -> string { return "n=" + "x"; }
    func shout(s: string) -> string { return s + "!"; }

    func main() -> void {
        let r = 9 >> intToStr >> shout;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_047():
    """Void function in middle of pipeline (should fail)"""
    source = """
    func speak(x: string) -> void {}
    func up(s: string) -> string { return s; }

    func main() -> void {
        let r = "hi" >> speak >> up;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(BinaryOp(StringLiteral('hi'), >>, Identifier(speak)), >>, Identifier(up))"
    assert Checker(source).check_from_source() == expected

def test_048():
    """Complex nested if-else return mix"""
    source = """
    func choose(x: int) -> int {
        if (x < 0) {
            return -1;
        } else {
            if (x % 2 == 0) {
                return 0;
            } else {
                return 1;
            }
        }
    }

    func main() -> void {
        let y = choose(3);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_049():
    """Function returning wrong type in pipeline (should fail)"""
    source = """
    func f(x: int) -> bool { return true; }
    func g(x: int) -> int { return x + 1; }

    func main() -> void {
        let r = 5 >> f >> g;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(BinaryOp(IntegerLiteral(5), >>, Identifier(f)), >>, Identifier(g))"
    assert Checker(source).check_from_source() == expected

def test_050():
    """Multiple shadowed variables and nested scopes"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            let x = 2;
            while (true) {
                let x = 3;
                break;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_051():
    """Recursive even check with bool return"""
    source = """
    func isEven(n: int) -> bool {
        if (n == 0) {
            return true;
        } else if (n == 1) {
            return false;
        } else {
            return isEven(n - 2);
        }
    }

    func main() -> void {
        let res = isEven(6);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_052():
    """Pipeline with mixed literal and call expressions"""
    source = """
    func wrap(x: string) -> string { return "[" + x + "]"; }
    func main() -> void {
        let s = ("hello" + "!") >> wrap;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_053():
    """Loop with return and break mixed"""
    source = """
    func findFirstEven(arr: [int; 4]) -> int {
        for (x in arr) {
            if (x % 2 == 0) {
                return x;
            }
            break;
        }
        return -1;
    }

    func main() -> void {
        let a = [1,3,4,5];
        let r = findFirstEven(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_054():
    """Pipeline with function returning array"""
    source = """
    func gen() -> [int; 2] { return [7, 8]; }
    func sum2(a: [int; 2]) -> int { return a[0] + a[1]; }

    func main() -> void {
        let result = gen() >> sum2;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_055():
    """Nested return in if-else, missing else (should fail)"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
            if (x < 5) {
                return 1;
            }
        } else {
            return -1;
        }
    }

    func main() -> void {
        let r = f(2);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, ..."
    assert Checker(source).check_from_source().startswith("Type Mismatch In Statement")

def test_056():
    """Function returning string through pipeline chain"""
    source = """
    func step1(x: int) -> string { return "v=" + "x"; }
    func step2(s: string) -> string { return s + "!"; }

    func main() -> void {
        let r = 3 >> step1 >> step2;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_057():
    """Wrong number of args in pipeline call (should fail)"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let r = 3 >> add;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(3), >>, Identifier(add))"
    assert Checker(source).check_from_source() == expected

def test_058():
    """Recursive fibonacci with correct return logic"""
    source = """
    func fib(n: int) -> int {
        if (n <= 1) {
            return n;
        } else {
            return fib(n-1) + fib(n-2);
        }
    }

    func main() -> void {
        let x = fib(6);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_059():
    """Return value from nested pipeline computation"""
    source = """
    func times2(x: int) -> int { return x * 2; }
    func str(x: int) -> string { return "n=" + "x"; }

    func main() -> void {
        let r = (1 + 2) >> times2 >> str;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_060():
    """Recursive factorial with check"""
    source = """
    func fact(n: int) -> int {
        if (n == 0) { return 1; }
        return n * fact(n - 1);
    }

    func main() -> void {
        let r = fact(4);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_061():
    """Shadowing in loop and if block"""
    source = """
    func main() -> void {
        let x = 1;
        for (x in [2,3]) {
            if (true) {
                let x = 5;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_062():
    """Invalid: void return type used in expression"""
    source = """
    func speak(msg: string) -> void {}
    func main() -> void {
        let x = "hi" >> speak;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, BinaryOp(StringLiteral('hi'), >>, Identifier(speak)))"
    assert Checker(source).check_from_source() == expected

def test_063():
    """Multiple break inside nested loops"""
    source = """
    func main() -> void {
        for (i in [1,2,3]) {
            while (true) {
                if (i > 1) { break; }
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_064():
    """Deep nested pipeline with math"""
    source = """
    func inc(x: int) -> int { return x + 1; }
    func sqr(x: int) -> int { return x * x; }

    func main() -> void {
        let result = ((1 + 2) * 3) >> inc >> sqr;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_065():
    """Call function with wrong number of args"""
    source = """
    func sum(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let a = sum(1);
    }
    """
    expected = "Type Mismatch In Expression: FunctionCall(Identifier(sum), [IntegerLiteral(1)])"
    assert Checker(source).check_from_source() == expected

def test_066():
    """Assign void return value to variable"""
    source = """
    func say(s: string) -> void {}

    func main() -> void {
        let x: void = say("hello");
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, void, FunctionCall(Identifier(say), [StringLiteral('hello')]))"
    assert Checker(source).check_from_source() == expected

def test_067():
    """Pipeline chaining with multiple params"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func mul(x: int) -> int { return x * 2; }

    func main() -> void {
        let res = 4 >> add(3) >> mul;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_068():
    """Return only in inner else branch (should fail)"""
    source = """
    func test(x: int) -> int {
        if (x > 0) {
            if (x < 10) {}
            else { return 1; }
        } else {
            return 0;
        }
    }

    func main() -> void {
        let y = test(3);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(test, [Param(x, int)], int, [...])"
    assert Checker(source).check_from_source().startswith("Type Mismatch In Statement")

def test_069():
    """Correct function with nested condition return"""
    source = """
    func test(x: int) -> int {
        if (x > 0) {
            if (x > 5) { return 1; }
            else { return 2; }
        } else {
            return 0;
        }
    }

    func main() -> void {
        let r = test(7);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_070():
    """Nested if-else with return in all paths"""
    source = """
    func grade(score: int) -> string {
        if (score >= 90) { return "A"; }
        else {
            if (score >= 80) { return "B"; }
            else if (score >= 70) { return "C"; }
            else { return "F"; }
        }
    }
    func main() -> void {
        let g = grade(85);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_071():
    """Function computing max of array"""
    source = """
    func max(arr: [int; 5]) -> int {
        let m = arr[0];
        for (x in arr) {
            if (x > m) { m = x; }
        }
        return m;
    }
    func main() -> void {
        let a = [3, 8, 2, 7, 4];
        let r = max(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_072():
    """Multi-param function in pipeline"""
    source = """
    func wrap(s: string, pre: string, post: string) -> string {
        return pre + s + post;
    }
    func main() -> void {
        let r = "msg" >> wrap("[", "]");
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_073():
    """Incorrect type in pipeline (should fail)"""
    source = """
    func double(x: int) -> int { return x * 2; }
    func main() -> void {
        let s = "abc" >> double;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(StringLiteral('abc'), >>, Identifier(double))"
    assert Checker(source).check_from_source() == expected

def test_074():
    """Valid: nested call with shadowed name"""
    source = """
    func main() -> void {
        let print = 5;
        {
            let print = 10;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_075():
    """Recursive GCD"""
    source = """
    func gcd(a: int, b: int) -> int {
        if (b == 0) { return a; }
        return gcd(b, a % b);
    }
    func main() -> void {
        let r = gcd(48, 18);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_076():
    """While with condition false from start"""
    source = """
    func main() -> void {
        while (false) {
            let x = 5;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_077():
    """Break used correctly inside loop"""
    source = """
    func find(arr: [int; 3]) -> int {
        for (x in arr) {
            if (x == 2) { break; }
        }
        return 1;
    }
    func main() -> void {
        let a = [1, 2, 3];
        let r = find(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_078():
    """Const with valid global scope"""
    source = """
    const ID: int = 101;
    func main() -> void {
        let x = ID;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_079():
    """Assign void type function result (should fail)"""
    source = """
    func act() -> void {}
    func main() -> void {
        let r = act();
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(r, FunctionCall(Identifier(act), []))"
    assert Checker(source).check_from_source() == expected

def test_080():
    """Check inferred array type"""
    source = """
    func main() -> void {
        let a = [1, 2, 3];
        let b: int = a[1];
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_081():
    """Function declared but never used"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func main() -> void {
        let a = 5;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_082():
    """Nested if-else missing return (should fail)"""
    source = """
    func choose(x: int) -> int {
        if (x > 0) {
            if (x < 10) {}
            else { return 2; }
        } else { return 0; }
    }
    func main() -> void {
        let r = choose(5);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(choose, [Param(x, int)], int, [...])"
    assert Checker(source).check_from_source().startswith("Type Mismatch In Statement")

def test_083():
    """Correct inferred type for array function"""
    source = """
    func squareEach(arr: [int; 3]) -> [int; 3] {
        return [arr[0]*arr[0], arr[1]*arr[1], arr[2]*arr[2]];
    }
    func main() -> void {
        let a = [2,3,4];
        let r = squareEach(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_084():
    """Array out of bounds (semantic ignores)"""
    source = """
    func main() -> void {
        let a = [1,2,3];
        let x = a[5];
    }
    """
    expected = "Static checking passed" # Should check in runtime not seman so will be passed here
    assert Checker(source).check_from_source() == expected  # Assuming runtime check

def test_085():
    """Pipeline with nested call and math"""
    source = """
    func double(x: int) -> int { return x * 2; }
    func dec(x: int) -> int { return x - 1; }

    func main() -> void {
        let r = (3 + 4) >> double >> dec;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_086():
    """Return based on loop exit"""
    source = """
    func detect(arr: [int; 3]) -> int {
        for (x in arr) {
            if (x == 9) { return 1; }
        }
        return 0;
    }
    func main() -> void {
        let a = [1,2,9];
        let x = detect(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_087():
    """Invalid: assign array to int"""
    source = """
    func main() -> void {
        let a = [1,2,3];
        let b: int = a;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(b, int, Identifier(a))"
    assert Checker(source).check_from_source() == expected

def test_088():
    """Incorrect return structure in nested condition"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
            if (x == 1) { return 1; }
        } else {
            return 2;
        }
    }
    func main() -> void {
        let y = f(3);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, [Param(x, int)], int, [...])"
    assert Checker(source).check_from_source().startswith("Type Mismatch In Statement")

def test_089():
    """Function with early return then fallback"""
    source = """
    func check(x: int) -> int {
        if (x == 1) { return 10; }
        return 0;
    }
    func main() -> void {
        let r = check(1);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_090():
    """Mutually recursive functions with condition"""
    source = """
    func isEven(n: int) -> bool {
        if (n == 0) { return true; } else { return isOdd(n - 1); }
    }

    func isOdd(n: int) -> bool {
        if (n == 0) { return false; } else { return isEven(n - 1); }
    }

    func main() -> void {
        let x = isEven(10);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_091():
    """Pipeline through inferred variable then used"""
    source = """
    func f(x: int) -> int { return x + 1; }
    func g(x: int) -> int { return x * 2; }

    func main() -> void {
        let temp = 3 >> f;
        let final = temp >> g;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_092():
    """Array of arrays used in loop"""
    source = """
    func main() -> void {
        let matrix = [[1,2], [3,4]];
        for (row in matrix) {
            for (val in row) {
                let x = val;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_093():
    """Shadow function name with variable inside block"""
    source = """
    func printVal(x: int) -> void {}

    func main() -> void {
        if (true) {
            let printVal = 100;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_094():
    """Loop with complex return in each branch"""
    source = """
    func sumFirstEven(arr: [int; 4]) -> int {
        let i = 0;
        while (i < 4) {
            if (arr[i] % 2 == 0) { return arr[i]; } else { i = i + 1; }
        }
        return -1;
    }

    func main() -> void {
        let a = [1, 3, 5, 6];
        let x = sumFirstEven(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_095():
    """Function returning function result from another"""
    source = """
    func square(x: int) -> int { return x * x; }
    func compute(x: int) -> int { return square(x); }

    func main() -> void {
        let r = compute(4);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_096():
    """Multiple return paths with mixed if else"""
    source = """
    func choose(x: int) -> int {
        if (x == 1) { return 1; } else {
            if (x == 2) { return 2; } else { return 3; }
        }
    }

    func main() -> void {
        let x = choose(2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_097():
    """Check bool in pipeline type check"""
    source = """
    func negate(x: bool) -> bool { return !x; }

    func main() -> void {
        let b = true >> negate;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_098():
    """Multiple parameters in pipeline with math"""
    source = """
    func operate(x: int, y: int) -> int { return x * y; }

    func main() -> void {
        let r = 5 >> operate(3);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_099():
    """Pipeline with function call returning array"""
    source = """
    func build() -> [int; 2] { return [5, 6]; }
    func head(arr: [int; 2]) -> int { return arr[0]; }

    func main() -> void {
        let result = build() >> head;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_100():
    """Pipeline with deeply nested calls"""
    source = """
    func trim(s: string) -> string { return s; }
    func upper(s: string) -> string { return s; }
    func addExcl(s: string) -> string { return s + "!"; }

    func main() -> void {
        let result = "hello" >> trim >> upper >> addExcl;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_101():
    """Recursive function with conditional logic"""
    source = """
    func gcd(a: int, b: int) -> int {
        if (b == 0) { return a; } else { return gcd(b, a % b); }
    }

    func main() -> void {
        let r = gcd(28, 14);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_102():
    """Break inside nested while with return after"""
    source = """
    func check() -> int {
        while (true) {
            if (true) { break; }
        }
        return 1;
    }

    func main() -> void {
        let x = check();
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_103():
    """Array pipeline to sum"""
    source = """
    func sum(arr: [int; 3]) -> int { return arr[0] + arr[1] + arr[2]; }

    func main() -> void {
        let a = [1, 2, 3] >> sum;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_104():
    """Nested if-else with multiple shadowing"""
    source = """
    func main() -> void {
        let x = 10;
        if (true) {
            let x = 20;
            if (x > 10) {
                let x = 30;
            } else {
                let x = 40;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_105():
    """Pipeline and normal call mixed"""
    source = """
    func f(x: int) -> int { return x + 1; }
    func g(x: int) -> int { return x * 2; }

    func main() -> void {
        let a = 5 >> f;
        let b = g(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_106():
    """If else if else with return in every path"""
    source = """
    func check(x: int) -> int {
        if (x < 0) { return -1; } 
        else if (x == 0) { return 0; } 
        else { return 1; }
    }

    func main() -> void {
        let r = check(-1);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_107():
    """Complex pipeline with math"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func mul(x: int) -> int { return x * 2; }

    func main() -> void {
        let r = (1 + 2) >> add(3) >> mul;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_108():
    """Array index assignment with correct type"""
    source = """
    func main() -> void {
        let a: [int; 3] = [1,2,3];
        a[0] = 5;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_109():
    """Return in while with conditional break"""
    source = """
    func loopCheck(n: int) -> int {
        let i = 0;
        while (i < n) {
            if (i == 2) { return i; }
            i = i + 1;
        }
        return -1;
    }

    func main() -> void {
        let x = loopCheck(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_110():
    """Array passed to pipeline expecting same"""
    source = """
    func sumAll(arr: [int; 3]) -> int {
        return arr[0] + arr[1] + arr[2];
    }

    func main() -> void {
        let r = [1,2,3] >> sumAll;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_111():
    """If with return but no else"""
    source = """
    func f(x: int) -> int {
        if (x > 0) { return x; }
        return -1;
    }

    func main() -> void {
        let x = f(3);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_112():
    """Multi-level nested return logic"""
    source = """
    func evaluate(x: int) -> int {
        if (x < 10) {
            if (x == 5) { return 0; }
            else { return 1; }
        } else {
            return 2;
        }
    }

    func main() -> void {
        let x = evaluate(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_113():
    """Array index used in expression"""
    source = """
    func main() -> void {
        let a = [1,2,3];
        let b = a[1] + 10;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_114():
    """Pipeline with wrong argument count"""
    source = """
    func f(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let r = 5 >> f;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(5), >>, Identifier(f))"
    assert Checker(source).check_from_source() == expected

def test_115():
    """Function call with void return used wrongly"""
    source = """
    func speak(msg: string) -> void {}

    func main() -> void {
        let x = speak("hi");
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, FunctionCall(Identifier(speak), [StringLiteral('hi')]))"
    assert Checker(source).check_from_source() == expected

def test_116():
    """Return inside loop and after loop"""
    source = """
    func search(arr: [int; 3], target: int) -> int {
        for (x in arr) {
            if (x == target) { return x; }
        }
        return -1;
    }

    func main() -> void {
        let r = search([1,2,3], 2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_117():
    """Invalid pipeline with void function"""
    source = """
    func show(x: int) -> void {}

    func main() -> void {
        let x = 5 >> show;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, BinaryOp(IntegerLiteral(5), >>, Identifier(show)))"
    assert Checker(source).check_from_source() == expected

def test_118():
    """Shadowing inside nested if"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            let x = 2;
            if (true) {
                let x = 3;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_119():
    """Return missing in one if branch"""
    source = """
    func bad(x: int) -> int {
        if (x == 1) { } else { return x; }
    }

    func main() -> void {
        let x = bad(2);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(bad, [Param(x, int)], int, ...)"
    assert "Type Mismatch In Statement" in Checker(source).check_from_source()

def test_120():
    """Hàm nhận array nhưng truyền int"""
    # lời gọi hàm f(x) ở đây là một Stmt và có kiểu ctx là ExprStmt(FunctionCall...), cần phân biệt nó với lời gọi hàm ở một phép gán, lúc này thì lời gọi hàm sẽ là một expr
    source = """
func f(a: [int; 3]) -> void {}

func main() -> void {
    let x: int = 5;
    f(x);
}
"""
    expected = "Type Mismatch In Statement: FunctionCall(Identifier(f), [Identifier(x)])"
    assert Checker(source).check_from_source() == expected

def test_121():
    """Test a valid program that should pass all checks"""
    source = """
    const PI: float = 3.14;
    func main() -> void {
        let x: int = 5;
        let y = x + 1;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"
    
def test_122():
    """Test Redeclared variable"""
    source = """
    func main() -> void {
        let x: int = 5;
        let x = 1;
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: x"

def test_123():
    """Test Redeclared constant"""
    source = """
    const PI: float = 3.14;
    const PI: float = 10.14;
    func main() -> void {
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Constant: PI"

def test_124():
    """Test Redeclared as a constant"""
    source = """
    const x: int = 5;
    const x: int = 10;
    func main() -> void {
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Constant: x"

def test_125():
    """Test Redeclared function"""
    source = """
    func foo() -> void {}
    func foo() -> int { return 1; }
    func main() -> void {
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Function: foo"

def test_126():
    """Test shadowing a variable"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            x = 2;
        }
        else {
            x = 0;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_127():
    """Test shadowing a constant"""
    source = """
    const MAX = 100;
    func main() -> void {
        MAX = 50;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(MAX), IntegerLiteral(50))"

def test_128():
    """Test shadowing a constant as a variable"""
    source = """
    const MAX = 100;
    func main() -> void {
        let MAX = 13;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_129():
    """Test Redeclared Parameter"""
    source = """
    func foo(x: int) -> int {
        let x: int = 23;
        return x;    
    }
    
    func main() -> void {  
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: x"
    
def test_130():
    """Test Redeclared variable in a loop"""
    source = """
    func main() -> void {
        let arr: [int; 2] = [1,2];  
        for(i in arr) {
            let i = 5;
        }
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: i"

def test_131():
    """Test Undeclared identifier"""
    source = """
    func main() -> void {  
        let x = y;
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: y"

def test_132():
    """Test Undeclared function"""
    source = """
    func main() -> void {  
        foo();
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: foo"

def test_133():
    """Test using a variable before declaration"""
    source = """
    func main() -> void {  
        let x = y;
        let y = 1;
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: y"

def test_135():
    """Test out of scope variable"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> void {  
        if (true) {
            let s = "hello";
        }
        print(s);
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: s"

def test_137():
    """Test using constant before declaration"""
    source = """
    func main() -> void {  
        let x = MAX;
    }
    const MAX: int = 100;
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_138():
    """Test invalid index - string index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number["1"];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), StringLiteral('1'))" 

def test_139():
    """Test invalid index - float index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number[2.3];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), FloatLiteral(2.3))"

def test_140():
    """Test invalid index - array index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let string_: [string; 3] = ["P", "P", "L"];
        let result = number[string_];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), Identifier(string_))"

def test_141():
    """Test invalid index - bool index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number[false];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), BooleanLiteral(False))"

def test_142():
    """Test Binary operation errors - sum = int + bool"""
    source = """
    func main() -> void {  
        let x = 2;
        let y = true;
        let sum = x + y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), +, Identifier(y))"

def test_143():
    """Test Binary operation errors - sum = int + float"""
    source = """
    func main() -> void {  
        let x = 2;
        let y = 0.3;
        let sum = x + y;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_144():
    """Test Binary operation errors - sum = string + string"""
    source = """
    func main() -> void {  
        let x = "Hello";
        let y = "World";
        let sum = x + y;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_145():
    """Test Binary operation errors - comparision: int vs float"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = 5.0;
        let comparision = x > y;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_146():
    """Test Binary operation errors - comparision: int vs string"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = "hi";
        let comparision = x > y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), >, Identifier(y))"

def test_147():
    """Test Binary operation errors - equality: int vs float"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = 5.0;
        let equality = x == y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), ==, Identifier(y))"

def test_148():
    """Test Binary operation errors - equality: int vs string"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = "hi";
        let equality = x != y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), !=, Identifier(y))"

def test_149():
    """Test Binary operation errors - logical: int vs bool"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = true;
        let equality = x && y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), &&, Identifier(y))"

def test_150():
    """Test Binary operation errors - logical: int vs bool"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = false;
        let equality = x || y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), ||, Identifier(y))"

def test_151():
    """Test Binary operation errors - mod: int vs float"""
    source = """
    func main() -> void {  
        let module = 45 % 104;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_152():
    """Test Unary operation errors - not: int"""
    source = """
    func main() -> void {  
        let x = !4;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(!, IntegerLiteral(4))"

def test_153():
    """Test Unary operation errors - not: float"""
    source = """
    func main() -> void {  
        let x = !4.3;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(!, FloatLiteral(4.3))"

def test_154():
    """Test Unary operation errors - sub/plus: bool"""
    source = """
    func main() -> void {  
        let x = -false;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(-, BooleanLiteral(False))"

def test_155():
    """Test Unary operation errors - sub/plus: string"""
    source = """
    func main() -> void {  
        let x = -"hi";
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(-, StringLiteral('hi'))"

def test_156():
    """Test Function call - void function"""
    source = """
    func print(s: string) -> void { return; }
    
    func main() -> void {  
        let x = print("hi");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(x, FunctionCall(Identifier(print), [StringLiteral('hi')]))"

def test_157():
    """Test Function call - wrong args"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    
    func main() -> void {  
        let x = add(5, "sh");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(5), StringLiteral('sh')])"

def test_158():
    """Test Function call - too few args"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    
    func main() -> void {  
        let x = add(5);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(5)])"

def test_159():
    """Test Function call - too many args"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    
    func main() -> void {  
        let x = add(5,3,4);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(5), IntegerLiteral(3), IntegerLiteral(4)])"

def test_160():
    """Test Array type mismatches - int + float"""
    source = """    
    func main() -> void {  
        let number: [int; 2] = [36, 63];
        let floatArray: [float; 2] = [3.6, 6.3];
        let x = number[0] + floatArray[0];
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_161():
    """Test Array type mismatches - int + string"""
    source = """    
    func main() -> void {  
        let number: [int; 2] = [36, 63];
        let string_: [string; 2] = ["3.6", "6.3"];
        let x = number[0] + string_[0];
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_162():
    """Test Nested expression errors - bool index"""
    source = """    
    func main() -> void {  
        let number: [int; 2] = [36, 63];
        let x = number[number[true]];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), BooleanLiteral(True))"

def test_163():
    """Test Function with undefined return type annotation"""
    source = """   
    func noReturn() -> int {let x = 5;} 
    func main() -> void {  
        noReturn();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FuncDecl(noReturn, [], int, [VarDecl(x, IntegerLiteral(5))])"

def test_164():
    """Test Empty array without type annotation"""
    source = """   
    func main() -> void {  
        let arr = [];
        arr[1] = 67;
    }
    """
    assert Checker(source).check_from_source() == "Type Cannot Be Inferred: VarDecl(arr, ArrayLiteral([]))"

def test_165():
    """Test Forward reference in initialization"""
    source = """   
    func sub(x: int, y: int) -> int { return x + y; }
    func main() -> void {  
        let sum = sub(x,y);
        let x = 2;
        let y = 5;
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: x"

def test_166():
    """Test Complex expression without sufficient context"""
    source = """   
    func type_list() -> bool { 
        let typ = Circle;
        return true;
    }
    func main() -> void {  
        let typ = type_list();
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: Circle"

def test_167():
    """Test Mixed array elements without clear type"""
    source = """   
    func print(s: string) -> string {
        return s;
    }
    
    func getInt() -> int { 
        return 5;
    }
    
    func getFloat() -> float {
        return 7.7;
    }
    
    func main() -> void {  
        let mix = [getInt(), getFloat()];
        print(str(len(mixed)));
    }
    """
    assert Checker(source).check_from_source() == "Type Cannot Be Inferred: VarDecl(mix, ArrayLiteral([FunctionCall(Identifier(getInt), []), FunctionCall(Identifier(getFloat), [])]))"
def test_168():
    """Test Function call without void type"""
    source = """   
    func getInt() -> int { 
        return 5;
    }
    
    func main() -> void {  
        getInt();
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_169():
    """Test Function call: void with return"""
    source = """   
    func foo() -> void { 
        return;
    }
    
    func main() -> void {  
        foo();
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_170():
    """Test Conditional statement errors - int condition"""
    source = """   
    func main() -> void {  
        let x = 5;
        if (x) {
            x = 1;
        }
        else {
            x = 0;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: IfStmt(condition=Identifier(x), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]), else_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(0))]))"

def test_171():
    """Test Conditional statement errors - string condition"""
    source = """   
    func main() -> void {  
        let x = "hello";
        if (x) {
            x = "1";
        }
        else {
            x = "0";
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: IfStmt(condition=Identifier(x), then_stmt=BlockStmt([Assignment(IdLValue(x), StringLiteral('1'))]), else_stmt=BlockStmt([Assignment(IdLValue(x), StringLiteral('0'))]))"

def test_172():
    """Test Conditional statement errors - string in logical expression"""
    source = """   
    func main() -> void {  
        let x = "hello";
        let y = 6;
        if (x && y > 5) {
            x = "1";
        }
    }
    """
    # cái này cũng confuse, hỏi thầy sau
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), &&, BinaryOp(Identifier(y), >, IntegerLiteral(5)))"

def test_173():
    """Test Loop statement errors - int condition"""
    source = """   
    func main() -> void {  
        let x = 5;
        while (x) {
            x = 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: WhileStmt(Identifier(x), BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]))"

def test_174():
    """Test Loop statement errors - string condition"""
    source = """   
    func main() -> void {  
        let x = "hello";
        while (x) {
            x = "hi";
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: WhileStmt(Identifier(x), BlockStmt([Assignment(IdLValue(x), StringLiteral('hi'))]))"

def test_175():
    """Test Loop statement errors - int is not iterable"""
    source = """   
    func main() -> void {  
        let x = 23;
        for (i in x) {
            let y = 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ForStmt(i, Identifier(x), BlockStmt([VarDecl(y, IntegerLiteral(1))]))"

def test_176():
    """Test Loop statement errors - string is not iterable"""
    source = """   
    func main() -> void {  
        let x = "hello";
        for (i in x) {
            let y = 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ForStmt(i, Identifier(x), BlockStmt([VarDecl(y, IntegerLiteral(1))]))"

def test_177():
    """Test Assignment statement errors - int to string"""
    source = """   
    func main() -> void {  
        let x = "hello";
        x = 1;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(x), IntegerLiteral(1))"

def test_178():
    """Test Assignment statement errors - float to bool"""
    source = """   
    func main() -> void {  
        let x = true;
        x = 1.0;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(x), FloatLiteral(1.0))"

def test_179():
    """Test Assignment statement errors - float array to int array"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = 2.3;
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), FloatLiteral(2.3))"

def test_180():
    """Test Assignment statement errors - float to int element"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = 2.3;
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), FloatLiteral(2.3))"

def test_181():
    """Test Assignment statement errors - string to int element"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = "hi";
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), StringLiteral('hi'))"

def test_182():
    """Test Assignment statement errors - float array to int array"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number = [1.0, 2.0];
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(number), ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0)]))"

def test_183():
    """Test Constant assignment error"""
    source = """   
    const MAX = 36;
    func main() -> void {
        MAX = 37;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(MAX), IntegerLiteral(37))"

def test_184():
    """Test Return statement errors - bool to int"""
    source = """   
    func returnInt() -> int {
        return false;
    }
    
    func main() -> void {
        let x = returnInt();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(BooleanLiteral(False))"

def test_185():
    """Test Return statement errors - string to float"""
    source = """   
    func returnFloat() -> float {
        return "hello";
    }
    
    func main() -> void {
        let x = returnFloat();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(StringLiteral('hello'))"

def test_186():
    """Test Return statement errors - string to float"""
    source = """   
    func returnArray() -> [int; 3] {
        return [1.0, 2.0, 3.0];
    }
    
    func main() -> void {
        let x = returnArray();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(3.0)]))"

def test_187():
    """Test Return statement errors - int to void"""
    source = """   
    func returnVoid() -> void {
        return 36;
    }
    
    func main() -> void {
        returnVoid();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(IntegerLiteral(36))"

def test_188():
    """Test Function call statement errors - void function assigned to variable"""
    source = """   
    func returnVoid() -> void {
        return;
    }
    
    func main() -> void {
        let x = 0;
        x = returnVoid();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(x), FunctionCall(Identifier(returnVoid), []))"

def test_189():
    """Test Function call statement errors - string args to int params"""
    source = """   
    func add(x: int, y: int) -> int {
        return x + y;
    }
    
    func main() -> void {
        let a = add("1", "3");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [StringLiteral('1'), StringLiteral('3')])"

def test_190():
    """Test Function call statement errors - string args to int params"""
    source = """   
    func add(x: int, y: int) -> int {
        return x + y;
    }
    
    func main() -> void {
        add("1", "3");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FunctionCall(Identifier(add), [StringLiteral('1'), StringLiteral('3')])"
def test_191():
    """Test Function call statement errors - too few args"""
    source = """   
    func add(x: int, y: int) -> int {
        return x + y;
    }
    
    func main() -> void {
        add(1);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FunctionCall(Identifier(add), [IntegerLiteral(1)])"

def test_192():
    """Test Function call errors - too many args"""
    source = """   
    func add(x: int, y: int) -> int {
        return x + y;
    }
    
    func main() -> void {
        let x = 3 >> add(1,2);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(IntegerLiteral(3), >>, FunctionCall(Identifier(add), [IntegerLiteral(1), IntegerLiteral(2)]))"

def test_193():
    """Test Complex type mismatch errors - different element types"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix = floatMatrix;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(matrix), Identifier(floatMatrix))"

def test_194():
    """Test Complex type mismatch errors - float array to int array row"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix[0] = [1.0, 2.0];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(matrix), IntegerLiteral(0)), ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0)]))"

def test_195():
    """Test Complex type mismatch errors - float to int element"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix[0][0] = 3.14;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(ArrayAccess(Identifier(matrix), IntegerLiteral(0)), IntegerLiteral(0)), FloatLiteral(3.14))"

def test_196():
    """Test Complex type mismatch errors - float row index"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix[3.14][0] = 0;
    }
    """
    # statement hay expr gì cũng được, dựa theo mục số 9 trong spec và mục số 3 thì chắc là nên chọn Expr
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(matrix), FloatLiteral(3.14))"

def test_197():
    """Test Complex type mismatch errors - float column index"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix[0][3.14] = 0;
    }
    """
    # Cũng giống cái trên nhưng chỉ lấy số cho đồng nhất
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccessLValue(ArrayAccess(Identifier(matrix), IntegerLiteral(0)), FloatLiteral(3.14))"

def test_198():
    """Test Array size mismatch - large to small"""
    source = """   
    func main() -> void {
        let small: [int; 2] = [1, 2];
        let large: [int; 4] = [1,2,3,4];
        
        small = large;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(small), Identifier(large))"
    
def test_199():
    """Test Array size mismatch - small to large"""
    source = """   
    func main() -> void {
        let small: [int; 2] = [1, 2];
        let large: [int; 4] = [1,2,3,4];
        
        large = small;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(large), Identifier(small))"

def test_200():
    """Test If else - Just If"""
    source = """   
    func main() -> void {
        let x = 1;
        if (x > 0) {
            x = 100;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_201():
    """Test If else - If else"""
    source = """   
    func main() -> void {
        let x = 1;
        if (x > 0) {
            x = 100;
        }
        else {
            x = 10;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_202():
    """Test If else - If else if else"""
    source = """   
    func main() -> void {
        let x = 1;
        if (x > 0) {
            x = 100;
        }
        else if (x == 0){
            let y = x;
        }
        else {
            x = 10;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_203():
    """Test func If else - If else if else missing return in elif"""
    source = """   
    func ifcond(x: int) -> string {
        if (x > 1) {
            return "Hello World";
        }
        else if (x == 0) {
            let y = x;
        }
        else {
            return "Hello";
        }
    }
    func main() -> void {
        let s = ifcond(3);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FuncDecl(ifcond, [Param(x, int)], string, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(1)), then_stmt=BlockStmt([ReturnStmt(StringLiteral('Hello World'))]), elif_branches=[(BinaryOp(Identifier(x), ==, IntegerLiteral(0)), BlockStmt([VarDecl(y, Identifier(x))]))], else_stmt=BlockStmt([ReturnStmt(StringLiteral('Hello'))]))])"

def test_204():
    """Test missing arg in func"""
    source = """   
    func returnVal() -> int {
        return x;
    }
    
    func main() -> void {
        let val = returnVal();
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: x"

def test_205():
    """Test passing param in func - mising args"""
    source = """   
    func returnVal() -> int {
        return x;
    }
    
    func main() -> void {
        let val = returnVal(3);
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: x"

def test_206():
    """Test initialize array without elements"""
    source = """  
    func main() -> void {
        let a: [float; 2] = [];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(a, [float; 2], ArrayLiteral([]))"
    
def test_207():
    """Test Calling a identier as a func"""
    source = """  
    func main() -> void {
        let a = 5;
        let b = a();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(a), [])"

def test_208():
    """Test Pipeline"""
    source = """  
    func say() -> string {
        return "PPL";
    }
    
    func say1(s: string) -> string {
        return "Hi" + s;
    }
    
    func main() -> void {
        let a = say() >> say1();
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_209():
    """Test Break/continue in function scope"""
    source = """  
    func main() -> void {
        break;
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_210():
    """Test Break/continue in function scope"""
    source = """  
    func main() -> void {
        continue;
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: ContinueStmt()"

def test_211():
    """Test Break/continue in conditional blocks"""
    source = """  
    func main() -> void {
        if (true) {
            break;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_212():
    """Test Break/continue in conditional blocks"""
    source = """  
    func main() -> void {
        if (true) {
            continue;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: ContinueStmt()"

def test_213():
    """Test Break/continue in conditional blocks"""
    source = """  
    func main() -> void {
        if (true) {
            let x = 5;
        }
        else {
            break;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_214():
    """Test Break/continue in nested blocks"""
    source = """  
    func main() -> void {
        let x = 10;
        if (x > 2) {
            break;
        }
        else {
            continue;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_215():
    """Test Break/continue in while loops"""
    source = """  
    func main() -> void {
        let x = 10;
        while (x > 5) {
            if (x == 10) {
                break;
            }
            if (x % 2 == 0) {
                x = x + 1;
                continue;                  
            }
            x = x + 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_216():
    """Test Break/continue in while loops"""
    source = """  
    func main() -> void {
        let numbers = [1, 2, 3, 4, 5];
        for (num in numbers) {
            if (num == 3) {
                break;                       
            }
            if (num % 2 == 0) {
                continue;                  
            }
            let y = 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_217():
    """Test Break/continue in while loops"""
    source = """  
    func main() -> void {
        let i = 0;
        while (i < 5) {
            let j = 0;
            while (j < 5) {
                if (i == j) {
                    break;                   
                }
                if (j == 2) {
                    j = j + 1;
                    continue;
                }
                j = j + 1;
            }
            i = i + 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_218():
    """Test Break/continue after loop"""
    source = """
    func main() -> void {
        let i = 0;
        while (i < 5) {
            i = i + 1;
        }
        break;
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_219():
    """Test Break/continue in function called from loop"""
    source = """  
    func helperFunction() -> void {
        break;
        continue;
    }
    
    func main() -> void {
        helperFunction();
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_220():
    """Test program with no main function"""
    source = """
    func print(s: string) -> string {
        return s;
    } 
    
    func helper() -> void {
        print("Helper function");
    }
    
    func calculate(x: int) -> int {
        return x * 2;
    }
    """
    assert Checker(source).check_from_source() == "No Entry Point"

def test_221():
    """Test main function with wrong case-sensitive name"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func Main() -> void {
        print("Wrong case");
    }
    """
    assert Checker(source).check_from_source() == "No Entry Point"

def test_222():
    """Test main function with parameters"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main(args: [string; 5]) -> void {
        print("With arguments");
    }
    """
    assert Checker(source).check_from_source() == "No Entry Point"

def test_223():
    """Test main function with non-void return type"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> int {
        print("Returns integer");
        return 0;
    }
    """
    assert Checker(source).check_from_source() == "No Entry Point"

def test_224():
    """Test multiple main functions"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> void {
        print("First main");
    }
    
    func main() -> void {
        print("Second main");
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Function: main"

def test_225():
    """Test valid main function"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> void {
        print("Hello, World!");
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_226():
    """Test out-of-bounds array access in ArrayAccessLValue"""
    source = """
    func main() -> void {
        let numbers: [int; 5] = [1, 2, 3, 4, 5];
        numbers[10] = 0;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_227():
    """Test valid array operations"""
    source = """
    func main() -> void {
        let arr1: [int; 3] = [1, 2, 3];
        let arr2: [int; 3] = [4, 5, 6];
        arr1 = arr2;
        arr1[0] = 10;
        arr1[1] = arr2[2];
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_228():
    """Test array_literal type"""
    source = """
    func main() -> void {
        let intArray: [int; 3] = [1, 2.5, 3]; 
    }
    """
    # Tương tự
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(intArray, [int; 3], ArrayLiteral([IntegerLiteral(1), FloatLiteral(2.5), IntegerLiteral(3)]))"

def test_229():
    """Test array_literal size"""
    source = """
    func main() -> void {
        let arr1: [int; 3] = [1, 2];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(arr1, [int; 3], ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]))"

def test_230():
    """Test array return type errors"""
    source = """
    func getFloatArray() -> [float; 3] {
        return [1.0, 2.0, 3.0];
    }
    func main() -> void {
        let result1: [int; 3] = getFloatArray();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(result1, [int; 3], FunctionCall(Identifier(getFloatArray), []))"

def test_231():
    """Test array return size errors"""
    source = """
    func getThreeInts() -> [int; 3] {
        return [1, 2, 3];
    }
    func main() -> void {
        let result2: [int; 5] = getThreeInts();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(result2, [int; 5], FunctionCall(Identifier(getThreeInts), []))"

def test_232():
    """Test array return size errors"""
    source = """
    func main() -> void {
        let matrix: [[int; 2]; 3] = [[1, 2], [3, 4], [5, 6]];
        let differentMatrix: [[int; 3]; 2] = [[1, 2, 3], [4, 5, 6]];
        
        matrix = differentMatrix;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(matrix), Identifier(differentMatrix))"

def test_233():
    """Test array return size errors"""
    source = """
    func main() -> void {
        let matrix: [[int; 2]; 3] = [[1, 2], [3, 4], [5, 6]];
        let floatMatrix: [[float; 2]; 3] = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
        
        matrix = floatMatrix;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(matrix), Identifier(floatMatrix))"

def test_234():
    
    source = """
    func modifyInt(x: int) -> void {
    x = 100;  // Only modifies local parameter copy
}

    func main() -> void {
        let a: int = 5;
        modifyInt(a);
    }"""
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(x), IntegerLiteral(100))"

def test_235():
    """Test type cannot be infered array"""
    source = """
    func getValue() -> int {
        return 42;
    }
    func getOtherValue() -> float{
        return 2.;
    }
    func print(s: string) -> string {
        return s;
    }
    func len(s: [int; 2]) -> int {
        return 28;
    }

    func str(s: int) -> string {
        return "string";
    }
    
    // Error: Mixed array elements without clear type
    func mixedArrayElements() -> void {
        let mixed = [getValue(), getOtherValue()]; // TypeCannotBeInferred - unclear element type
        print(str(len(mixed)));
    }
    func main() -> void {
    }
    """
    assert Checker(source).check_from_source() == "Type Cannot Be Inferred: VarDecl(mixed, ArrayLiteral([FunctionCall(Identifier(getValue), []), FunctionCall(Identifier(getOtherValue), [])]))"
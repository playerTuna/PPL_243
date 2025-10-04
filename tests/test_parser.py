# from utils import Parser


# def test_001():
#     """Test basic function declaration"""
#     source = """func main() -> void {}"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_002():
#     """Test function with parameters"""
#     source = """func add(a: int, b: int) -> int { return a + b; }"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_003():
#     """Test variable declaration with type annotation"""
#     source = """func main() -> void { let x: int = 42; }"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_004():
#     """Test variable declaration with type inference"""
#     source = """func main() -> void { let name = "Alice"; }"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_005():
#     """Test constant declaration"""
#     source = """const PI: float = 3.14159; func main() -> void {}"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_006():
#     """Test if-else statement"""
#     source = """func main() -> void { 
#         if (x > 0) { 
#             print("positive"); 
#         } else { 
#             print("negative"); 
#         }
#     }"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_007():
#     """Test while loop"""
#     source = """func main() -> void { 
#         let i = 0;
#         while (i < 10) { 
#             i = i + 1; 
#         }
#     }"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_008():
#     """Test for loop with array"""
#     source = """func main() -> void { 
#         let numbers = [1, 2, 3, 4, 5];
#         for (num in numbers) { 
#             print(str(num)); 
#         }
#     }"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_009():
#     """Test array declaration and access"""
#     source = """func main() -> void { 
#         let arr: [int; 3] = [1, 2, 3];
#         let first = arr[0];
#         arr[1] = 42;
#     }"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_010():
#     """Test complex expression with pipeline operator"""
#     source = """func main() -> void { 
#         let result = data >> process >> validate >> transform;
#         let calculation = 5 >> add(3) >> multiply(2);
#     }"""
#     expected = "success"
#     assert Parser(source).parse() == expected


# def test_011():
#     """Test parser error: missing closing brace in function declaration"""
#     source = """func main() -> void { let x = 1; """  # Thiếu dấu }
#     expected = "Error on line 1 col 33: <EOF>"
#     assert Parser(source).parse() == expected
    
# def test_012():
#     """Test parser error: invalid type annotation"""
#     source = """func add(a: integer, b: int) -> int { return a + b; }"""  # 'integer' is not a valid type
#     expected = "Error on line 1 col 12: integer"
#     assert Parser(source).parse() == expected
    
# def test_013():
#     """Test 2-D array declaration and access"""
#     source = """func main() -> void { 
#         let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
#         let first_row = matrix[0];
#         let second_element = matrix[1][0];
#     }"""
#     expected = "success"
#     assert Parser(source).parse() == expected
    
# def test_014():
#     """Test array with illegal size declaration"""
#     source = """func main() -> void { 
#         let arr: [int; -1] = [1, 2, 3];  // Negative size is illegal
#     }"""
#     expected = "Error on line 2 col 23: -"
#     assert Parser(source).parse() == expected
    
# def test_015():
#     """Test missing arrow in function declaration"""
#     source = """
#     func add(a: int, b: int) { 
#         return a + b; 
#     }"""  # Missing '->'
#     expected = "Error on line 2 col 29: {"  
#     assert Parser(source).parse() == expected

from math import exp
from utils import Parser

def test_001():
    """Test empty program with main function"""
    source = """func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_002():
    """Test function with single parameter"""
    source = """func greet(name: string) -> void { print(name); }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_003():
    """Test multiple functions"""
    source = """
    func add(a: int, b: int) -> int { return a + b; }
    func main() -> void { let x = add(1, 2); }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_004():
    """Test missing main function"""
    source = """func helper() -> void {}"""
    expected = "success"  # Parser chỉ kiểm tra cú pháp
    assert Parser(source).parse() == expected

def test_005():
    """Test missing arrow in function declaration"""
    source = """func main() { }"""
    expected = "Error on line 1 col 12: {"
    assert Parser(source).parse() == expected

def test_006():
    """Test missing closing brace in function"""
    source = """func main() -> void { let x = 1; """
    expected = "Error on line 1 col 33: <EOF>"
    assert Parser(source).parse() == expected

def test_007():
    """Test invalid function name (starts with digit)"""
    source = """func 123main() -> void {}"""
    expected = "Error on line 1 col 5: 123"
    assert Parser(source).parse() == expected

def test_008():
    """Test function with void parameter"""
    source = """func test() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_009():
    """Test function with multiple return statements"""
    source = """
    func max(a: int, b: int) -> int {
        if (a > b) { return a; } else { return b; }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_010():
    """Test missing parameter type"""
    source = """func add(a, b: int) -> int { return a + b; }"""
    expected = "Error on line 1 col 10: ,"
    assert Parser(source).parse() == expected

def test_011():
    """Test constant declaration with explicit type"""
    source = """const MAX: int = 100; func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_012():
    """Test constant declaration with type inference"""
    source = """const PI = 3.14159; func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected

# def test_013():
#     """Test variable declaration with type inference"""
#     source = """func main() -> void { let x = 42; }"""
#     expected = "success"
#     assert Parser(source).parse() == expected

def test_013():
    source = """
            func sumArray(numbers: [int; 5]) -> int {
                let total = 0;
                for (num in numbers) {
                    total = total + num;
                }
                let s = "A";
                if ((total == 0) && numbers[0] == 0) {
                    s = "C";
                }
                else {
                    s = "B";
                }
                return s;
            }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_014():
    """Test variable declaration with explicit type"""
    source = """func main() -> void { 
        let name: string = "Alice";
        print(name);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_015():
    """Test missing initializer in variable declaration"""
    source = """func main() -> void { let x: int; }"""
    expected = "Error on line 1 col 32: ;"
    assert Parser(source).parse() == expected

def test_016():
    """Test missing initializer in constant declaration"""
    source = """const SIZE: int; func main() -> void {}"""
    expected = "Error on line 1 col 15: ;"
    assert Parser(source).parse() == expected

def test_017():
    """Test invalid type in variable declaration"""
    source = """func main() -> void { let x: integer = 42; }"""
    expected = "Error on line 1 col 29: integer"
    assert Parser(source).parse() == expected

def test_018():
    """Test multiple variable declarations in block"""
    source = """
    func main() -> void {
        let x = 1;
        let y: float = 2.5;
        let z = true;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_019():
    """Test missing semicolon in constant declaration"""
    source = """const PI: float = 3.14 func main() -> void {}"""
    expected = "Error on line 1 col 23: func"
    assert Parser(source).parse() == expected

def test_020():
    """Test invalid constant name (keyword)"""
    source = """const if: int = 42; func main() -> void {}"""
    expected = "Error on line 1 col 6: if"
    assert Parser(source).parse() == expected

def test_021():
    """Test arithmetic expression"""
    source = """func main() -> void { 
            let x = 5 + 3 * 2;
            ++x;
        }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_022():
    """Test comparison expression"""
    source = """func main() -> void { let b = 5 < 10; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_023():
    """Test logical expression"""
    source = """func main() -> void { let result = true && false || !true; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_024():
    """Test string concatenation"""
    source = """func main() -> void { let s = "Hello" + "World"; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_025():
    """Test unmatched parentheses in expression"""
    source = """func main() -> void { let x = (5 + 3 ; }"""
    expected = "Error on line 1 col 37: ;"
    assert Parser(source).parse() == expected

def test_026():
    """Test invalid operator in expression"""
    source = """func main() -> void { let x = 5 ** 2; }"""
    expected = "Error on line 1 col 33: *"
    assert Parser(source).parse() == expected
    
def test_027():
    """Test nested expressions"""
    source = """func main() -> void { let x = (5 + (3 * 2)) / 2; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_028():
    """Test function call expression"""
    source = """func add(a: int, b: int) -> int { return a + b; }
    func main() -> void { let x = add(5, 3); }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_029():
    """Test invalid function call (missing parentheses)"""
    source = """func main() -> void { let x = add 5, 3; }"""
    expected = "Error on line 1 col 34: 5"
    assert Parser(source).parse() == expected

def test_030():
    """Test unary operators"""
    source = """func main() -> void { let x = -5; let y = !true; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_031():
    """Test array declaration with explicit size"""
    source = """func main() -> void { let arr: [int; 3] = [1, 2, 3]; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_032():
    """Test array declaration with type inference"""
    source = """func main() -> void { let arr = [true, false]; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_033():
    """Test array access"""
    source = """func main() -> void { let arr = [1, 2, 3]; let x = arr[0]; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_034():
    """Test array assignment"""
    source = """func main() -> void { let arr = [1, 2, 3]; arr[1] = 42; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_035():
    """Test 3D array declaration"""
    source = """func main() -> void { let matrix: [[[int; 3]; 3]; 3] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_036():
    """Test 2D array access"""
    source = """func main() -> void { let matrix = [[1, 2], [3, 4]]; let x = matrix[0][1]; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_037():
    """Test invalid array size (negative)"""
    source = """func main() -> void { let arr: [int; -1] = []; }"""
    expected = "Error on line 1 col 37: -"
    assert Parser(source).parse() == expected

def test_038():
    """Test missing array closing bracket"""
    source = """func main() -> void { let arr = [1, 2, 3; }"""
    expected = "Error on line 1 col 40: ;"
    assert Parser(source).parse() == expected

def test_039():
    """Test empty array declaration"""
    source = """func main() -> void { let arr: [int; 0] = []; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_040():
    """Test invalid array index expression"""
    source = """func main() -> void { let arr = [1, 2, 3]; let x = arr[true]; }"""
    expected = "success"  # Parser không kiểm tra kiểu
    assert Parser(source).parse() == expected

def test_041():
    """Test simple if statement"""
    source = """func main() -> void { if (x > 0) { print("positive"); } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_042():
    """Test if-else statement"""
    source = """func main() -> void { if (x > 0) { print("positive"); } else { print("negative"); } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_043():
    """Test if-else if-else statement"""
    source = """
    func main() -> void {
        if (x > 0) { print("positive"); }
        else if (x == 0) { print("zero"); }
        else { print("negative"); }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_044():
    """Test missing condition parentheses"""
    source = """func main() -> void { if x > 0 { print("positive"); } }"""
    expected = "Error on line 1 col 25: x"
    assert Parser(source).parse() == expected

def test_045():
    """Test nested if statements"""
    source = """
    func main() -> void {
        if (x > 0) {
            if (x < 10) { print("single digit"); }
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_046():
    """Test missing else keyword"""
    source = """func main() -> void { if (x > 0) { print("positive"); } { print("negative"); } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_047():
    """Test complex condition expression"""
    source = """func main() -> void { if ((x > 0 && y < 10) || z) { print("valid"); } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_048():
    """Test empty if block"""
    source = """func main() -> void { if (x > 0) {} }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_049():
    """Test missing condition in if statement"""
    source = """func main() -> void { if () { print("error"); } }"""
    expected = "Error on line 1 col 26: )"
    assert Parser(source).parse() == expected

def test_050():
    """Test multiple else if clauses"""
    source = """
    func main() -> void {
        if (x == 1) { print("one"); }
        else if (x == 2) { print("two"); }
        else if (x == 3) { print("three"); }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_051():
    """Test simple while loop"""
    source = """func main() -> void { while (x < 5) { x = x + 1; } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_052():
    """Test for loop with array"""
    source = """func main() -> void { let arr = [1, 2, 3]; for (x in arr) { print(str(x)); } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_053():
    """Test nested while loops"""
    source = """
    func main() -> void {
        let i = 0;
        while (i < 3) {
            let j = 0;
            while (j < 2) { j = j + 1; }
            i = i + 1;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_054():
    """Test missing condition in while loop"""
    source = """func main() -> void { while () { x = x + 1; } }"""
    expected = "Error on line 1 col 29: )"
    assert Parser(source).parse() == expected

def test_055():
    """Test for loop with empty array"""
    source = """func main() -> void { let arr: [int; 0] = []; for (x in arr) {} }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_056():
    """Test invalid for loop variable"""
    source = """func main() -> void { for (123 in [1, 2, 3]) { print("error"); } }"""
    expected = "Error on line 1 col 27: 123"
    assert Parser(source).parse() == expected

def test_057():
    """Test break statement in while loop"""
    source = """func main() -> void { while (true) { break; } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_058():
    """Test continue statement in for loop"""
    source = """func main() -> void { for (x in [1, 2, 3]) { continue; } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_059():
    """Test missing in keyword in for loop"""
    source = """func main() -> void { for (x [1, 2, 3]) { print("error"); } }"""
    expected = "Error on line 1 col 29: ["
    assert Parser(source).parse() == expected

def test_060():
    """Test nested for loops with arrays"""
    source = """
    func main() -> void {
        let matrix = [[1, 2], [3, 4]];
        for (row in matrix) {
            for (elem in row) { print(str(elem)); }
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_061():
    """Test simple pipeline expression"""
    source = """func main() -> void { let x = 5 >> add(3); }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_062():
    """Test chained pipeline operators"""
    source = """func main() -> void { let x = data >> process >> transform; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_063():
    """Test pipeline with multiple arguments"""
    source = """func main() -> void { let x = "test" >> format("prefix", "suffix"); }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_064():
    """Test pipeline with invalid operator"""
    source = """func main() -> void { let x = data >>> process; }"""
    expected = "Error on line 1 col 37: >"
    assert Parser(source).parse() == expected

def test_065():
    """Test pipeline in complex expression"""
    source = """func main() -> void { let x = (5 + 3) >> multiply(2); }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_066():
    """Test pipeline with missing function call"""
    source = """func main() -> void { let x = data >> process; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_067():
    """Test pipeline with array transformation"""
    source = """func main() -> void { let x = [1, 2, 3] >> map(square); }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_068():
    """Test pipeline with parenthesized expression"""
    source = """func main() -> void { let x = (data >> filter) >> map(square); }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_069():
    """Test invalid pipeline operator syntax"""
    source = """func main() -> void { let x = data >> >> process; }"""
    expected = "Error on line 1 col 38: >>"
    assert Parser(source).parse() == expected

def test_070():
    """Test complex pipeline chain"""
    source = """
    func main() -> void {
        let result = numbers >> filter(isEven) >> map(square) >> reduce(add);
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_071():
    """Test integer literals"""
    source = """func main() -> void { let x = 42; let y = -17; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_072():
    """Test float literals"""
    source = """func main() -> void { let x = 3.14; let y = -2.5; let z = 0.0; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_073():
    """Test boolean literals"""
    source = """func main() -> void { let x = true; let y = false; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_074():
    """Test string literals with escape sequences"""
    source = """func main() -> void { let s = "Hello\\nWorld"; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_075():
    """Test function call with string literal"""
    source = """func print(msg: string) -> string {
        return msg;
    }
    func main() -> void { 
        let result = print("Hello, World!");
    }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_076():
    """Test empty string literal"""
    source = """func main() -> void { let s = ""; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_077():
    """Test missing comma in function parameter list"""
    source = """func add(a: int b: int) -> int { return a + b; }"""
    expected = "Error on line 1 col 16: b"
    assert Parser(source).parse() == expected

def test_078():
    """Test array literals with mixed types"""
    source = """func main() -> void { let arr = [1, "two", 3]; }"""
    expected = "success"  # Parser không kiểm tra kiểu
    assert Parser(source).parse() == expected

def test_079():
    """Test invalid type annotation"""
    source = """func main() -> void { let x: unknown = 42; }"""
    expected = "Error on line 1 col 29: unknown"
    assert Parser(source).parse() == expected

def test_080():
    """Test valid type annotations"""
    source = """
    func main() -> void {
        let x: int = 42;
        let y: float = 3.14;
        let z: bool = true;
        let s: string = "test";
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_081():
    """Test break statement in for loop"""
    source = """func main() -> void { for (x in [1, 2, 3]) { break; } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_082():
    """Test continue statement in while loop"""
    source = """func main() -> void { while (true) { continue; } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_083():
    """Test return statement with expression"""
    source = """func add(a: int, b: int) -> int { return a + b; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_084():
    """Test void return statement"""
    source = """func main() -> void { return; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_085():
    """Test block statement"""
    source = """func main() -> void { { let x = 1; } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_086():
    """Test break outside loop"""
    source = """func main() -> void { break; }"""
    expected = "success"  # Parser không kiểm tra ngữ nghĩa
    assert Parser(source).parse() == expected

def test_087():
    """Test continue outside loop"""
    source = """func main() -> void { continue; }"""
    expected = "success"  # Parser không kiểm tra ngữ nghĩa
    assert Parser(source).parse() == expected

def test_088():
    """Test nested block statements"""
    source = """
    func main() -> void {
        { let x = 1; { let y = 2; } }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_089():
    """Test function with multiple statements"""
    source = """
    func foo(a: int) -> int {
        if (a > 0) { return a; }
        else { return -a; }
    }
    func main() -> void {
        let x = 5;
        if (x > 0) { print("positive"); }
        else { print("negative"); }
        x = x + 1;
        let y = foo(x);
        print(str(y));
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_090():
    """Test complex control flow"""
    source = """
    func main() -> void {
        let x = 5;
        if (x > 0) {
            while (x > 0) {
                for (y in [1, 2, 3]) {
                    if (y == 2) { break; }
                }
                x = x - 1;
            }
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_091():
    """Test empty program"""
    source = """"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_092():
    """Test invalid keyword as identifier"""
    source = """func main() -> void { let func = 42; }"""
    expected = "Error on line 1 col 26: func"
    assert Parser(source).parse() == expected

def test_093():
    """Test multiple semicolons"""
    source = """func main() -> void { let x = 1;;; }"""
    # expected = "Error on line 1 col 32: ;"
    expected = "success" 
    assert Parser(source).parse() == expected

def test_094():
    """Test line comment"""
    source = """func main() -> void { // comment
        let x = 1;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_095():
    """Test block comment"""
    source = """func main() -> void { /* comment */ let x = 1; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_096():
    """Test missing closing brace in nested block"""
    source = """func main() -> void { if (x > 0) { let y = 1; }"""
    expected = "Error on line 1 col 47: <EOF>"
    assert Parser(source).parse() == expected

def test_097():
    """Test built-in function calls"""
    source = """func main() -> void { print("test"); let x = str(42); }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_098():
    """Test mixing types in array"""
    source = """func main() -> void { let arr = [1, "two", 3.0]; }"""
    expected = "success" 
    assert Parser(source).parse() == expected

def test_099():
    """Test complex program structure"""
    source = """
    const MAX: int = 100;
    func add(a: int, b: int) -> int { return a + b; }
    func main() -> void {
        let x = [1, 2, 3] >> map(add(1));
        if (x[0] > 0) {
            for (n in x) {
                print(str(n));
            }
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_100():
    """Test missing semicolon after expression statement"""
    source = """func main() -> void { x = 5 }"""
    expected = "Error on line 1 col 28: }"
    assert Parser(source).parse() == expected

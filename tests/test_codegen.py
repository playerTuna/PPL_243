from src.utils.nodes import *
from utils import CodeGenerator

def test_001():
    """Test basic print statement"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"), [StringLiteral("Hello World")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_002():
    ast = Program(
        [],
        [
            FuncDecl(
                "sum_array",
                [Param("arr", ArrayType(IntType(), 5))],
                IntType(),
                [
                    VarDecl("total", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "x",
                        Identifier("arr"),
                        BlockStmt([
                            Assignment(IdLValue("total"), BinaryOp(Identifier("total"), "+", Identifier("x")))
                        ])
                    ),
                    ReturnStmt(Identifier("total"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 5), ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)])),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("int2str"), [FunctionCall(Identifier("sum_array"), [Identifier("arr")])])]))
                ]
            )
        ]
    )
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_003():
    ast = Program(
        [
            ConstDecl(
                "NUMS",
                ArrayType(IntType(), 3),
                ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])
            )
        ],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ForStmt(
                        "i",
                        Identifier("NUMS"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("i")])]
                                )
                            )
                        ])
                    )
                ]
            )
        ]
    )
    expected = "1\n2\n3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_004():
    """Test variable declaration and binary operations"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(10)),
                    VarDecl("b", IntType(), IntegerLiteral(5)),
                    VarDecl("result", IntType(), BinaryOp(Identifier("a"), "+", Identifier("b"))),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("int2str"), [Identifier("result")])]))
                ]
            )
        ]
    )
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_005():
    """Test if-else statement"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(10)),
                    IfStmt(
                        BinaryOp(Identifier("x"), ">", IntegerLiteral(5)),
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("x is greater than 5")]))
                        ]),
                        [],
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("x is not greater than 5")]))
                        ])
                    )
                ]
            )
        ]
    )
    expected = "x is greater than 5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_006():
    """Test while loop"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("i", IntType(), IntegerLiteral(1)),
                    VarDecl("sum", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<=", IntegerLiteral(5)),
                        BlockStmt([
                            Assignment(IdLValue("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i"))),
                            Assignment(IdLValue("i"), BinaryOp(Identifier("i"), "+", IntegerLiteral(1)))
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("int2str"), [Identifier("sum")])]))
                ]
            )
        ]
    )
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_007():
    """Test nested function calls"""
    ast = Program(
        [],
        [
            FuncDecl(
                "square",
                [Param("x", IntType())],
                IntType(),
                [
                    ReturnStmt(BinaryOp(Identifier("x"), "*", Identifier("x")))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(FunctionCall(
                        Identifier("print"), 
                        [FunctionCall(
                            Identifier("int2str"), 
                            [FunctionCall(Identifier("square"), [IntegerLiteral(4)])]
                        )]
                    ))
                ]
            )
        ]
    )
    expected = "16"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_008():
    """Test string concatenation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("firstName", StringType(), StringLiteral("Hello")),
                    VarDecl("lastName", StringType(), StringLiteral("World")),
                    VarDecl("fullName", StringType(), BinaryOp(Identifier("firstName"), "+", Identifier("lastName"))),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("fullName")]))
                ]
            )
        ]
    )
    expected = "HelloWorld"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_009():
    """Test factorial computed with a while‐loop instead of recursion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("n", IntType(), IntegerLiteral(5)),
                    VarDecl("result", IntType(), IntegerLiteral(1)),
                    WhileStmt(
                        BinaryOp(Identifier("n"), ">", IntegerLiteral(1)),
                        BlockStmt([
                            Assignment(
                                IdLValue("result"),
                                BinaryOp(Identifier("result"), "*", Identifier("n"))
                            ),
                            Assignment(
                                IdLValue("n"),
                                BinaryOp(Identifier("n"), "-", IntegerLiteral(1))
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "120"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_010():
    """Test global constants with computation"""
    ast = Program(
        [
            ConstDecl("PI", FloatType(), FloatLiteral(3.14)),
            ConstDecl("RADIUS", FloatType(), FloatLiteral(2.0))
        ],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("area", FloatType(), BinaryOp(
                        BinaryOp(Identifier("PI"), "*", Identifier("RADIUS")),
                        "*", 
                        Identifier("RADIUS")
                    )),
                    ExprStmt(FunctionCall(
                        Identifier("print"), 
                        [FunctionCall(Identifier("float2str"), [Identifier("area")])]
                    ))
                ]
            )
        ]
    )
    expected = "12.56"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_011():
    """Test array element assignment"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "arr", 
                        ArrayType(IntType(), 3), 
                        ArrayLiteral([
                            IntegerLiteral(1), 
                            IntegerLiteral(2), 
                            IntegerLiteral(3)
                        ])
                    ),
                    Assignment(
                        ArrayAccessLValue(
                            Identifier("arr"), 
                            IntegerLiteral(1)
                        ), 
                        IntegerLiteral(99)
                    ),
                    ForStmt(
                        "i",
                        Identifier("arr"),
                        BlockStmt([
                            ExprStmt(FunctionCall(
                                Identifier("print"), 
                                [FunctionCall(Identifier("int2str"), [Identifier("i")])]
                            ))
                        ])
                    )
                ]
            )
        ]
    )
    expected = "1\n99\n3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_012():
    """Test recursive function (factorial)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "factorial",
                [Param("n", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "<=", IntegerLiteral(1)),
                        BlockStmt([ReturnStmt(IntegerLiteral(1))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    Identifier("n"),
                                    "*",
                                    FunctionCall(
                                        Identifier("factorial"),
                                        [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                    )
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"),
                                [FunctionCall(Identifier("factorial"), [IntegerLiteral(5)])]
                            )]
                        )
                    )
                ]
            )
        ]
    )
    expected = "120"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_013():
    """Test nested loops with break statement"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", StringType(), StringLiteral("")),
                    VarDecl("i", IntType(), IntegerLiteral(1)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<=", IntegerLiteral(3)),
                        BlockStmt([
                            VarDecl("j", IntType(), IntegerLiteral(1)),
                            WhileStmt(
                                BinaryOp(Identifier("j"), "<=", IntegerLiteral(3)),
                                BlockStmt([
                                    Assignment(
                                        IdLValue("result"),
                                        BinaryOp(
                                            Identifier("result"),
                                            "+",
                                            BinaryOp(
                                                FunctionCall(Identifier("int2str"), [Identifier("i")]),
                                                "+",
                                                BinaryOp(
                                                    StringLiteral(","),
                                                    "+",
                                                    FunctionCall(Identifier("int2str"), [Identifier("j")])
                                                )
                                            )
                                        )
                                    ),
                                    Assignment(
                                        IdLValue("result"),
                                        BinaryOp(Identifier("result"), "+", StringLiteral(";"))
                                    ),
                                    IfStmt(
                                        BinaryOp(
                                            BinaryOp(Identifier("i"), "==", IntegerLiteral(2)),
                                            "&&",
                                            BinaryOp(Identifier("j"), "==", IntegerLiteral(2))
                                        ),
                                        BlockStmt([BreakStmt()]),
                                        [],
                                        None
                                    ),
                                    Assignment(
                                        IdLValue("j"),
                                        BinaryOp(Identifier("j"), "+", IntegerLiteral(1))
                                    )
                                ])
                            ),
                            Assignment(
                                IdLValue("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("result")]))
                ]
            )
        ]
    )
    expected = "1,1;1,2;1,3;2,1;2,2;3,1;3,2;3,3;"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_014():
    """Test multiple return paths in a function"""
    ast = Program(
        [],
        [
            FuncDecl(
                "grade",
                [Param("score", IntType())],
                StringType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("score"), ">=", IntegerLiteral(90)),
                        BlockStmt([ReturnStmt(StringLiteral("A"))]),
                        [
                            (
                                BinaryOp(Identifier("score"), ">=", IntegerLiteral(80)),
                                BlockStmt([ReturnStmt(StringLiteral("B"))])
                            ),
                            (
                                BinaryOp(Identifier("score"), ">=", IntegerLiteral(70)),
                                BlockStmt([ReturnStmt(StringLiteral("C"))])
                            ),
                            (
                                BinaryOp(Identifier("score"), ">=", IntegerLiteral(60)),
                                BlockStmt([ReturnStmt(StringLiteral("D"))])
                            )
                        ],
                        BlockStmt([ReturnStmt(StringLiteral("F"))])
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("grade"), [IntegerLiteral(85)])]
                    ))
                ]
            )
        ]
    )
    expected = "B"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_015():
    """Test mixed type operations (int and float)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("intVal", IntType(), IntegerLiteral(5)),
                    VarDecl("floatVal", FloatType(), FloatLiteral(2.5)),
                    VarDecl("result", FloatType(), BinaryOp(Identifier("intVal"), "+", Identifier("floatVal"))),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("float2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "7.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_016():
    """Test boolean operations and conditional execution"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", BoolType(), BooleanLiteral(True)),
                    VarDecl("b", BoolType(), BooleanLiteral(False)),
                    VarDecl("c", BoolType(), BooleanLiteral(True)),
                    VarDecl("result1", BoolType(), BinaryOp(
                        BinaryOp(Identifier("a"), "&&", Identifier("b")),
                        "||",
                        Identifier("c")
                    )),
                    VarDecl("result2", BoolType(), BinaryOp(
                        Identifier("a"),
                        "&&",
                        BinaryOp(Identifier("b"), "||", Identifier("c"))
                    )),
                    IfStmt(
                        Identifier("result1"),
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Result1: True")]))
                        ]),
                        [],
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Result1: False")]))
                        ])
                    ),
                    IfStmt(
                        Identifier("result2"),
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Result2: True")]))
                        ]),
                        [],
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Result2: False")]))
                        ])
                    )
                ]
            )
        ]
    )
    expected = "Result1: True\nResult2: True"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_017():
    """Test continue statement in a loop"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    VarDecl("result", StringType(), StringLiteral("")),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<", IntegerLiteral(10)),
                        BlockStmt([
                            Assignment(
                                IdLValue("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))
                            ),
                            IfStmt(
                                BinaryOp(
                                    BinaryOp(Identifier("i"), "%", IntegerLiteral(2)),
                                    "==",
                                    IntegerLiteral(0)
                                ),
                                BlockStmt([ContinueStmt()]),
                                [],
                                None
                            ),
                            Assignment(
                                IdLValue("result"),
                                BinaryOp(
                                    Identifier("result"),
                                    "+",
                                    BinaryOp(
                                        FunctionCall(Identifier("int2str"), [Identifier("i")]),
                                        "+",
                                        StringLiteral(",")
                                    )
                                )
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("result")]))
                ]
            )
        ]
    )
    expected = "1,3,5,7,9,"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_018():
    """Test nested function calls with multiple parameters"""
    ast = Program(
        [],
        [
            FuncDecl(
                "max",
                [Param("a", IntType()), Param("b", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("a"), ">", Identifier("b")),
                        BlockStmt([ReturnStmt(Identifier("a"))]),
                        [],
                        BlockStmt([ReturnStmt(Identifier("b"))])
                    )
                ]
            ),
            FuncDecl(
                "min",
                [Param("a", IntType()), Param("b", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("a"), "<", Identifier("b")),
                        BlockStmt([ReturnStmt(Identifier("a"))]),
                        [],
                        BlockStmt([ReturnStmt(Identifier("b"))])
                    )
                ]
            ),
            FuncDecl(
                "sum",
                [Param("a", IntType()), Param("b", IntType())],
                IntType(),
                [
                    ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(10)),
                    VarDecl("y", IntType(), IntegerLiteral(20)),
                    VarDecl("z", IntType(), IntegerLiteral(5)),
                    VarDecl("result", IntType(), FunctionCall(
                        Identifier("sum"),
                        [
                            FunctionCall(Identifier("max"), [Identifier("x"), Identifier("y")]),
                            FunctionCall(Identifier("min"), [Identifier("y"), Identifier("z")])
                        ]
                    )),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "25"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_019():
    """Test Pipeline operator (let result = num >> getSquare)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "getSquare",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "*", Identifier("x")))]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("num", IntType(), IntegerLiteral(4)),
                    VarDecl(
                        "result",
                        IntType(),
                        BinaryOp(Identifier("num"), ">>", Identifier("getSquare"))
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "16"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_020():
    """Test multi string concat"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("tinhieu1", StringType(), StringLiteral("Len phim ")),
                    VarDecl("tinhieu2", IntType(), IntegerLiteral(36)),
                    VarDecl("tinhieu3", StringType(), StringLiteral("duyet binh o ")),
                    VarDecl("tinhieu4", IntType(), IntegerLiteral(120)),
                    VarDecl("tinhieu5", StringType(), StringLiteral(" Yen Lang")),
                    VarDecl("combined", StringType(), BinaryOp(
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(
                                    BinaryOp(Identifier("tinhieu1"), "+", FunctionCall(Identifier("int2str"), [Identifier("tinhieu2")])),
                                    "+",
                                    StringLiteral(" ")
                                ),
                                "+",
                                Identifier("tinhieu3")
                            ),
                            "+",
                            FunctionCall(Identifier("int2str"), [Identifier("tinhieu4")])
                        ),
                        "+",
                        Identifier("tinhieu5")
                    )),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("combined")]))
                ]
            )
        ]
    )
    expected = "Len phim 36 duyet binh o 120 Yen Lang"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_021():
    """Test nested multidimensional arrays"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "matrix", 
                        ArrayType(ArrayType(IntType(), 3), 2), 
                        ArrayLiteral([
                            ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]),
                            ArrayLiteral([IntegerLiteral(4), IntegerLiteral(5), IntegerLiteral(6)])
                        ])
                    ),
                    VarDecl("sum", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "row",
                        Identifier("matrix"),
                        BlockStmt([
                            ForStmt(
                                "element",
                                Identifier("row"),
                                BlockStmt([
                                    Assignment(
                                        IdLValue("sum"), 
                                        BinaryOp(Identifier("sum"), "+", Identifier("element"))
                                    )
                                ])
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                    ))
                ]
            )
        ]
    )
    expected = "21"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_022():
    """Test string escape sequences"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "text", 
                        StringType(), 
                        StringLiteral("Line1\\nLine2\\tTabbed\\\"Quoted\\\"\\\\Backslash")
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("text")]))
                ]
            )
        ]
    )
    expected = "Line1\nLine2\tTabbed\"Quoted\"\\Backslash"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_023():
    """Test complex pipeline operator chaining"""
    ast = Program(
        [],
        [
            FuncDecl(
                "double",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "*", IntegerLiteral(2)))]
            ),
            FuncDecl(
                "increment",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", IntegerLiteral(1)))]
            ),
            FuncDecl(
                "square",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "*", Identifier("x")))]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "result",
                        IntType(),
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(IntegerLiteral(5), ">>", Identifier("increment")),
                                ">>",
                                Identifier("double")
                            ),
                            ">>",
                            Identifier("square")
                        )
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "144"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_024():
    """Test recursive function with multiple base cases (Fibonacci)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "fibonacci",
                [Param("n", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "<=", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(IntegerLiteral(0))]),
                        [
                            (
                                BinaryOp(Identifier("n"), "==", IntegerLiteral(1)),
                                BlockStmt([ReturnStmt(IntegerLiteral(1))])
                            )
                        ],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    FunctionCall(
                                        Identifier("fibonacci"),
                                        [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                    ),
                                    "+",
                                    FunctionCall(
                                        Identifier("fibonacci"),
                                        [BinaryOp(Identifier("n"), "-", IntegerLiteral(2))]
                                    )
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("n", IntType(), IntegerLiteral(10)),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [
                            FunctionCall(Identifier("fibonacci"), [Identifier("n")])
                        ])]
                    ))
                ]
            )
        ]
    )
    expected = "55"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_025():
    """Test array bounds and complex indexing"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "arr",
                        ArrayType(IntType(), 10),
                        ArrayLiteral([
                            IntegerLiteral(10),
                            IntegerLiteral(20),
                            IntegerLiteral(30),
                            IntegerLiteral(40),
                            IntegerLiteral(50),
                            IntegerLiteral(60),
                            IntegerLiteral(70),
                            IntegerLiteral(80),
                            IntegerLiteral(90),
                            IntegerLiteral(100),
                            IntegerLiteral(30)
                        ])
                    ),
                    VarDecl("index", IntType(), IntegerLiteral(2)),
                    VarDecl(
                        "value",
                        IntType(),
                        ArrayAccess(Identifier("arr"), Identifier("index"))
                    ),
                    VarDecl(
                        "nestedValue",
                        IntType(),
                        ArrayAccess(
                            Identifier("arr"),
                            ArrayAccess(Identifier("arr"), IntegerLiteral(0))
                        )
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"), 
                        [
                            BinaryOp(
                                FunctionCall(Identifier("int2str"), [Identifier("value")]),
                                "+",
                                BinaryOp(
                                    StringLiteral(","),
                                    "+",
                                    FunctionCall(Identifier("int2str"), [Identifier("nestedValue")])
                                )
                            )
                        ]
                    ))
                ]
            )
        ]
    )
    expected = "30,30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_026():
    """Test deeply nested control flow structures"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", StringType(), StringLiteral("")),
                    VarDecl("x", IntType(), IntegerLiteral(5)),
                    IfStmt(
                        BinaryOp(Identifier("x"), ">", IntegerLiteral(0)),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(Identifier("x"), "<", IntegerLiteral(10)),
                                BlockStmt([
                                    ForStmt(
                                        "i",
                                        ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]),
                                        BlockStmt([
                                            WhileStmt(
                                                BinaryOp(Identifier("i"), ">", IntegerLiteral(0)),
                                                BlockStmt([
                                                    Assignment(
                                                        IdLValue("result"),
                                                        BinaryOp(
                                                            Identifier("result"),
                                                            "+",
                                                            FunctionCall(Identifier("int2str"), [Identifier("i")])
                                                        )
                                                    ),
                                                    Assignment(
                                                        IdLValue("i"),
                                                        BinaryOp(Identifier("i"), "-", IntegerLiteral(1))
                                                    )
                                                ])
                                            )
                                        ])
                                    )
                                ]),
                                [],
                                None
                            )
                        ]),
                        [],
                        None
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("result")]))
                ]
            )
        ]
    )
    expected = "121321"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_027():
    """Test complex type coercion in arithmetic expressions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("intVal", IntType(), IntegerLiteral(5)),
                    VarDecl("floatVal", FloatType(), FloatLiteral(2.5)),
                    VarDecl(
                        "result1",
                        FloatType(),
                        BinaryOp(
                            BinaryOp(Identifier("intVal"), "+", Identifier("floatVal")),
                            "*",
                            BinaryOp(Identifier("floatVal"), "-", IntegerLiteral(1))
                        )
                    ),
                    VarDecl(
                        "result2",
                        FloatType(),
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(Identifier("intVal"), "*", Identifier("floatVal")),
                                "/",
                                IntegerLiteral(2)
                            ),
                            "+",
                            BinaryOp(
                                IntegerLiteral(3),
                                "%",
                                IntegerLiteral(2)
                            )
                        )
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [
                            BinaryOp(
                                FunctionCall(Identifier("float2str"), [Identifier("result1")]),
                                "+",
                                BinaryOp(
                                    StringLiteral(","),
                                    "+",
                                    FunctionCall(Identifier("float2str"), [Identifier("result2")])
                                )
                            )
                        ]
                    ))
                ]
            )
        ]
    )
    expected = "11.25,7.25"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_028():
    """Test multiple conditional early returns in a function"""
    ast = Program(
        [],
        [
            FuncDecl(
                "findCategory",
                [Param("value", IntType())],
                StringType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("value"), "<", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(StringLiteral("negative"))]),
                        [],
                        None
                    ),
                    IfStmt(
                        BinaryOp(Identifier("value"), "==", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(StringLiteral("zero"))]),
                        [],
                        None
                    ),
                    IfStmt(
                        BinaryOp(Identifier("value"), "<", IntegerLiteral(10)),
                        BlockStmt([ReturnStmt(StringLiteral("small"))]),
                        [],
                        None
                    ),
                    IfStmt(
                        BinaryOp(Identifier("value"), "<", IntegerLiteral(100)),
                        BlockStmt([ReturnStmt(StringLiteral("medium"))]),
                        [],
                        None
                    ),
                    ReturnStmt(StringLiteral("large"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "values",
                        ArrayType(IntType(), 5),
                        ArrayLiteral([
                            IntegerLiteral(-5),
                            IntegerLiteral(0),
                            IntegerLiteral(5),
                            IntegerLiteral(50),
                            IntegerLiteral(500)
                        ])
                    ),
                    VarDecl("result", StringType(), StringLiteral("")),
                    ForStmt(
                        "val",
                        Identifier("values"),
                        BlockStmt([
                            Assignment(
                                IdLValue("result"),
                                BinaryOp(
                                    Identifier("result"),
                                    "+",
                                    BinaryOp(
                                        FunctionCall(Identifier("findCategory"), [Identifier("val")]),
                                        "+",
                                        StringLiteral(",")
                                    )
                                )
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("result")]))
                ]
            )
        ]
    )
    expected = "negative,zero,small,medium,large,"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_029():
    """Test mutual recursion between functions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "isEven",
                [Param("n", IntType())],
                BoolType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "==", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(BooleanLiteral(True))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                FunctionCall(
                                    Identifier("isOdd"),
                                    [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "isOdd",
                [Param("n", IntType())],
                BoolType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "==", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(BooleanLiteral(False))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                FunctionCall(
                                    Identifier("isEven"),
                                    [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", StringType(), StringLiteral("")),
                    ForStmt(
                        "i",
                        ArrayLiteral([
                            IntegerLiteral(1),
                            IntegerLiteral(2),
                            IntegerLiteral(3),
                            IntegerLiteral(4),
                            IntegerLiteral(5)
                        ]),
                        BlockStmt([
                            IfStmt(
                                FunctionCall(Identifier("isEven"), [Identifier("i")]),
                                BlockStmt([
                                    Assignment(
                                        IdLValue("result"),
                                        BinaryOp(
                                            Identifier("result"),
                                            "+",
                                            BinaryOp(
                                                FunctionCall(Identifier("int2str"), [Identifier("i")]),
                                                "+",
                                                StringLiteral("-even;")
                                            )
                                        )
                                    )
                                ]),
                                [],
                                BlockStmt([
                                    Assignment(
                                        IdLValue("result"),
                                        BinaryOp(
                                            Identifier("result"),
                                            "+",
                                            BinaryOp(
                                                FunctionCall(Identifier("int2str"), [Identifier("i")]),
                                                "+",
                                                StringLiteral("-odd;")
                                            )
                                        )
                                    )
                                ])
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("result")]))
                ]
            )
        ]
    )
    expected = "1-odd;2-even;3-odd;4-even;5-odd;"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_030():
    """Test string concat with a String type and any type"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", StringType(), StringLiteral("Hello")),
                    VarDecl("b", BoolType(), BooleanLiteral(True)),
                    VarDecl("c", FloatType(), FloatLiteral(3.14)),
                    ExprStmt(BinaryOp(Identifier("a"), "+", Identifier("b"))),
                    ExprStmt(BinaryOp(Identifier("a"), "+", Identifier("c"))),
                    ExprStmt(FunctionCall(Identifier("print"), [BinaryOp(Identifier("a"), "+", Identifier("b"))])),
                    ExprStmt(FunctionCall(Identifier("print"), [BinaryOp(Identifier("a"), "+", Identifier("c"))]))
                ]
            )
        ]
    )
    expected = "Hellotrue\nHello3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_031():
    """Numeric promotion + pipeline chaining"""
    ast = Program(
        [],
        [
            FuncDecl(
                "double",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "*", IntegerLiteral(2)))]
            ),
            FuncDecl(
                "addFloat",
                [Param("x", FloatType())],
                FloatType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", FloatLiteral(2.5)))]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "v",
                        FloatType(),
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(IntegerLiteral(5), ">>", Identifier("double")),
                                "+",
                                FloatLiteral(3.5)
                            ),
                            ">>",
                            Identifier("addFloat")
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("v")])]
                        )
                    )
                ]
            )
        ]
    )
    expected = "16.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_032():
    """String concatenation with mixed types"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl(
                        "msg",
                        StringType(),
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(
                                    BinaryOp(
                                        StringLiteral("Start:"),
                                        "+",
                                        IntegerLiteral(1)
                                    ),
                                    "+",
                                    StringLiteral(" ")
                                ),
                                "+",
                                FloatLiteral(2.5)
                            ),
                            "+",
                            BinaryOp(StringLiteral(" "), "+", BooleanLiteral(True))
                        )
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("msg")]))
                ]
            )
        ]
    )
    expected = "Start:1 2.5 true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_033():
    """Parameter immutability"""
    ast = Program(
        [],
        [
            FuncDecl(
                "sumArr",
                [Param("a", ArrayType(IntType(), 5))],
                IntType(),
                [
                    VarDecl("s", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "x",
                        Identifier("a"),
                        BlockStmt([
                            Assignment(
                                IdLValue("s"),
                                BinaryOp(Identifier("s"), "+", Identifier("x"))
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("s"))
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl(
                        "data",
                        ArrayType(IntType(), 5),
                        ArrayLiteral([
                            IntegerLiteral(2),
                            IntegerLiteral(4),
                            IntegerLiteral(6),
                            IntegerLiteral(8),
                            IntegerLiteral(10)
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(
                            Identifier("int2str"),
                            [FunctionCall(Identifier("sumArr"), [Identifier("data")])]
                        )]
                    ))
                ]
            )
        ]
    )
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_034():
    """String parameter read-only concatenation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "wrap",
                [Param("s", StringType())],
                StringType(),
                [
                    VarDecl("prefix", StringType(), StringLiteral("[[")),
                    VarDecl("suffix", StringType(), StringLiteral("]]")),
                    ReturnStmt(
                        BinaryOp(
                            BinaryOp(Identifier("prefix"), "+", Identifier("s")),
                            "+",
                            Identifier("suffix")
                        )
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("base", StringType(), StringLiteral("HLang")),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("wrap"), [Identifier("base")])]
                    ))
                ]
            )
        ]
    )
    expected = "[[HLang]]"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_035():
    """Pipeline chaining across numeric + float promotion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "inc",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", IntegerLiteral(1)))]
            ),
            FuncDecl(
                "toFloatAdd",
                [Param("x", IntType())],
                FloatType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", FloatLiteral(0.5)))]
            ),
            FuncDecl(
                "mul2f",
                [Param("f", FloatType())],
                FloatType(),
                [ReturnStmt(BinaryOp(Identifier("f"), "*", FloatLiteral(2.0)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl(
                        "res",
                        FloatType(),
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(IntegerLiteral(7), ">>", Identifier("inc")),
                                ">>",
                                Identifier("toFloatAdd")
                            ),
                            ">>",
                            Identifier("mul2f")
                        )
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("float2str"), [Identifier("res")])]
                    ))
                ]
            )
        ]
    )
    expected = "17.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_036():
    """Sum elements of 2D array passed as parameter (immutable)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "sum2D",
                [Param("m", ArrayType(ArrayType(IntType(), 3), 2))],
                IntType(),
                [
                    VarDecl("total", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "row",
                        Identifier("m"),
                        BlockStmt([
                            ForStmt(
                                "cell",
                                Identifier("row"),
                                BlockStmt([
                                    Assignment(
                                        IdLValue("total"),
                                        BinaryOp(Identifier("total"), "+", Identifier("cell"))
                                    )
                                ])
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("total"))
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl(
                        "mat",
                        ArrayType(ArrayType(IntType(), 3), 2),
                        ArrayLiteral([
                            ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]),
                            ArrayLiteral([IntegerLiteral(4), IntegerLiteral(5), IntegerLiteral(6)])
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(
                            Identifier("int2str"),
                            [FunctionCall(Identifier("sum2D"), [Identifier("mat")])]
                        )]
                    ))
                ]
            )
        ]
    )
    expected = "21"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_037():
    """Mutual recursion counting down (parameters immutable)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "fA",
                [Param("n", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "==", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(IntegerLiteral(1))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    Identifier("n"),
                                    "+",
                                    FunctionCall(
                                        Identifier("fB"),
                                        [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                    )
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "fB",
                [Param("n", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "==", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(IntegerLiteral(0))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                FunctionCall(
                                    Identifier("fA"),
                                    [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(
                            Identifier("int2str"),
                            [FunctionCall(Identifier("fA"), [IntegerLiteral(5)])]
                        )]
                    ))
                ]
            )
        ]
    )
    expected = "9"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_038():
    """Linear search function returns index or -1; array immutable"""
    ast = Program(
        [],
        [
            FuncDecl(
                "find",
                [Param("arr", ArrayType(IntType(), 6)), Param("target", IntType())],
                IntType(),
                [
                    VarDecl("idx", IntType(), IntegerLiteral(0)),
                    VarDecl("ans", IntType(), IntegerLiteral(-1)),
                    WhileStmt(
                        BinaryOp(Identifier("idx"), "<", IntegerLiteral(6)),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(
                                    ArrayAccess(Identifier("arr"), Identifier("idx")),
                                    "==",
                                    Identifier("target")
                                ),
                                BlockStmt([
                                    Assignment(IdLValue("ans"), Identifier("idx")),
                                    BreakStmt()
                                ]),
                                [],
                                None
                            ),
                            Assignment(
                                IdLValue("idx"),
                                BinaryOp(Identifier("idx"), "+", IntegerLiteral(1))
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("ans"))
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl(
                        "data",
                        ArrayType(IntType(), 6),
                        ArrayLiteral([
                            IntegerLiteral(3),
                            IntegerLiteral(8),
                            IntegerLiteral(2),
                            IntegerLiteral(7),
                            IntegerLiteral(9),
                            IntegerLiteral(5)
                        ])
                    ),
                    VarDecl("pos", IntType(),
                            FunctionCall(Identifier("find"), [Identifier("data"), IntegerLiteral(7)])),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("pos")])]
                    ))
                ]
            )
        ]
    )
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_039():
    """Tail-recursive style factorial with accumulator parameter (not mutated)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "factAcc",
                [Param("n", IntType()), Param("acc", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "<=", IntegerLiteral(1)),
                        BlockStmt([ReturnStmt(Identifier("acc"))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                FunctionCall(
                                    Identifier("factAcc"),
                                    [
                                        BinaryOp(Identifier("n"), "-", IntegerLiteral(1)),
                                        BinaryOp(Identifier("acc"), "*", Identifier("n"))
                                    ]
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(
                            Identifier("int2str"),
                            [FunctionCall(Identifier("factAcc"), [IntegerLiteral(5), IntegerLiteral(1)])]
                        )]
                    ))
                ]
            )
        ]
    )
    expected = "120"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_040():
    """Short-circuit OR prevents evaluation of expensive branch"""
    ast = Program(
        [],
        [
            FuncDecl(
                "expensive",
                [Param("x", IntType())],
                IntType(),
                [
                    ReturnStmt(BinaryOp(Identifier("x"), "*", IntegerLiteral(100)))
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("flag", BoolType(), BooleanLiteral(True)),
                    VarDecl("val", IntType(), IntegerLiteral(5)),
                    VarDecl(
                        "result",
                        BoolType(),
                        BinaryOp(Identifier("flag"), "||",
                                 BinaryOp(
                                     FunctionCall(Identifier("expensive"), [Identifier("val")]),
                                     "==",
                                     IntegerLiteral(500)
                                 ))
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("bool2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_041():
    """Complex nested pipelines with arithmetic + float promotion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "add3",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", IntegerLiteral(3)))]
            ),
            FuncDecl(
                "half",
                [Param("x", IntType())],
                FloatType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "/", FloatLiteral(2.0)))]
            ),
            FuncDecl(
                "neg",
                [Param("f", FloatType())],
                FloatType(),
                [ReturnStmt(BinaryOp(FloatLiteral(0.0), "-", Identifier("f")))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl(
                        "ans",
                        FloatType(),
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(IntegerLiteral(10), ">>", Identifier("add3")),
                                ">>",
                                Identifier("half")
                            ),
                            ">>",
                            Identifier("neg")
                        )
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("float2str"), [Identifier("ans")])]
                    ))
                ]
            )
        ]
    )
    expected = "-6.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_042():
    """Boolean expression mixing comparisons and arithmetic precedence"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl(
                        "b",
                        BoolType(),
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(IntegerLiteral(4), "*", IntegerLiteral(5)),
                                "==",
                                IntegerLiteral(20)
                            ),
                            "&&",
                            BinaryOp(
                                BinaryOp(IntegerLiteral(9), "%", IntegerLiteral(4)),
                                "==",
                                IntegerLiteral(1)
                            )
                        )
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("bool2str"), [Identifier("b")])]
                    ))
                ]
            )
        ]
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_043():
    """Global constants + recursion without mutation"""
    ast = Program(
        [
            ConstDecl("BASE", IntType(), IntegerLiteral(2))
        ],
        [
            FuncDecl(
                "pow2",
                [Param("n", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "==", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(IntegerLiteral(1))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    Identifier("BASE"),
                                    "*",
                                    FunctionCall(
                                        Identifier("pow2"),
                                        [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                    )
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(
                            Identifier("int2str"),
                            [FunctionCall(Identifier("pow2"), [IntegerLiteral(5)])]
                        )]
                    ))
                ]
            )
        ]
    )
    expected = "32"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_044():
    """Function returning boolean from complex parameter usage (no mutation)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "inRange",
                [Param("x", IntType()), Param("low", IntType()), Param("high", IntType())],
                BoolType(),
                [
                    ReturnStmt(
                        BinaryOp(
                            BinaryOp(Identifier("x"), ">=", Identifier("low")),
                            "&&",
                            BinaryOp(Identifier("x"), "<=", Identifier("high"))
                        )
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(
                            Identifier("bool2str"),
                            [FunctionCall(Identifier("inRange"),
                                          [IntegerLiteral(15), IntegerLiteral(10), IntegerLiteral(20)])]
                        )]
                    ))
                ]
            )
        ]
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_045():
    """Multiple prints mixing types and conversions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("i", IntType(), IntegerLiteral(7)),
                    VarDecl("f", FloatType(), FloatLiteral(2.25)),
                    VarDecl("b", BoolType(), BooleanLiteral(False)),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [BinaryOp(StringLiteral("i="), "+",
                                  FunctionCall(Identifier("int2str"), [Identifier("i")]))]
                    )),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [BinaryOp(StringLiteral("f="), "+",
                                  FunctionCall(Identifier("float2str"), [Identifier("f")]))]
                    )),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [BinaryOp(StringLiteral("b="), "+",
                                  FunctionCall(Identifier("bool2str"), [Identifier("b")]))]
                    ))
                ]
            )
        ]
    )
    expected = "i=7\nf=2.25\nb=false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_046():
    """Nested for with continue skipping even numbers"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("nums", ArrayType(IntType(), 6),
                            ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3),
                                          IntegerLiteral(4), IntegerLiteral(5), IntegerLiteral(6)])),
                    VarDecl("out", StringType(), StringLiteral("")),
                    ForStmt(
                        "n",
                        Identifier("nums"),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(
                                    BinaryOp(Identifier("n"), "%", IntegerLiteral(2)),
                                    "==",
                                    IntegerLiteral(0)
                                ),
                                BlockStmt([ContinueStmt()]),
                                [],
                                None
                            ),
                            Assignment(
                                IdLValue("out"),
                                BinaryOp(
                                    Identifier("out"),
                                    "+",
                                    BinaryOp(
                                        FunctionCall(Identifier("int2str"), [Identifier("n")]),
                                        "+",
                                        StringLiteral(" ")
                                    )
                                )
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("out")]))
                ]
            )
        ]
    )
    expected = "1 3 5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_047():
    """Pipeline into multi-parameter string builder (immutable params)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "wrapAdd",
                [Param("x", IntType()), Param("suffix", StringType())],
                StringType(),
                [
                    ReturnStmt(
                        BinaryOp(
                            FunctionCall(Identifier("int2str"), [Identifier("x")]),
                            "+",
                            Identifier("suffix")
                        )
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("res", StringType(),
                            BinaryOp(
                                IntegerLiteral(42),
                                ">>",
                                FunctionCall(Identifier("wrapAdd"), [StringLiteral("_units")])
                            )),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("res")]))
                ]
            )
        ]
    )
    expected = "42_units"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_048():
    """Short-circuit AND prevents second branch evaluation effect (simulated)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "flagTrue", [], BoolType(),
                [ReturnStmt(BooleanLiteral(True))]
            ),
            FuncDecl(
                "side",
                [Param("x", IntType())],
                IntType(),
                [
                    ReturnStmt(BinaryOp(Identifier("x"), "+", IntegerLiteral(999)))
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("base", IntType(), IntegerLiteral(1)),
                    VarDecl("b", BoolType(),
                            BinaryOp(
                                FunctionCall(Identifier("flagTrue"), []),
                                "&&",
                                BinaryOp(
                                    FunctionCall(Identifier("side"), [Identifier("base")]),
                                    ">",
                                    IntegerLiteral(0)
                                )
                            )),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("bool2str"), [Identifier("b")])]
                    ))
                ]
            )
        ]
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_049():
    """Operator precedence with %, *, +"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("val", IntType(),
                            BinaryOp(
                                BinaryOp(
                                    IntegerLiteral(7),
                                    "+",
                                    BinaryOp(IntegerLiteral(10), "%", IntegerLiteral(6))
                                ),
                                "*",
                                IntegerLiteral(2)
                            )),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("val")])]
                    ))
                ]
            )
        ]
    )
    expected = "22"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_050():
    """Pipeline after function result (array sum -> inc -> double)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "foo",
                [Param("a", ArrayType(IntType(), 5))],
                IntType(),
                [
                    VarDecl("acc", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "v",
                        Identifier("a"),
                        BlockStmt([
                            Assignment(
                                IdLValue("acc"),
                                BinaryOp(Identifier("acc"), "+", Identifier("v"))
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("acc"))
                ]
            ),
            FuncDecl(
                "inc",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", IntegerLiteral(1)))]
            ),
            FuncDecl(
                "double",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "*", IntegerLiteral(2)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl(
                        "arr",
                        ArrayType(IntType(), 5),
                        ArrayLiteral([
                            IntegerLiteral(1),
                            IntegerLiteral(2),
                            IntegerLiteral(3),
                            IntegerLiteral(4),
                            IntegerLiteral(5)
                        ])
                    ),
                    VarDecl("s", IntType(), FunctionCall(Identifier("foo"), [Identifier("arr")])),
                    VarDecl("r1", IntType(), BinaryOp(Identifier("s"), ">>", Identifier("inc"))),
                    VarDecl("r2", IntType(), BinaryOp(Identifier("r1"), ">>", Identifier("double"))),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("r2")])]
                    ))
                ]
            )
        ]
    )
    expected = "32"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_051():
    """Boolean arithmetic mix inside nested If"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(9)),
                    VarDecl("y", IntType(), IntegerLiteral(3)),
                    VarDecl("msg", StringType(), StringLiteral("")),
                    IfStmt(
                        BinaryOp(
                            BinaryOp(Identifier("x"), "%", Identifier("y")),
                            "==",
                            IntegerLiteral(0)
                        ),
                        BlockStmt([
                            Assignment(IdLValue("msg"), StringLiteral("div"))
                        ]),
                        [],
                        BlockStmt([
                            Assignment(IdLValue("msg"), StringLiteral("ndiv"))
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("msg")]))
                ]
            )
        ]
    )
    expected = "div"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_052():
    """Pipeline into function producing float then string concat"""
    ast = Program(
        [],
        [
            FuncDecl(
                "half",
                [Param("n", IntType())],
                FloatType(),
                [ReturnStmt(BinaryOp(Identifier("n"), "/", FloatLiteral(2.0)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("txt", StringType(),
                            BinaryOp(
                                StringLiteral("Value="),
                                "+",
                                FunctionCall(Identifier("float2str"),
                                             [BinaryOp(IntegerLiteral(9), ">>", Identifier("half"))])
                            )),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("txt")]))
                ]
            )
        ]
    )
    expected = "Value=4.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_053():
    """Recursive sum down without param mutation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "sumDown",
                [Param("n", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "==", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(IntegerLiteral(0))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    Identifier("n"),
                                    "+",
                                    FunctionCall(
                                        Identifier("sumDown"),
                                        [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                    )
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [FunctionCall(Identifier("sumDown"), [IntegerLiteral(5)])])]
                    ))
                ]
            )
        ]
    )
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_054():
    """Multi-branch If cascade building category string"""
    ast = Program(
        [],
        [
            FuncDecl(
                "cat",
                [Param("n", IntType())],
                StringType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "<", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(StringLiteral("neg"))]),
                        [
                            (BinaryOp(Identifier("n"), "<", IntegerLiteral(10)), BlockStmt([ReturnStmt(StringLiteral("small"))])),
                            (BinaryOp(Identifier("n"), "<", IntegerLiteral(100)), BlockStmt([ReturnStmt(StringLiteral("mid"))]))
                        ],
                        BlockStmt([ReturnStmt(StringLiteral("big"))])
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("vals", ArrayType(IntType(), 4),
                            ArrayLiteral([IntegerLiteral(-2), IntegerLiteral(5),
                                          IntegerLiteral(50), IntegerLiteral(500)])),
                    VarDecl("res", StringType(), StringLiteral("")),
                    ForStmt(
                        "v",
                        Identifier("vals"),
                        BlockStmt([
                            Assignment(
                                IdLValue("res"),
                                BinaryOp(
                                    Identifier("res"),
                                    "+",
                                    BinaryOp(FunctionCall(Identifier("cat"), [Identifier("v")]),
                                             "+",
                                             StringLiteral(";"))
                                )
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("res")]))
                ]
            )
        ]
    )
    expected = "neg;small;mid;big;"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_055():
    """Comparison chain simulated with &&"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(3)),
                    VarDecl("b", IntType(), IntegerLiteral(5)),
                    VarDecl("c", IntType(), IntegerLiteral(9)),
                    VarDecl("ok", BoolType(),
                            BinaryOp(
                                BinaryOp(Identifier("a"), "<", Identifier("b")),
                                "&&",
                                BinaryOp(Identifier("b"), "<", Identifier("c"))
                            )),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("bool2str"), [Identifier("ok")])]
                    ))
                ]
            )
        ]
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_056():
    """Integer division truncation and modulo combo"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("v", IntType(),
                            BinaryOp(
                                BinaryOp(IntegerLiteral(7), "/", IntegerLiteral(2)),
                                "+",
                                BinaryOp(IntegerLiteral(7), "%", IntegerLiteral(2))
                            )),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("v")])]
                    ))
                ]
            )
        ]
    )
    expected = "4"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_057():
    """Recursive string builder without mutating params"""
    ast = Program(
        [],
        [
            FuncDecl(
                "repeat",
                [Param("s", StringType()), Param("n", IntType())],
                StringType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "<=", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(StringLiteral(""))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    Identifier("s"),
                                    "+",
                                    FunctionCall(
                                        Identifier("repeat"),
                                        [
                                            Identifier("s"),
                                            BinaryOp(Identifier("n"), "-", IntegerLiteral(1))
                                        ]
                                    )
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("out", StringType(),
                            FunctionCall(Identifier("repeat"),
                                         [StringLiteral("A"),
                                          IntegerLiteral(5)])),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("out")]))
                ]
            )
        ]
    )
    expected = "AAAAA"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_058():
    """Test pipeline with function returning bool, then use in arithmetic"""
    ast = Program(
        [],
        [
            FuncDecl(
                "isEven",
                [Param("n", IntType())],
                BoolType(),
                [ReturnStmt(BinaryOp(BinaryOp(Identifier("n"), "%", IntegerLiteral(2)), "==", IntegerLiteral(0)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("flag", BoolType(), BinaryOp(IntegerLiteral(6), ">>", Identifier("isEven"))),
                    VarDecl("num", IntType(), IntegerLiteral(10)),
                    IfStmt(
                        BinaryOp(Identifier("flag"), "==", BooleanLiteral(True)),
                        BlockStmt([Assignment(IdLValue("num"), BinaryOp(Identifier("num"), "*", IntegerLiteral(2)))]),
                        [],
                        None
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("int2str"), [Identifier("num")])]))
                ]
            )
        ]
    )
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_059():
    """Test function returning array of floats, then sum"""
    ast = Program(
        [],
        [
            FuncDecl(
                "makeArr", [], ArrayType(FloatType(), 3),
                [ReturnStmt(ArrayLiteral([FloatLiteral(1.5), FloatLiteral(2.5), FloatLiteral(3.0)]))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("arr", ArrayType(FloatType(), 3), FunctionCall(Identifier("makeArr"), [])),
                    VarDecl("sum", FloatType(), FloatLiteral(0.0)),
                    ForStmt("v", Identifier("arr"),
                            BlockStmt([
                                Assignment(IdLValue("sum"), BinaryOp(Identifier("sum"), "+", Identifier("v")))
                            ])),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("float2str"), [Identifier("sum")])]))
                ]
            )
        ]
    )
    expected = "7.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_060():
    """Test chained pipeline with function result and concat"""
    ast = Program(
        [],
        [
            FuncDecl(
                "toStr", [Param("x", IntType())], StringType(),
                [ReturnStmt(FunctionCall(Identifier("int2str"), [Identifier("x")]))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("msg", StringType(),
                            BinaryOp(
                                BinaryOp(IntegerLiteral(42), ">>", Identifier("toStr")),
                                "+",
                                StringLiteral("_units")
                            )),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("msg")]))
                ]
            )
        ]
    )
    expected = "42_units"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_061():
    """Test function returning bool, then pipeline to string conversion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "isZero", [Param("x", IntType())], BoolType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "==", IntegerLiteral(0)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("msg", StringType(),
                            FunctionCall(Identifier("bool2str"),
                                         [BinaryOp(IntegerLiteral(0), ">>", Identifier("isZero"))])),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("msg")]))
                ]
            )
        ]
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_062():
    """Test nested pipeline with float promotion and arithmetic"""
    ast = Program(
        [],
        [
            FuncDecl(
                "toFloat", [Param("x", IntType())], FloatType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", FloatLiteral(0.0)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("v", FloatType(),
                            BinaryOp(
                                BinaryOp(IntegerLiteral(7), ">>", Identifier("toFloat")),
                                "+",
                                FloatLiteral(2.5)
                            )),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("float2str"), [Identifier("v")])]))
                ]
            )
        ]
    )
    expected = "9.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_063():
    """Test chained pipeline with bool, int, and string conversion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "toInt", [Param("b", BoolType())], IntType(),
                [ReturnStmt(BinaryOp(Identifier("b"), "==", BooleanLiteral(True)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("flag", BoolType(), BooleanLiteral(True)),
                    VarDecl("num", IntType(), BinaryOp(Identifier("flag"), ">>", Identifier("toInt"))),
                    VarDecl("msg", StringType(), FunctionCall(Identifier("int2str"), [Identifier("num")])),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("msg")]))
                ]
            )
        ]
    )
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_064():
    """Test nested If with pipeline and arithmetic"""
    ast = Program(
        [],
        [
            FuncDecl(
                "inc", [Param("x", IntType())], IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", IntegerLiteral(1)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(5)),
                    VarDecl("b", IntType(), IntegerLiteral(10)),
                    IfStmt(
                        BinaryOp(BinaryOp(Identifier("a"), ">>", Identifier("inc")), "==", IntegerLiteral(6)),
                        BlockStmt([ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("INC")]))]),
                        [],
                        BlockStmt([ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("NO")]))])
                    )
                ]
            )
        ]
    )
    expected = "INC"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_065():
    """Test pipeline with function returning float, then compare"""
    ast = Program(
        [],
        [
            FuncDecl(
                "half", [Param("x", IntType())], FloatType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "/", FloatLiteral(2.0)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("v", FloatType(), BinaryOp(IntegerLiteral(8), ">>", Identifier("half"))),
                    VarDecl("ok", BoolType(), BinaryOp(Identifier("v"), "==", FloatLiteral(4.0))),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("bool2str"), [Identifier("ok")])]))
                ]
            )
        ]
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_066():
    """Test pipeline with function returning bool, then string conversion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "isZero", [Param("x", IntType())], BoolType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "==", IntegerLiteral(0)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("n", IntType(), IntegerLiteral(0)),
                    VarDecl("msg", StringType(),
                            FunctionCall(Identifier("bool2str"),
                                         [BinaryOp(Identifier("n"), ">>", Identifier("isZero"))])),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("msg")]))
                ]
            )
        ]
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_067():
    """Test pipeline chaining with arithmetic and bool conversion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "isPositive", [Param("x", IntType())], BoolType(),
                [ReturnStmt(BinaryOp(Identifier("x"), ">", IntegerLiteral(0)))]
            ),
            FuncDecl(
                "main", [], VoidType(),
                [
                    VarDecl("n", IntType(), IntegerLiteral(-3)),
                    VarDecl("flag", BoolType(), BinaryOp(Identifier("n"), ">>", Identifier("isPositive"))),
                    IfStmt(Identifier("flag"),
                           BlockStmt([ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("POS")]))]),
                           [],
                           BlockStmt([ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("NEG")]))]))
                ]
            )
        ]
    )
    expected = "NEG"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
    
def test_068():
    """Test float arithmetic operations"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", FloatType(), FloatLiteral(3.5)),
                    VarDecl("b", FloatType(), FloatLiteral(2.0)),
                    VarDecl("result", FloatType(), BinaryOp(
                        BinaryOp(Identifier("a"), "+", Identifier("b")),
                        "*",
                        FloatLiteral(2.0)
                    )),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("float2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "11.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_069():
    """Test boolean logic in if statement"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", BoolType(), BooleanLiteral(True)),
                    VarDecl("b", BoolType(), BooleanLiteral(False)),
                    IfStmt(
                        BinaryOp(
                            Identifier("a"),
                            "||",
                            Identifier("b")
                        ),
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("True")]))
                        ]),
                        [],
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("False")]))
                        ])
                    )
                ]
            )
        ]
    )
    expected = "True"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_070():
    """Test array of strings and concatenation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "words",
                        ArrayType(StringType(), 3),
                        ArrayLiteral([
                            StringLiteral("Hello"),
                            StringLiteral(" "),
                            StringLiteral("World")
                        ])
                    ),
                    VarDecl("result", StringType(), StringLiteral("")),
                    ForStmt(
                        "word",
                        Identifier("words"),
                        BlockStmt([
                            Assignment(
                                IdLValue("result"),
                                BinaryOp(Identifier("result"), "+", Identifier("word"))
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("result")]))
                ]
            )
        ]
    )
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_071():
    """Test pipeline with multiple functions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "inc",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "+", IntegerLiteral(1)))]
            ),
            FuncDecl(
                "double",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "*", IntegerLiteral(2)))]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "result",
                        IntType(),
                        BinaryOp(
                            BinaryOp(IntegerLiteral(5), ">>", Identifier("inc")),
                            ">>",
                            Identifier("double")
                        )
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "12"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_072():
    """Test recursive fibonacci"""
    ast = Program(
        [],
        [
            FuncDecl(
                "fib",
                [Param("n", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "<=", IntegerLiteral(1)),
                        BlockStmt([ReturnStmt(Identifier("n"))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    FunctionCall(Identifier("fib"), [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]),
                                    "+",
                                    FunctionCall(Identifier("fib"), [BinaryOp(Identifier("n"), "-", IntegerLiteral(2))])
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [FunctionCall(Identifier("fib"), [IntegerLiteral(6)])])]
                    ))
                ]
            )
        ]
    )
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_073():
    """Test while loop with continue"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    VarDecl("sum", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<", IntegerLiteral(10)),
                        BlockStmt([
                            Assignment(IdLValue("i"), BinaryOp(Identifier("i"), "+", IntegerLiteral(1))),
                            IfStmt(
                                BinaryOp(
                                    BinaryOp(Identifier("i"), "%", IntegerLiteral(2)),
                                    "==",
                                    IntegerLiteral(0)
                                ),
                                BlockStmt([ContinueStmt()]),
                                [],
                                None
                            ),
                            Assignment(IdLValue("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i")))
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                    ))
                ]
            )
        ]
    )
    expected = "25"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_074():
    """Test for loop with break"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 5), ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)])),
                    VarDecl("sum", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "num",
                        Identifier("arr"),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(Identifier("num"), "==", IntegerLiteral(4)),
                                BlockStmt([BreakStmt()]),
                                [],
                                None
                            ),
                            Assignment(IdLValue("sum"), BinaryOp(Identifier("sum"), "+", Identifier("num")))
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                    ))
                ]
            )
        ]
    )
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_075():
    """Test global constant usage in function"""
    ast = Program(
        [ConstDecl("MAX", IntType(), IntegerLiteral(100))],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("value", IntType(), BinaryOp(Identifier("MAX"), "-", IntegerLiteral(10))),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("value")])]
                    ))
                ]
            )
        ]
    )
    expected = "90"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_076():
    """Test multi-dimensional array access"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl(
                        "matrix",
                        ArrayType(ArrayType(IntType(), 2), 2),
                        ArrayLiteral([
                            ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]),
                            ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [ArrayAccess(ArrayAccess(Identifier("matrix"), IntegerLiteral(1)), IntegerLiteral(1))])]
                    ))
                ]
            )
        ]
    )
    expected = "4"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_077():
    """Test string concatenation with int via int2str"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("text", StringType(), StringLiteral("Value: ")),
                    VarDecl("num", IntType(), IntegerLiteral(42)),
                    VarDecl("combined", StringType(), BinaryOp(Identifier("text"), "+", FunctionCall(Identifier("int2str"), [Identifier("num")]))),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("combined")]))
                ]
            )
        ]
    )
    expected = "Value: 42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_078():
    """Test nested if statements with multiple conditions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(15)),
                    IfStmt(
                        BinaryOp(Identifier("x"), ">", IntegerLiteral(10)),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(Identifier("x"), "<", IntegerLiteral(20)),
                                BlockStmt([
                                    ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("In Range")]))
                                ]),
                                [],
                                BlockStmt([
                                    ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Out of Range")]))
                                ])
                            )
                        ]),
                        [],
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Below Range")]))
                        ])
                    )
                ]
            )
        ]
    )
    expected = "In Range"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_079():
    """Test array element access with computed index"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 4), ArrayLiteral([IntegerLiteral(10), IntegerLiteral(20), IntegerLiteral(30), IntegerLiteral(40)])),
                    VarDecl("index", IntType(), BinaryOp(IntegerLiteral(2), "+", IntegerLiteral(1))),
                    VarDecl("value", IntType(), ArrayAccess(Identifier("arr"), Identifier("index"))),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("value")])]
                    ))
                ]
            )
        ]
    )
    expected = "40"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_080():
    """Test nested while loops with boolean conditions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    VarDecl("count", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<", IntegerLiteral(3)),
                        BlockStmt([
                            VarDecl("j", IntType(), IntegerLiteral(0)),
                            WhileStmt(
                                BinaryOp(Identifier("j"), "<", IntegerLiteral(2)),
                                BlockStmt([
                                    Assignment(IdLValue("count"), BinaryOp(Identifier("count"), "+", IntegerLiteral(1))),
                                    Assignment(IdLValue("j"), BinaryOp(Identifier("j"), "+", IntegerLiteral(1)))
                                ])
                            ),
                            Assignment(IdLValue("i"), BinaryOp(Identifier("i"), "+", IntegerLiteral(1)))
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("count")])]
                    ))
                ]
            )
        ]
    )
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_081():
    """Test function returning array and type inference"""
    ast = Program(
        [],
        [
            FuncDecl(
                "getArray",
                [],
                ArrayType(IntType(), 3),
                [
                    ReturnStmt(ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 3), FunctionCall(Identifier("getArray"), [])),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [ArrayAccess(Identifier("arr"), IntegerLiteral(2))])]
                    ))
                ]
            )
        ]
    )
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_082():
    """Test modulo operation in loop"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("sum", IntType(), IntegerLiteral(0)),
                    VarDecl("i", IntType(), IntegerLiteral(1)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<=", IntegerLiteral(10)),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(
                                    BinaryOp(Identifier("i"), "%", IntegerLiteral(3)),
                                    "==",
                                    IntegerLiteral(0)
                                ),
                                BlockStmt([
                                    Assignment(IdLValue("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i")))
                                ]),
                                [],
                                None
                            ),
                            Assignment(IdLValue("i"), BinaryOp(Identifier("i"), "+", IntegerLiteral(1)))
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                    ))
                ]
            )
        ]
    )
    expected = "18"  # 3 + 6 + 9
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_083():
    """Test string comparison with equality operator"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("str1", StringType(), StringLiteral("test")),
                    VarDecl("str2", StringType(), StringLiteral("test")),
                    IfStmt(
                        BinaryOp(Identifier("str1"), "==", Identifier("str2")),
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Equal")]))
                        ]),
                        [],
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Not Equal")]))
                        ])
                    )
                ]
            )
        ]
    )
    expected = "Equal"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_084():
    """Test function with array parameter (no modification)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "sumArray",
                [Param("arr", ArrayType(IntType(), 3))],
                IntType(),
                [
                    VarDecl("total", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "num",
                        Identifier("arr"),
                        BlockStmt([
                            Assignment(IdLValue("total"), BinaryOp(Identifier("total"), "+", Identifier("num")))
                        ])
                    ),
                    ReturnStmt(Identifier("total"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("numbers", ArrayType(IntType(), 3), ArrayLiteral([IntegerLiteral(2), IntegerLiteral(4), IntegerLiteral(6)])),
                    VarDecl("sum", IntType(), FunctionCall(Identifier("sumArray"), [Identifier("numbers")])),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                    ))
                ]
            )
        ]
    )
    expected = "12"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_085():
    """Test boolean negation in conditional"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("flag", BoolType(), BooleanLiteral(False)),
                    IfStmt(
                        UnaryOp("!", Identifier("flag")),
                        BlockStmt([
                            ExprStmt(FunctionCall(Identifier("print"), [StringLiteral("Negated")]))
                        ]),
                        [],
                        None
                    )
                ]
            )
        ]
    )
    expected = "Negated"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_086():
    """Test float to string conversion with concatenation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("value", FloatType(), FloatLiteral(3.14159)),
                    VarDecl("prefix", StringType(), StringLiteral("Pi: ")),
                    VarDecl("result", StringType(), BinaryOp(Identifier("prefix"), "+", FunctionCall(Identifier("float2str"), [Identifier("value")]))),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("result")]))
                ]
            )
        ]
    )
    expected = "Pi: 3.1416"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_087():
    """Test for loop with array of booleans"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("flags", ArrayType(BoolType(), 3), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)])),
                    VarDecl("count", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "flag",
                        Identifier("flags"),
                        BlockStmt([
                            IfStmt(
                                Identifier("flag"),
                                BlockStmt([
                                    Assignment(IdLValue("count"), BinaryOp(Identifier("count"), "+", IntegerLiteral(1)))
                                ]),
                                [],
                                None
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("count")])]
                    ))
                ]
            )
        ]
    )
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_088():
    """Test recursive function with multiple parameters"""
    ast = Program(
        [],
        [
            FuncDecl(
                "power",
                [Param("base", IntType()), Param("exp", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("exp"), "<=", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(IntegerLiteral(1))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    Identifier("base"),
                                    "*",
                                    FunctionCall(Identifier("power"), [Identifier("base"), BinaryOp(Identifier("exp"), "-", IntegerLiteral(1))])
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(), FunctionCall(Identifier("power"), [IntegerLiteral(2), IntegerLiteral(3)])),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
    
def test_089():
    """Param int immutable: use local copy to modify"""
    ast = Program(
        [],
        [
            FuncDecl(
                "inc_copy",
                [Param("x", IntType())],
                IntType(),
                [
                    VarDecl("y", IntType(), Identifier("x")),
                    Assignment(IdLValue("y"), BinaryOp(Identifier("y"), "+", IntegerLiteral(1))),
                    ReturnStmt(Identifier("y")),
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(7)),
                    VarDecl("res", IntType(), FunctionCall(Identifier("inc_copy"), [Identifier("a")])),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [
                                BinaryOp(
                                    FunctionCall(Identifier("int2str"), [Identifier("res")]),
                                    "+",
                                    BinaryOp(StringLiteral(","), "+", FunctionCall(Identifier("int2str"), [Identifier("a")]))
                                )
                            ],
                        )
                    ),
                ],
            ),
        ],
    )
    expected = "8,7"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_090():
    """Param array immutable: sum without mutation and verify original array unchanged"""
    ast = Program(
        [],
        [
            FuncDecl(
                "sum_array_nomut",
                [Param("arr", ArrayType(IntType(), 5))],
                IntType(),
                [
                    VarDecl("total", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "v",
                        Identifier("arr"),
                        BlockStmt([
                            Assignment(IdLValue("total"), BinaryOp(Identifier("total"), "+", Identifier("v")))
                        ])
                    ),
                    ReturnStmt(Identifier("total")),
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 5), ArrayLiteral([
                        IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)
                    ])),
                    VarDecl("s", IntType(), FunctionCall(Identifier("sum_array_nomut"), [Identifier("arr")])),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("int2str"), [Identifier("s")])])),
                    VarDecl("show", StringType(), StringLiteral("")),
                    ForStmt(
                        "e",
                        Identifier("arr"),
                        BlockStmt([
                            Assignment(
                                IdLValue("show"),
                                BinaryOp(Identifier("show"), "+",
                                         BinaryOp(FunctionCall(Identifier("int2str"), [Identifier("e")]), "+", StringLiteral(",")))
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("show")])),
                ],
            ),
        ],
    )
    expected = "15\n1,2,3,4,5,"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_091():
    """Mix params (int + array) immutable: compute using reads only"""
    ast = Program(
        [],
        [
            FuncDecl(
                "add_mid",
                [Param("a", IntType()), Param("arr", ArrayType(IntType(), 3))],
                IntType(),
                [
                    VarDecl("mid", IntType(), ArrayAccess(Identifier("arr"), IntegerLiteral(1))),
                    ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("mid")))
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(10)),
                    VarDecl("arr", ArrayType(IntType(), 3), ArrayLiteral([IntegerLiteral(0), IntegerLiteral(5), IntegerLiteral(0)])),
                    VarDecl("r", IntType(), FunctionCall(Identifier("add_mid"), [Identifier("a"), Identifier("arr")])),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("int2str"), [Identifier("r")])]))
                ],
            ),
        ],
    )
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_092():
    """Two string params immutable: build result via locals"""
    ast = Program(
        [],
        [
            FuncDecl(
                "greet",
                [Param("prefix", StringType()), Param("name", StringType())],
                StringType(),
                [
                    VarDecl("msg", StringType(), BinaryOp(Identifier("prefix"), "+", Identifier("name"))),
                    ReturnStmt(Identifier("msg"))
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("greet"), [StringLiteral("Hello, "), StringLiteral("HLang")])]))
                ],
            ),
        ],
    )
    expected = "Hello, HLang"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_093():
    """Two readers over same array param: max & min; verify no mutation by reprinting array"""
    ast = Program(
        [],
        [
            FuncDecl(
                "arr_max",
                [Param("arr", ArrayType(IntType(), 3))],
                IntType(),
                [
                    VarDecl("m", IntType(), ArrayAccess(Identifier("arr"), IntegerLiteral(0))),
                    ForStmt(
                        "v",
                        Identifier("arr"),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(Identifier("v"), ">", Identifier("m")),
                                BlockStmt([Assignment(IdLValue("m"), Identifier("v"))]),
                                [],
                                None
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("m"))
                ],
            ),
            FuncDecl(
                "arr_min",
                [Param("arr", ArrayType(IntType(), 3))],
                IntType(),
                [
                    VarDecl("m", IntType(), ArrayAccess(Identifier("arr"), IntegerLiteral(0))),
                    ForStmt(
                        "v",
                        Identifier("arr"),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(Identifier("v"), "<", Identifier("m")),
                                BlockStmt([Assignment(IdLValue("m"), Identifier("v"))]),
                                [],
                                None
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("m"))
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 3), ArrayLiteral([IntegerLiteral(1), IntegerLiteral(5), IntegerLiteral(3)])),
                    VarDecl("mx", IntType(), FunctionCall(Identifier("arr_max"), [Identifier("arr")])),
                    VarDecl("mn", IntType(), FunctionCall(Identifier("arr_min"), [Identifier("arr")])),
                    VarDecl(
                        "line1",
                        StringType(),
                        BinaryOp(
                            FunctionCall(Identifier("int2str"), [Identifier("mx")]),
                            "+",
                            BinaryOp(StringLiteral(","), "+", FunctionCall(Identifier("int2str"), [Identifier("mn")]))
                        )
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("line1")])),
                    VarDecl("show", StringType(), StringLiteral("")),
                    ForStmt(
                        "e",
                        Identifier("arr"),
                        BlockStmt([
                            Assignment(
                                IdLValue("show"),
                                BinaryOp(Identifier("show"), "+",
                                         BinaryOp(FunctionCall(Identifier("int2str"), [Identifier("e")]), "+", StringLiteral(",")))
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("show")])),
                ],
            ),
        ],
    )
    expected = "5,1\n1,5,3,"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_094():
    """Bool param immutable: decision without changing flag"""
    ast = Program(
        [],
        [
            FuncDecl(
                "decide",
                [Param("flag", BoolType())],
                StringType(),
                [
                    IfStmt(
                        Identifier("flag"),
                        BlockStmt([ReturnStmt(StringLiteral("yes"))]),
                        [],
                        BlockStmt([ReturnStmt(StringLiteral("no"))])
                    )
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("decide"), [BooleanLiteral(True)])])),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("decide"), [BooleanLiteral(False)])])),
                ],
            ),
        ],
    )
    expected = "yes\nno"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_095():
    """Pipeline with param read-only: verify original arg unchanged"""
    ast = Program(
        [],
        [
            FuncDecl(
                "doub",
                [Param("x", IntType())],
                IntType(),
                [ReturnStmt(BinaryOp(Identifier("x"), "*", IntegerLiteral(2)))]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("n", IntType(), IntegerLiteral(3)),
                    VarDecl(
                        "res",
                        IntType(),
                        BinaryOp(BinaryOp(Identifier("n"), ">>", Identifier("doub")), ">>", Identifier("doub"))
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [
                                BinaryOp(
                                    FunctionCall(Identifier("int2str"), [Identifier("res")]),
                                    "+",
                                    BinaryOp(StringLiteral(","), "+", FunctionCall(Identifier("int2str"), [Identifier("n")]))
                                )
                            ]
                        )
                    )
                ],
            ),
        ],
    )
    expected = "12,3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_096():
    """2D array param immutable: sum elements and re-show original matrix"""
    ast = Program(
        [],
        [
            FuncDecl(
                "sum2",
                [Param("m", ArrayType(ArrayType(IntType(), 2), 2))],
                IntType(),
                [
                    VarDecl("s", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "row",
                        Identifier("m"),
                        BlockStmt([
                            ForStmt(
                                "e",
                                Identifier("row"),
                                BlockStmt([
                                    Assignment(IdLValue("s"), BinaryOp(Identifier("s"), "+", Identifier("e")))
                                ])
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("s"))
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("mat", ArrayType(ArrayType(IntType(), 2), 2), ArrayLiteral([
                        ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]),
                        ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])
                    ])),
                    VarDecl("s", IntType(), FunctionCall(Identifier("sum2"), [Identifier("mat")])),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("int2str"), [Identifier("s")])])),
                    VarDecl("show", StringType(), StringLiteral("")),
                    ForStmt(
                        "r",
                        Identifier("mat"),
                        BlockStmt([
                            ForStmt(
                                "e",
                                Identifier("r"),
                                BlockStmt([
                                    Assignment(IdLValue("show"),
                                               BinaryOp(Identifier("show"), "+",
                                                        BinaryOp(FunctionCall(Identifier("int2str"), [Identifier("e")]), "+", StringLiteral(","))))
                                ])
                            )
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("show")])),
                ],
            ),
        ],
    )
    expected = "10\n1,2,3,4,"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_097():
    """While using local copy of int param; verify param unchanged"""
    ast = Program(
        [],
        [
            FuncDecl(
                "countdown_to_zero",
                [Param("x", IntType())],
                IntType(),
                [
                    VarDecl("y", IntType(), Identifier("x")),
                    WhileStmt(
                        BinaryOp(Identifier("y"), ">", IntegerLiteral(0)),
                        BlockStmt([
                            Assignment(IdLValue("y"), BinaryOp(Identifier("y"), "-", IntegerLiteral(1)))
                        ])
                    ),
                    ReturnStmt(Identifier("y"))
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("n", IntType(), IntegerLiteral(4)),
                    VarDecl("r", IntType(), FunctionCall(Identifier("countdown_to_zero"), [Identifier("n")])),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [
                                BinaryOp(
                                    FunctionCall(Identifier("int2str"), [Identifier("r")]),
                                    "+",
                                    BinaryOp(StringLiteral(","), "+", FunctionCall(Identifier("int2str"), [Identifier("n")]))
                                )
                            ]
                        )
                    ),
                ],
            ),
        ],
    )
    expected = "0,4"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected

def test_098():
    """Recursive prefix sum over array param (immutable)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "sum_prefix",
                [Param("arr", ArrayType(IntType(), 5)), Param("k", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("k"), "<=", IntegerLiteral(0)),
                        BlockStmt([ReturnStmt(IntegerLiteral(0))]),
                        [],
                        BlockStmt([
                            ReturnStmt(
                                BinaryOp(
                                    ArrayAccess(Identifier("arr"), BinaryOp(Identifier("k"), "-", IntegerLiteral(1))),
                                    "+",
                                    FunctionCall(Identifier("sum_prefix"), [Identifier("arr"), BinaryOp(Identifier("k"), "-", IntegerLiteral(1))])
                                )
                            )
                        ])
                    )
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 5), ArrayLiteral([
                        IntegerLiteral(2), IntegerLiteral(4), IntegerLiteral(6), IntegerLiteral(8), IntegerLiteral(10)
                    ])),
                    VarDecl("k", IntType(), IntegerLiteral(3)),
                    VarDecl("r", IntType(), FunctionCall(Identifier("sum_prefix"), [Identifier("arr"), Identifier("k")])),
                    ExprStmt(FunctionCall(Identifier("print"), [FunctionCall(Identifier("int2str"), [Identifier("r")])])),
                    VarDecl("show", StringType(), StringLiteral("")),
                    ForStmt(
                        "e",
                        Identifier("arr"),
                        BlockStmt([
                            Assignment(IdLValue("show"),
                                       BinaryOp(Identifier("show"), "+",
                                                BinaryOp(FunctionCall(Identifier("int2str"), [Identifier("e")]), "+", StringLiteral(","))))
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("show")])),
                ],
            ),
        ],
    )
    expected = "12\n2,4,6,8,10,"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected   

def test_099():
    """Immutable array param: build reversed copy locally without mutating original"""
    ast = Program(
        [],
        [
            FuncDecl(
                "reverse_copy",
                [Param("arr", ArrayType(IntType(), 4))],
                ArrayType(IntType(), 4),
                [
                    VarDecl("rev", ArrayType(IntType(), 4),
                            ArrayLiteral([IntegerLiteral(0), IntegerLiteral(0), IntegerLiteral(0), IntegerLiteral(0)])),
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<", IntegerLiteral(4)),
                        BlockStmt([
                            Assignment(
                                ArrayAccessLValue(Identifier("rev"), Identifier("i")),
                                ArrayAccess(Identifier("arr"), BinaryOp(IntegerLiteral(3), "-", Identifier("i")))
                            ),
                            Assignment(IdLValue("i"), BinaryOp(Identifier("i"), "+", IntegerLiteral(1)))
                        ])
                    ),
                    ReturnStmt(Identifier("rev"))
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 4), ArrayLiteral([
                        IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3), IntegerLiteral(4)
                    ])),
                    VarDecl("rev", ArrayType(IntType(), 4), FunctionCall(Identifier("reverse_copy"), [Identifier("arr")])),
                    VarDecl("out1", StringType(), StringLiteral("")),
                    ForStmt(
                        "e",
                        Identifier("rev"),
                        BlockStmt([
                            Assignment(IdLValue("out1"),
                                       BinaryOp(Identifier("out1"), "+",
                                                BinaryOp(FunctionCall(Identifier("int2str"), [Identifier("e")]), "+", StringLiteral(","))))
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("out1")])),
                    VarDecl("out2", StringType(), StringLiteral("")),
                    ForStmt(
                        "e2",
                        Identifier("arr"),
                        BlockStmt([
                            Assignment(IdLValue("out2"),
                                       BinaryOp(Identifier("out2"), "+",
                                                BinaryOp(FunctionCall(Identifier("int2str"), [Identifier("e2")]), "+", StringLiteral(","))))
                        ])
                    ),
                    ExprStmt(FunctionCall(Identifier("print"), [Identifier("out2")]))
                ],
            ),
        ],
    )
    expected = "4,3,2,1,\n1,2,3,4,"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_100():
    """Test float division and string conversion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", FloatType(), FloatLiteral(10.0)),
                    VarDecl("b", IntType(), IntegerLiteral(4)),
                    VarDecl("result", FloatType(), BinaryOp(Identifier("a"), "/", Identifier("b"))),
                    ExprStmt(FunctionCall(
                        Identifier("print"),
                        [FunctionCall(Identifier("float2str"), [Identifier("result")])]
                    ))
                ]
            )
        ]
    )
    expected = "2.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
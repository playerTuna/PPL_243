# HLang Compiler Project (PPL_243)

## 📌 Overview
This is a HLang programming language project built as part of the *Principles of Programming Languages (PPL)* course.  
The project demonstrates the full compilation pipeline, including **lexer, parser, AST construction, semantic checking, and code generation**.  
---

## ⚙️ Features
- **Lexer**: Tokenizes source code into lexical units.  
- **Parser**: Builds parse trees and validates syntax according to grammar.  
- **AST Generation**: Converts parse tree into Abstract Syntax Tree for easier analysis.  
- **Static Checker**: Performs type checking and semantic validation.  
- **Code Generation**: Generates target code (using Jasmin/Java bytecode backend provided by instructor).  

---

## 🛠️ Tech Stack
- **Python**: Core implementation of compiler stages  
- **ANTLR**: Grammar definition and parser generation  
- **Jasmin**: Java bytecode backend (provided)  

---
## 📂 Project Structure

PPL_243/
├── src/ # Compiler implementation
│ ├── lexer/ # Lexical analysis
│ ├── parser/ # Syntax parsing
│ ├── ast/ # Abstract Syntax Tree
│ ├── checker/ # Semantic and type checking
│ └── codegen/ # Code generation
│
├── tests/ # Unit tests
│ ├── test_lexer.py # Tests for lexical analysis
│ ├── test_parser.py # Tests for syntax parsing
│ ├── test_ast_gen.py # Tests for AST generation
│ ├── test_checker.py # Tests for type checking
│ ├── test_codegen.py # Tests for code generation
│ └── utils.py # Shared test utilities
│
└── run.py # Entry point to run the compiler

## 1️⃣ Prerequisites

Make sure you have:

- **Python 3.12+**
- **Java 17+**

---

## 2️⃣ Clone the repository

```bash
git clone <repository-url>
cd hlang-compiler
```

---

## 3️⃣ Setup environment

```bash
# Option 1: Using Makefile (recommended)
make setup

# Option 2: Using Python script
# Windows:
python run.py setup
# macOS/Linux:
python3 run.py setup
```

✅ This will:

- Create a virtual environment
- Install Python dependencies
- Download ANTLR4 automatically

---

## 4️⃣ Activate the virtual environment

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

---

## 5️⃣ Build the compiler

```bash
# Using Makefile
make build

# Or using Python script
# Windows:
python run.py build
# macOS/Linux:
python3 run.py build
```

---

## 6️⃣ Run tests

You can run all test suites or specific stages:

```bash
# Run all tests
make test

# Or run specific test suites
make test-lexer     # Lexical analysis
make test-parser    # Syntax analysis
make test-ast       # AST generation
make test-checker   # Semantic analysis
make test-codegen   # Code generation
```

Or equivalently using the entry script:

```bash
# Windows:
python run.py test-lexer
python run.py test-parser
python run.py test-ast
python run.py test-checker
python run.py test-codegen

# macOS/Linux:
python3 run.py test-lexer
python3 run.py test-parser
python3 run.py test-ast
python3 run.py test-checker
python3 run.py test-codegen
```

## 7️⃣ Clean build or cache

```bash
make clean          # Remove build artifacts
make clean-cache    # Remove __pycache__ files
make clean-venv     # Remove virtual environment
```

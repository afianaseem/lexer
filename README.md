# Lexical Analyzer (Lexer) Project
A simple lexical analyzer that reads source code and converts it into tokens. This project implements two versions of a lexer: one using regular expressions and another using a state machine with raw string comparisons.

# 📁 Project Structure
```
lexer/

├── tokens.py          # Token definitions and TokenType enum

├── regex_lexer.py     # Lexer implementation using regular expressions

├── state_lexer.py     # Lexer implementation using state machine

├── main.py           # Main program to test both lexers

└── requirements.txt   # Project dependencies
```

# 🚀 Features
Core Functionality
Tokenizes source code into meaningful tokens

 1 Two implementations: Regex-based and State Machine-based

 2 Error handling for invalid characters and identifiers

Line tracking for error reporting

Supported Token Types
```Keywords: fn, int, float, string, bool, return, if, else, while, for, true, false

Identifiers: Variable and function names

Literals: Integer, float, string, and boolean values

Operators: =, ==, !=, <, >, <=, >=, &&, ||, +, -, *, /

Delimiters: (), {}, [], ,, ;, :

Comments: Single-line (//) and multi-line (/* */)
```
Advanced Features

```
Escape sequence support in strings: \n, \t, \r, \", \\

Unicode support for identifiers (Chinese characters, etc.)

Basic emoji support (experimental)

Error detection for invalid identifiers
```
#🛠️ Installation & Setup
Clone the repository:
```
git clone <your-repo-url>
cd lexer
```
Run the lexer (no installation required):
```
python main.py
```
# 📋 Usage
Basic Usage
```
from regex_lexer import RegexLexer
from state_lexer import StateMachineLexer
```
# Sample code to tokenize
```
code = """
fn int my_function(int x) {
    return x + 42;
}
"""
```
# Using regex lexer
```
regex_lexer = RegexLexer(code)
tokens = regex_lexer.tokenize()
```
# Using state machine lexer
```
state_lexer = StateMachineLexer(code)
tokens = state_lexer.tokenize()
```
Testing with Custom Code
```
Modify the sample_code variable in main.py to test with your own code:
```
# Sample code 
```
sample_code = """
// Your custom code here
fn int calculate(int a, int b) {
    return a * b + 3.14;
}
```

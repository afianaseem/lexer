# tokens.py
from enum import Enum

class TokenType(Enum):
    # Keywords
    FUNCTION = "FUNCTION"
    INT = "INT"
    FLOAT = "FLOAT"
    STRING = "STRING"
    BOOL = "BOOL"
    RETURN = "RETURN"
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    FOR = "FOR"
    TRUE = "TRUE"
    FALSE = "FALSE"
    
    # Identifiers and literals
    IDENTIFIER = "IDENTIFIER"
    INTLIT = "INTLIT"
    FLOATLIT = "FLOATLIT"
    STRINGLIT = "STRINGLIT"
    BOOLLIT = "BOOLLIT"
    
    # Operators
    ASSIGNOP = "ASSIGNOP"
    EQUALSOP = "EQUALSOP"
    NOTEQUALS = "NOTEQUALS"
    LESSTHAN = "LESSTHAN"
    GREATERTHAN = "GREATERTHAN"
    LESSEQUAL = "LESSEQUAL"
    GREATEREQUAL = "GREATEREQUAL"
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    
    # Delimiters
    PARENL = "PARENL"
    PARENR = "PARENR"
    BRACEL = "BRACEL"
    BRACER = "BRACER"
    BRACKETL = "BRACKETL"
    BRACKETR = "BRACKETR"
    COMMA = "COMMA"
    SEMICOLON = "SEMICOLON"
    QUOTES = "QUOTES"
    COLON = "COLON"
    
    # Special
    COMMENT = "COMMENT"
    EOF = "EOF"
    ERROR = "ERROR"


class Token:
    def __init__(self, type, value=None, line=None):
        self.type = type
        self.value = value
        self.line = line
    
    def __str__(self):
        if self.value is not None:
            return f"T_{self.type.name}({repr(self.value)})"
        return f"T_{self.type.name}"
    
    def __repr__(self):
        return self.__str__()
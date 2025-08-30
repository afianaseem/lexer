# regex_lexer.py
import re
from tokens import Token, TokenType

class RegexLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.tokens = []
        
        # Define regex patterns in order of priority
        self.patterns = [
            # Comments (must come first to avoid matching as operators)
            (r'//.*', TokenType.COMMENT),
            (r'/\*.*?\*/', TokenType.COMMENT),
            
            # Keywords
            (r'\bfn\b', TokenType.FUNCTION),
            (r'\bint\b', TokenType.INT),
            (r'\bfloat\b', TokenType.FLOAT),
            (r'\bstring\b', TokenType.STRING),
            (r'\bbool\b', TokenType.BOOL),
            (r'\breturn\b', TokenType.RETURN),
            (r'\bif\b', TokenType.IF),
            (r'\belse\b', TokenType.ELSE),
            (r'\bwhile\b', TokenType.WHILE),
            (r'\bfor\b', TokenType.FOR),
            (r'\btrue\b', TokenType.TRUE),
            (r'\bfalse\b', TokenType.FALSE),
            
            # Literals
            (r'"[^"\\]*(?:\\.[^"\\]*)*"', TokenType.STRINGLIT),
            (r'\d+\.\d+', TokenType.FLOATLIT),
            (r'\d+', TokenType.INTLIT),
            
            # Multi-character operators
            (r'==', TokenType.EQUALSOP),
            (r'!=', TokenType.NOTEQUALS),
            (r'<=', TokenType.LESSEQUAL),
            (r'>=', TokenType.GREATEREQUAL),
            (r'&&', TokenType.AND),
            (r'\|\|', TokenType.OR),
            
            # Single-character operators
            (r'=', TokenType.ASSIGNOP),
            (r'<', TokenType.LESSTHAN),
            (r'>', TokenType.GREATERTHAN),
            (r'!', TokenType.NOT),
            (r'\+', TokenType.PLUS),
            (r'-', TokenType.MINUS),
            (r'\*', TokenType.MULTIPLY),
            (r'/', TokenType.DIVIDE),
            
            # Delimiters
            (r'\(', TokenType.PARENL),
            (r'\)', TokenType.PARENR),
            (r'\{', TokenType.BRACEL),
            (r'\}', TokenType.BRACER),
            (r'\[', TokenType.BRACKETL),
            (r'\]', TokenType.BRACKETR),
            (r',', TokenType.COMMA),
            (r';', TokenType.SEMICOLON),
            (r':', TokenType.COLON),
            
            # Identifiers (must come last)
# Alternative for standard re module:
(r'[a-zA-Z_\u0080-\uFFFF][a-zA-Z0-9_\u0080-\uFFFF]*', TokenType.IDENTIFIER),      ]
    
    def tokenize(self):
        while self.position < len(self.source_code):
            char = self.source_code[self.position]
            
            # Skip whitespace and track lines
            if char.isspace():
                if char == '\n':
                    self.line += 1
                self.position += 1
                continue
            
            matched = False
            for pattern, token_type in self.patterns:
                regex = re.compile(pattern)
                match = regex.match(self.source_code, self.position)
                if match:
                    value = match.group()
                    # Don't add comments to token stream
                    if token_type != TokenType.COMMENT:
                        self.tokens.append(Token(token_type, value, self.line))
                    self.position = match.end()
                    matched = True
                    break
            
            if not matched:
                # Handle error - invalid character
                error_token = Token(TokenType.ERROR, char, self.line)
                self.tokens.append(error_token)
                self.position += 1
        
        self.tokens.append(Token(TokenType.EOF, None, self.line))
        return self.tokens
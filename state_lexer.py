# state_lexer.py
from tokens import Token, TokenType

class StateMachineLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.tokens = []
        
        self.keywords = {
            'fn': TokenType.FUNCTION,
            'int': TokenType.INT,
            'float': TokenType.FLOAT,
            'string': TokenType.STRING,
            'bool': TokenType.BOOL,
            'return': TokenType.RETURN,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'for': TokenType.FOR,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE
        }
    
    def current_char(self):
        if self.position < len(self.source_code):
            return self.source_code[self.position]
        return None
    
    def peek_char(self):
        if self.position + 1 < len(self.source_code):
            return self.source_code[self.position + 1]
        return None
    
    def advance(self):
        if self.current_char() == '\n':
            self.line += 1
        self.position += 1
    
    def add_token(self, type, value=None):
        self.tokens.append(Token(type, value, self.line))
    
# Add this helper method to check if a character is an emoji or Unicode
    def is_unicode_identifier_char(self, char):
        if char is None:
            return False
        if char.isidentifier() or char.isdigit() or char == '_':
            return True
    # Check for emojis and other Unicode characters
        code = ord(char)
        return code > 127  # All non-ASCII characters

# Then update handle_identifier:
# state_lexer.py - replace the handle_identifier method:

    def handle_identifier(self):
        start = self.position
    
    # Check if first character is valid for identifier start
        char = self.current_char()
        if not (char.isalpha() or char == '_' or self.is_emoji(char)):
            self.add_token(TokenType.ERROR, char)
            self.advance()
            return
    
    # Read the rest of the identifier
        while self.current_char() and (self.current_char().isalnum() or 
                                  self.current_char() == '_' or 
                                  self.is_emoji(self.current_char())):
            self.advance()
    
        value = self.source_code[start:self.position]
        token_type = self.keywords.get(value, TokenType.IDENTIFIER)
        self.add_token(token_type, value)

    def is_emoji(self, char):
        """Check if character is an emoji or other Unicode symbol"""
        if not char:
            return False
        try:
        # Simple check: if it's not ASCII and not a common punctuation
            code = ord(char)
            return (code > 127 and 
                    not char.isspace() and 
                    not char in '=!<>&|+-*(){}[],;:/"\'')
        except:
            return False


    def handle_number(self):
        start = self.position
        is_float = False
        
        # Read integer part
        while self.current_char() and self.current_char().isdigit():
            self.advance()
        
        # Check for decimal point
        if self.current_char() == '.' and self.peek_char() and self.peek_char().isdigit():
            is_float = True
            self.advance()  # Skip the dot
            while self.current_char() and self.current_char().isdigit():
                self.advance()
        
        value = self.source_code[start:self.position]
        token_type = TokenType.FLOATLIT if is_float else TokenType.INTLIT
        self.add_token(token_type, value)
    
    def handle_string(self):
        self.advance()  # Skip opening quote
        value_chars = []
        
        while self.current_char() and self.current_char() != '"':
            if self.current_char() == '\\':
                self.advance()  # Skip backslash
                if self.current_char():
                    # Handle escape sequences
                    escape_map = {
                        'n': '\n', 't': '\t', 'r': '\r',
                        '"': '"', '\\': '\\', "'": "'"
                    }
                    value_chars.append(escape_map.get(self.current_char(), self.current_char()))
                    self.advance()
            else:
                value_chars.append(self.current_char())
                self.advance()
        
        if not self.current_char() or self.current_char() != '"':
            raise Exception(f"Unterminated string literal at line {self.line}")
        
        self.advance()  # Skip closing quote
        self.add_token(TokenType.STRINGLIT, ''.join(value_chars))
    
    def handle_comment(self):
        if self.peek_char() == '/':  # Single-line comment
            self.advance()  # Skip first /
            self.advance()  # Skip second /
            while self.current_char() and self.current_char() != '\n':
                self.advance()
        elif self.peek_char() == '*':  # Multi-line comment
            self.advance()  # Skip /
            self.advance()  # Skip *
            while self.current_char() and not (self.current_char() == '*' and self.peek_char() == '/'):
                if self.current_char() == '\n':
                    self.line += 1
                self.advance()
            if self.current_char() == '*':
                self.advance()
            if self.current_char() == '/':
                self.advance()
        else:
            self.add_token(TokenType.DIVIDE, '/')
            self.advance()
    
    def handle_operator(self):
        char = self.current_char()
        next_char = self.peek_char()
        
        two_char_ops = {
            '==': TokenType.EQUALSOP,
            '!=': TokenType.NOTEQUALS,
            '<=': TokenType.LESSEQUAL,
            '>=': TokenType.GREATEREQUAL,
            '&&': TokenType.AND,
            '||': TokenType.OR,
        }
        
        one_char_ops = {
            '=': TokenType.ASSIGNOP,
            '<': TokenType.LESSTHAN,
            '>': TokenType.GREATERTHAN,
            '!': TokenType.NOT,
            '+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '*': TokenType.MULTIPLY,
            '/': TokenType.DIVIDE,
        }
        
        if next_char and char + next_char in two_char_ops:
            op = char + next_char
            self.add_token(two_char_ops[op], op)
            self.advance()
            self.advance()
        elif char in one_char_ops:
            self.add_token(one_char_ops[char], char)
            self.advance()
        else:
            self.add_token(TokenType.ERROR, char)
            self.advance()
    
    def tokenize(self):
        while self.current_char() is not None:
            char = self.current_char()
            
            # Skip whitespace
            if char.isspace():
                self.advance()
                continue
            
            # Handle identifiers and keywords
            if char.isalpha() or char == '_':
                self.handle_identifier()
            
            # Handle numbers
            elif char.isdigit():
                self.handle_number()
            
            # Handle strings
            elif char == '"':
                self.handle_string()
            
            # Handle comments and division operator
            elif char == '/':
                self.handle_comment()
            
            # Handle operators
            elif char in '=!<>&|+-*':
                self.handle_operator()
            
            # Handle single character tokens
            elif char == '(':
                self.add_token(TokenType.PARENL, char)
                self.advance()
            elif char == ')':
                self.add_token(TokenType.PARENR, char)
                self.advance()
            elif char == '{':
                self.add_token(TokenType.BRACEL, char)
                self.advance()
            elif char == '}':
                self.add_token(TokenType.BRACER, char)
                self.advance()
            elif char == '[':
                self.add_token(TokenType.BRACKETL, char)
                self.advance()
            elif char == ']':
                self.add_token(TokenType.BRACKETR, char)
                self.advance()
            elif char == ',':
                self.add_token(TokenType.COMMA, char)
                self.advance()
            elif char == ';':
                self.add_token(TokenType.SEMICOLON, char)
                self.advance()
            elif char == ':':
                self.add_token(TokenType.COLON, char)
                self.advance()
            
            else:
                # Invalid character
                self.add_token(TokenType.ERROR, char)
                self.advance()
        
        self.add_token(TokenType.EOF, None)
        return self.tokens
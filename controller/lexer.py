from controller.token import (
    Token,
    TokenType
)

from model.Error import Error

ErrorList = []

class Lexer:
    
    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0
        self._line: int = 0
        self._column: int = 0
        
        self._read_character()
            
    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]
            self._position = self._read_position
            self._column += 1
            self._read_position += 1
            
    # state 0
    def next_token(self) -> Token:
        self._skipWhitespace()
        
        if (self._character == '' ):
            token = Token(TokenType.EOF, '')
        else: 
        # state 1
            if (self._character == '{'):
                token: Token = Token(TokenType.LBRACE, self._character)
            # state 2
            elif (self._character == '}'):
                token: Token  = Token(TokenType.RBRACE, self._character)
            # state 3
            elif (self._character == '[' ):
                token: Token  = Token(TokenType.LBRACKET, self._character)
            # state 4
            elif (self._character == ']'):
                token: Token  = Token(TokenType.RBRACKET, self._character)
            # state 5
            elif (self._character == ':'):
                token: Token  = Token(TokenType.COLON, self._character)
            # state 6
            elif (self._character == ','):
                token: Token  = Token(TokenType.COMMA, self._character)
            # states 7 - 12
            else:
                # state 8, 12
                if self._isNumber(self._character):
                    token: Token  = Token(TokenType.NUMBER, self._readNumber() )
                    return token
                 # states 7, 9, 10
                elif self._isLetter(self._character):
                    token: Token  = Token(TokenType.LETTER, self._readIdentifier())
                    return token
                # Error
                else:
                    token = Token(TokenType.ILLEGAL, self._character)
                    error = Error(self._character, self._line, self._column)
                    ErrorList.append(error)
            
        self._read_character()
        return token
    
    def _skipWhitespace(self) -> None:
        while self._character in [' ', '\t', '\n', '\r']:
            if self._character == '\n':
                self._line += 1
                self._column = 0
            self._read_character()
            
    def _readIdentifier(self) -> str:
        position = self._position
        while self._isLetter(self._character):
            self._read_character()
        return self._source[position:self._position]
    
    def _readNumber(self) -> str:
        position = self._position
        while self._isNumber(self._character):
            self._read_character()
        return self._source[position:self._position]
    
    def _isLetter(self, character: str) -> bool:
        return 'a' <= character <= 'z' or 'A' <= character <= 'Z' or '0' <= character <= '9' or character == '"'
    
    def _isNumber(self, character: str) -> bool:
        return '0' <= character <= '9' or character == '.' or character == '-'
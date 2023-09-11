from controller.lexer import Lexer
from controller.token import (
    Token,
    TokenType
)
from controller.parser import start_evaluate

EOF_TOKEN: Token = Token(TokenType.EOF, '')

def start_repl(jsonString) -> None:
    
    tokens = []  # List to store the tokens
    tokensView = []
    
    lexer: Lexer = Lexer(jsonString)
    while (token := lexer.next_token()) != EOF_TOKEN:
        tokens.append(token)
        tokensView.append(token)
        
    start_evaluate(tokens)
    return tokensView
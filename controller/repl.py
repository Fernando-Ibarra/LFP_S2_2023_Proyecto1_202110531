from controller.lexer import Lexer
from controller.token import (
    Token,
    TokenType
)
from controller.parser import start_evaluate


EOF_TOKEN: Token = Token(TokenType.EOF, '')

def start_repl() -> None:
    # Read the JSON string from the file
    with open('./prueba.json', 'r') as file:
        jsonString = file.read()
        
    tokens = []  # List to store the tokens
    
    lexer: Lexer = Lexer(jsonString)
    while (token := lexer.next_token()) != EOF_TOKEN:
        tokens.append(token)
        print(token)
    
    start_evaluate(tokens)
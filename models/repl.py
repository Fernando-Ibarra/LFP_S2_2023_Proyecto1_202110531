from models.lexer import Lexer
from models.token import (
    Token,
    TokenType
)

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
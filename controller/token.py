from enum import (
    auto,
    Enum,
    unique
)

from typing import NamedTuple

@unique
class TokenType(Enum):
    ILLEGAL = auto()
    EOF = auto()
    
    # Identifiers + literals
    LETTER = auto()
    NUMBER = auto()
    
    # Delimiters
    COMMA = auto()
    COLON = auto()
    LBRACKET = auto()
    LBRACE = auto()
    RBRACKET = auto()
    RBRACE = auto()
    PERIOD = auto() 


    
class Token(NamedTuple):
    token_type: TokenType
    literal: str
    
    def __str__(self) -> str:
        return f"Type: { self.token_type }, Literal: { self.literal }"
    
    def getLiteral(self) -> str:
        return self.literal
    
    def getType(self) -> TokenType:
        return self.token_type
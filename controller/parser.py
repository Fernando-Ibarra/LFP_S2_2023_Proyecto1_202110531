from controller.token import (
    Token,
    TokenType
)

from model.Operation import Operation

operationList = []

def start_evaluate(tokens_input = [], prevOperation = None) -> Operation:
    
    index: int = 0
    tokens = tokens_input

    currentOperation = Operation(fatherOperation=prevOperation)
    
    while len(tokens):
        token: Token = tokens.pop(0)
        
        if token.getType() == TokenType.RBRACE:
            if currentOperation.fatherOperation is None:
                operationList.append(currentOperation)
                return start_evaluate(tokens, None)
        
        if token.getType() == TokenType.RBRACKET:
            
            if currentOperation.operation is None:
                # TODO: SETTINGS GRAPHVIZ PARSER
                return
        
            return currentOperation
        
        if token.getType() == TokenType.LETTER and token.getLiteral() =='"operacion"':
            res: str = tokens[1].getLiteral()
            res: str = res.replace('"', '')
            currentOperation.operation = res
        
        if token.getType() == TokenType.LETTER and token.getLiteral() == '"valor1"':
            valueToken: Token = tokens[1]
            
            if valueToken.getType() == TokenType.NUMBER:
                currentOperation.value1 = float(valueToken.getLiteral())
            else:
                currentOperation.value1 = start_evaluate(tokens, currentOperation)
        
        if token.getType() == TokenType.LETTER and token.getLiteral() == '"valor2"':
            valueToken: Token = tokens[1]
            
            if valueToken.getType() == TokenType.NUMBER:
                currentOperation.value2 = float(valueToken.getLiteral())
            else:
                currentOperation.value2 = start_evaluate(tokens, currentOperation)
        
        index += 1
    
    return currentOperation
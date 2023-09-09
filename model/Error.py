class Error:
    
    def __init__(self, lexema: str, row: int, column: int) -> None:
        self._lexema: str = lexema
        self._row: int = row
        self._column: int = column

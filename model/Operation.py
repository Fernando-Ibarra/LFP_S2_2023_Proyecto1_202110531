import numpy as np

class Operation:
    
    value1: float
    value2: float
    
    def __init__(self, operation: str = None, value1: float  = None, value2: float = None, fatherOperation = None) -> None:
        self.operation = operation
        self.value1 = value1
        self.value2 = value2
        self.fatherOperation = fatherOperation
        
    def __str__(self):
        return f"Operation: { self.operation }, Value1: { self.value1 }, Value2: { self.value2 }, FatherOperation: { self.fatherOperation }"

    def traverse(self):

        out = ""

        out += "("
        if isinstance(self.value1, Operation):
            out += self.value1.traverse()
        else:
            out += str(self.value1)

        out += ")"
        
        try:
            out += self.operation
        except:
            print("Error", str(self))
            out+="xxxx"

        out +="("
        if isinstance(self.value2, Operation):
            out += self.value2.traverse()
        else:
            out += str(self.value2)

        out += ")"

        return out

    def getResult(self):

        leftVal = None
        rightVal = None

        if isinstance(self.value1, Operation):
            leftVal = self.value1.getResult()
        elif isinstance(self.value1, float):
            leftVal = self.value1

        if isinstance(self.value2, Operation):
            rightVal = self.value2.getResult()
        elif isinstance(self.value2, float):
            rightVal = self.value2

        self.result = self.operation_result(self.operation, leftVal, rightVal)
        return self.result
      
    def operation_result(self, typeOperation = '', val1 = None, val2 = None ):
        res = 0
        
        if typeOperation == "suma":
            res = val1 + val2
        
        if typeOperation == "resta":
            res = val1 - val2
        
        if typeOperation == "multiplicacion":
            res = val1 * val2
        
        if typeOperation == "division":
            res = val1 / val2
            
        if typeOperation == "potencia":
            res = val1 ** val2
        
        if typeOperation == "raiz":
            res = np.sqrt(val1)
            
        if typeOperation == "inverso":
            res = 1 / val1
        
        if typeOperation == "seno":
            res = np.sin(val1)
        
        if typeOperation == "coseno":
            res = np.cos(val1)
        
        if typeOperation == "tangente":
            res = np.tan(val1)
        
        if typeOperation == "mod":
            res = val1 % val2

        return res

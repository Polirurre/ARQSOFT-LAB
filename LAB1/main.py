from Expressions.SimpleExpression import SimpleExpression
from Operands.Operand import Operand
from Operands.Number import Number
from Operators.Operator import Operator
from Expressions.Computation import Computation

def main():
    operand1 = Number(15)
    operand2 = Number(5)
    operand3 = Number(20)
    operand4 = Number(10)
    operator = Operator("+")  
    
    computation1 = Computation(operand1, operator, operand2)
    computation2 = Computation(operand3, operator, operand4)

    result1 = computation1.evaluate(None)  
    result2 = computation2.evaluate(None)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()

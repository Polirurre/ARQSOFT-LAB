from SimpleExpression import SimpleExpression
from Operand import Operand
from MyNumber import MyNumber
from Operator import Operator
from Computation import Computation

def main():
    operand1 = MyNumber(15)
    operand2 = MyNumber(5)
    operand3 = MyNumber(20)
    operand4 = MyNumber(10)
    operator = Operator("+")  
    
    computation1 = Computation(operand1, operator, operand2)
    computation2 = Computation(operand3, operator, operand4)

    result1 = computation1.evaluate(None)  
    result2 = computation2.evaluate(None)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()

from Expressions.SimpleExpression import SimpleExpression
from Operands.Operand import Operand
from Operands.Number import Number
from Operands.Variable import Variable
from Operators.Operator import Operator
from Expressions.Computation import Computation
from Memory import Memory
from Expressions.Assignment import Assignment

def main():
    memory = Memory()

    operand1 = Number(15)
    operand2 = Number(5)
    operator = Operator("+")  
    computation1 = Computation(operand1, operator, operand2)
    result1 = computation1.evaluate(None)  
    print(result1)

    variable1 = Variable("A")
    operand1 = Number(10)
    operand2 = Number(20)
    operator = Operator("+")
    assignment1 = Assignment(variable1, operand1, operator, operand2)
    result2 = assignment1.evaluate(None)
    print(result2)
    
if __name__ == "__main__":
    main()

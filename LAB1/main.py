import MyNumber
import Operator
import Computation

if __name__ == "__main__":
    number = MyNumber.MyNumber(5)
    print(number.get_value())

    op = Operator.Operator("+")
    print(op.compute(10, 5))  
    op.set_operation("*")
    print(op.compute(10, 5)) 




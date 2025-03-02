class Assignment:
    def __init__(self, variable, first_operand, operator, second_operand):
        """
        Constructor of Assignment.

        Parameters:
        variable: the variable to which the result of operating the two operands is assigned to
        first_operand: the first operand
        operator: the operator
        second_operand: the second operand
        """
        self.variable = variable
        self.first_operand = first_operand
        self.operator = operator
        self.second_operand = second_operand

    def evaluate(self, memory):
        if None in (self.variable, self.first_operand, self.operator, self.second_operand):
            raise Exception("One or more components of the expression are None")

        # Assuming Operator class has a static method compute
        result = self.operator.compute(self.first_operand, self.second_operand)
        memory[self.variable] = result
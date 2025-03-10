class Assignment:
    def __init__(self, variable, first_operand, operator, second_operand):
        self.variable = variable
        self.first_operand = first_operand
        self.operator = operator
        self.second_operand = second_operand

    def evaluate(self, memory):
        if self.variable is None or self.first_operand is None or self.operator is None or self.second_operand is None:
            raise Exception("Invalid expression: None value found")

        # Assuming operator has a compute method that takes two operands and returns the result
        result = self.operator.compute(self.first_operand, self.second_operand)

        # Assign the result to the variable in memory
        memory[self.variable] = result
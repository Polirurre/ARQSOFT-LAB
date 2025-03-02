class Memory:
    def __init__(self):
        self.variables = {}

    def add_variable(self, variable):
        self.variables[variable.name] = variable

    def get_variable(self, name):
        return self.variables.get(name, None)

    def __str__(self):
        return str(self.variables)
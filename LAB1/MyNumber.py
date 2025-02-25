class MyNumber():
    value: float

    function __init__(self, value):
        self.value = float(value)
    
    function getValue(self):
        return self.value


mi_numero = MyNumber(15)
print(f"atributo value {mi_numero.getValue()}")
posible_valor_estatico = MyNumber.value
print(posible_valor_estatico)
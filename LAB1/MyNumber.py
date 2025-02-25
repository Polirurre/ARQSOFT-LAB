class MyNumber():

    def __init__(self, value: float):
        self.value = float(value)
    
    def getValue(self) -> float:
        return self.value

mi_numero = MyNumber(15)
print(f"atributo value: {mi_numero.getValue()}")
#posible_valor_estatico = MyNumber.value
#print(posible_valor_estatico)
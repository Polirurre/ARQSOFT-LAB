from Content.Content import Content

class NumericalContent(Content):
    def __init__(self, number : float):
        super(). __init__(number)


    def getValue(self) -> float:
        return self.value
    
    def setValue(self, value: float) -> None:
        self.value = value
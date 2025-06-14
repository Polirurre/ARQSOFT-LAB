#from FormulaController.PostfixEvaluator import EvaluatePostfix
from Content.Content import Content

class FormulaContent(Content):
    def __init__(self, formula: str):
        self.formula = formula
        self.value = None
        self.expression = []
        pass

    
    def getValue(self) -> float:
        return self.value

    def getFormula(self) -> str:
        return self.formula
    
    def setFormula(self, formula: str) -> None:
        self.formula = formula

    #def setValue(self, formula: str) -> None:
    #    self.value = EvaluatePostfix(formula)

    def __repr__(self) -> str:
        return f"FormulaContent(formula={self.formula}, value={self.value})"
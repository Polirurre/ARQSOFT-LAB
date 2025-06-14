from src.FormulaController.PostfixEvaluator import PostfixEvaluator
from .Parser import Parser
from .GeneratePostfix import GeneratePostfix
from .Tokenizer import Tokenizer

class FormulaManager:
    def __init__(self):
        self.tokenize = Tokenizer()
        self.parse = Parser()
        self.generatePostfix = GeneratePostfix()
        self.evaluator = PostfixEvaluator()
        pass

    def computeFormula(self, formula, context=None):
        token_list = self.tokenize.tokenize(formula)
        parsed_list = self.parse.parse(token_list)
        postfix = self.generatePostfix.infixToPostfix(parsed_list)
        result = self.evaluator.evaluate(postfix, context)
        return result
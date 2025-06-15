from Content.NumericalContent import NumericalContent
from Content.TextContent import TextContent
from Content.Content import Content
from FormulaController.GeneratePostfix import GeneratePostfix
from FormulaController.Parser import Parser
from FormulaController.Tokenizer import Tokenizer
from Spreadsheet.Cell import Cell
from Spreadsheet.Coordinate import Coordinate
from Spreadsheet.Spreadsheet import Spreadsheet

# Main function
def main():

    spreadsheet = Spreadsheet("test.s2v")

    spreadsheet.set("A1", "Hello")

    spreadsheet.set("A2", "2")

    formula = "A4-B2/SUM(A2:A4;B4)"
    tokenizer = Tokenizer(formula)
    tokens = tokenizer.tokenize()
    print(tokens)
    parser = Parser(tokens)
    #formula_tokens = ['1.05', '+', 'A1', '*', '(', '(', 'SUMA', '(', 'A2', ':', 'B5', ';', 'PROMEDIO', '(', 'B6', ':', 'D8', ')', ';', 'C1', ';', '27', ')', '/', '4', ')', '+', '(', 'D6', '-', 'D8', ')', ')']
    gen_postfix = GeneratePostfix(tokens)
    postfix_expression = gen_postfix.generate_postfix()
    print(postfix_expression)

if __name__ == "__main__":
    main()
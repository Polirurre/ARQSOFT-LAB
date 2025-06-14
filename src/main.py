from Content.NumericalContent import NumericalContent
from Content.TextContent import TextContent
from Content.Content import Content
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

    print(spreadsheet.get("A1"))

    print(spreadsheet.get("A2"))

    formula = "=1.05 + A1*((SUMA(A2:B5;PROMEDIO(B6:D8);C1;27)/4)+(D6-D8))"
    tokenizer = Tokenizer(formula)
    tokens = tokenizer.tokenize()
    print(tokens)
    parser = Parser(tokens)
    try:
        parsed_tokens = parser.parse()
        print("Syntax is correct:", parsed_tokens)
    except SyntaxError as e:
        print("Syntax error:", e)

if __name__ == "__main__":
    main()
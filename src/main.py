from Content.NumericalContent import NumericalContent
from Content.TextContent import TextContent
from Content.Content import Content
from Controller.SpreadSheetController import SpreadsheetController
from FormulaController.GeneratePostfix import GeneratePostfix
from FormulaController.Parser import Parser
from FormulaController.Tokenizer import Tokenizer
from Spreadsheet.Cell import Cell
from Spreadsheet.Coordinate import Coordinate
from Spreadsheet.Spreadsheet import Spreadsheet
from UI.Terminal import Terminal
from UI.UI import UI

# Main function
def main():

    #spreadsheet = Spreadsheet("test.s2v")
#
    #spreadsheet.set("A1", "Hello")
#
    #spreadsheet.set("A2", "2")
    #spreadsheet.set("C4", "5")

    #print(spreadsheet.get("A1"))

    #userInterface=UI(spreadsheet).display()
    #terminal = Terminal().display()

    sc=SpreadsheetController()
    sc.display_spreadsheet()

    #formula = "A4-B2/SUM(A2:A4;B4)"
    #tokenizer = Tokenizer(formula)
    #tokens = tokenizer.tokenize()
    #print(tokens)
    #parser = Parser(tokens)
    #gen_postfix = GeneratePostfix(tokens)
    #postfix_expression = gen_postfix.generate_postfix()
    #print(postfix_expression)

if __name__ == "__main__":
    main()
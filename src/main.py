from Content.NumericalContent import NumericalContent
from Content.TextContent import TextContent
from Content.Content import Content
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

if __name__ == "__main__":
    main()
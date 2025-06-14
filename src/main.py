
from Content.Content import Content
from Content import NumericalContent, TextContent
from Spreadsheet import Cell
from Spreadsheet.Coordinate import Coordinate


def main():
    # Test Coordinate
    coord = Coordinate(1, 2)
    print(f"Coordinate: {coord}")

    # Test Content (assuming it's an abstract/base class)
    try:
        content = Content()
        print(f"Content: {content}")
    except Exception as e:
        print(f"Content instantiation failed (as expected if abstract): {e}")

    # Test NumericalContent
    num_content = NumericalContent(42)
    print(f"NumericalContent: {num_content}")

    # Test TextContent
    text_content = TextContent("Hello, World!")
    print(f"TextContent: {text_content}")

    # Test Cell with NumericalContent
    cell_num = Cell(coord, num_content)
    print(f"Cell with NumericalContent: {cell_num}")

    # Test Cell with TextContent
    cell_text = Cell(Coordinate(3, 4), text_content)
    print(f"Cell with TextContent: {cell_text}")

if __name__ == "__main__":
    main()
from Content.NumericalContent import NumericalContent
from Content.TextContent import TextContent
from Content.Content import Content
from Spreadsheet.Cell import Cell
from Spreadsheet.Coordinate import Coordinate

# Main function
def main():
    # Test Coordinate
    coord = Coordinate("A", 2)
    print(f"Coordinate: {coord}")

    # Test Content (should fail as it's abstract)
    try:
        content = Content("test")
        print(f"Content: {content}")
    except Exception as e:
        print(f"Content instantiation failed (as expected if abstract): {e}")

    # Test NumberContent
    num_content = NumericalContent(42.0)  # Use NumberContent instead of Content
    print(f"NumberContent: {num_content.get_value()}")

    # Test TextContent
    text_content = TextContent("Hello, World!")  # Use TextContent instead of Content
    print(f"TextContent: {text_content.get_value()}")

    # Test Cell with NumberContent
    cell_num = Cell(coord, num_content)
    print(f"Cell with NumberContent: {cell_num}")

    # Test Cell with TextContent
    cell_text = Cell(Coordinate("B", 4), text_content)
    print(f"Cell with TextContent: {cell_text}")

if __name__ == "__main__":
    main()
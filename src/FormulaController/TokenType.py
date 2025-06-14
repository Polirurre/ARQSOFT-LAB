import re
from enum import Enum

class TokenType(Enum):
    OPERATOR = 1
    CELL_IDENTIFIER = 2
    NUMBER = 3
    OPENING_BRACKET = 4
    CLOSING_BRACKET = 5
    COLON = 6
    SEMI_COLON = 7
    COMMA = 8
    FUNCTION_NAME = 9
    RANGE = 10
class Parser:
    def __init__(self):
        """
        Initializes the Parser.

        Data Needed:
            - 

        Exceptions:
            - None

        Returns:
            - None
        """

    def next_token(self, tokens, current_index):
        """
        Retrieves the next token from the token list and advances the current index.

        Data Needed:
            - tokens (list): A list of tokens representing a formula (ex.: ["A1", "+", "B2"]).
            - current_index (int): The current index in the token list.

        Exceptions:
            - None

        Returns:
            - str or None: The next token in the list, or None if no tokens remain.
        """

    def parse(self, tokens):
        """
        Parses the token list by visiting each token to validate syntax and ensure a well-formed formula.

        Data Needed:
            - tokens (list): A list of tokens representing a formula (ex.: ["A1", "+", "B2"]).

        Exceptions:
            - ValueError: If the token list is empty.
            - SyntaxError: If the tokens form an invalid formula (ex.: unbalanced parentheses, invalid operator placement).

        Returns:
            - list: The validated token list representing the parsed formula.
        """

    def visit_function(self, token):
        """
        Processes a function token (ex.: 'SUM', 'AVERAGE') during parsing.

        Data Needed:
            - token (str): The function token to process.

        Exceptions:
            - SyntaxError: If the function token is invalid or misplaced.

        Returns:
            - None
        """

    def visit_coordinate(self, token):
        """
        Processes a cell coordinate token (ex.: 'A1', 'B2') during parsing.

        Data Needed:
            - token (str): The coordinate token to process.

        Exceptions:
            - SyntaxError: If the coordinate token is invalid or misplaced.

        Returns:
            - None
        """

    def visit_number(self, token):
        """
        Processes a number token (ex.: '5', '3.14') during parsing.

        Data Needed:
            - token (str): The number token to process.

        Exceptions:
            - SyntaxError: If the number token is invalid or misplaced.

        Returns:
            - None
        """

    def visit_operator(self, token):
        """
        Processes an operator token (ex.: '+', '-', '*', '/', ':', ';') during parsing.

        Data Needed:
            - token (str): The operator token to process.

        Exceptions:
            - SyntaxError: If the operator token is invalid or misplaced.

        Returns:
            - None
        """

    def visit_parenthesis(self, token):
        """
        Processes a parenthesis token (ex.: '(', ')') during parsing.

        Data Needed:
            - token (str): The parenthesis token to process.

        Exceptions:
            - SyntaxError: If the parenthesis token is invalid or causes unbalanced parentheses.

        Returns:
            - None
        """

    def visit_unknown(self, token):
        """
        Processes an unrecognized token during parsing.

        Data Needed:
            - token (str): The unknown token to process.

        Exceptions:
            - SyntaxError: If the token is unrecognized.

        Returns:
            - None
        """

    def is_function(self, token):
        """
        Checks if the given token represents a function name.

        Data Needed:
            - token (str): The token to check.

        Exceptions:
            - None

        Returns:
            - bool: True if the token is a function name, False otherwise.
        """

    def is_coordinate(self, token):
        """
        Checks if the given token represents a cell coordinate (ex.: 'A1').

        Data Needed:
            - token (str): The token to check.

        Exceptions:
            - None

        Returns:
            - bool: True if the token is a cell coordinate, False otherwise.
        """

    def is_number(self, token):
        """
        Checks if the given token represents a number (integer or decimal).

        Data Needed:
            - token (str): The token to check.

        Exceptions:
            - None

        Returns:
            - bool: True if the token is a number, False otherwise.
        """
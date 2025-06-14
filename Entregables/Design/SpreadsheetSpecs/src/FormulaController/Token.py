class Token:
    def __init__(self, token, sequence):
        """
        Initializes a Token with a token type and its sequence.

        Data Needed:
            - token (int): The token type identifier.
            - sequence (str): The string sequence representing the token (ex.: "A1", "+").

        Exceptions:
            - ValueError: If the token type or sequence is invalid.

        Returns:
            - None
        """
        pass

    def evaluate(self):
        """
        Evaluates the token to compute or validate its value (ex.: cell reference or number).

        Data Needed:
            - None (uses self.token and self.sequence)

        Exceptions:
            - ValueError: If the token cannot be evaluated (ex.: invalid cell reference or number).
            - RuntimeError: If evaluation depends on external context (ex.: undefined cell value).

        Returns:
            - float or int: The computed or validated value of the token.
        """
        pass
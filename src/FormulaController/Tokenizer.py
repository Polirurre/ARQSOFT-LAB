class Tokenizer:
    def __init__(self):
        """
        Initializes the Tokenizer with empty lists for tokens and token information.

        Data Needed:
            - None

        Exceptions:
            - None

        Returns:
            - None
        """
        pass

    def add(self, regex, token):
        """
        Adds a new token type and its associated regular expression pattern.

        Data Needed:
            - regex (str): The regular expression pattern to match tokens.
            - token (int): The token type identifier.

        Exceptions:
            - ValueError: If the regex pattern or token type is invalid.

        Returns:
            - None
        """
        pass

    def tokenize(self, formula):
        """
        Converts a formula string into a list of Token objects based on defined patterns.

        Data Needed:
            - formula (str): The formula string to tokenize (ex.: "A1 + B2 * 2").

        Exceptions:
            - ValueError: If the formula contains invalid or unrecognized characters.

        Returns:
            - list: A list of Token objects representing the tokenized formula.
        """
        pass

    def getTokens(self):
        """
        Retrieves the list of tokenized Token objects.

        Data Needed:
            - None (uses self.tokens)

        Exceptions:
            - None

        Returns:
            - list: The list of Token objects.
        """
        pass
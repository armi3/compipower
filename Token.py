class Token:

    def __init__(self, lexeme, token, token_type):
        self._lexeme = lexeme
        self._token = token
        self._token_type = token_type

    @property
    def lexeme(self):
        return self._lexeme

    @lexeme.setter
    def lexeme(self, val):
        self._lexeme = val

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, val):
        self._token = val

    @property
    def token_type(self):
        return self._token_type

    @token_type.setter
    def token_type(self, val):
        self._token_type = val

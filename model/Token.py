class Token:

    def __init__(self, lexeme, token, token_type, line_num):
        self._lexeme = lexeme
        self._token = token
        self._token_type = token_type
        self._line_num = line_num

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

    @property
    def line_num(self):
        return self._line_num

    @line_num.setter
    def line_num(self, val):
        self._line_num = val

class AST:

    def __init__(self, root):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, token):
        self._root = token

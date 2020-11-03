class Node:

    def __init__(self, token, parent, children):
        self._token = token
        self._parent = parent
        self._children = children

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children


    def append_child(self, child):
        children_copy = children(self).copy()
        children_copy.append(child)
        children(self, children_copy)
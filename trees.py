# coding=utf-8

class BT_Node(object):
    def __init__(self, _value=None):
        self.left = None
        self.right = None
        self.value = _value

class BinaryTree(object):
    """docstring for BinaryTree"""
    def __init__(self):
        self.root = None

    def add(self, _value):
        self.root = self._add(_value, self.root)

    def _add(self, _value, _node=None):
        if _node is None:
            _node = BT_Node(_value)
            return _node

        if _value > _node.value:
            _node.right = self._add(_value, _node.right)
            return _node
        elif _value < _node.value:
            _node.left = self._add(_value, _node.left)
            return _node

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, _node=None):
        if _node is None:
            return
        self._in_order(_node.left)
        print(_node.value)
        self._in_order(_node.right)


if __name__=='__main__':
    tree = BinaryTree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    tree.add(4)
    tree.add(-1)
    tree.add(6)
    tree.in_order()

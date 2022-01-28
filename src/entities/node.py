class Node:
    def __init__(self, character, freq, left=None, right=None):
        self.character = character
        self.freq = freq
        self.left = left
        self.right = right

    @classmethod
    def is_leaf_node(cls, root):
        return root.left is None and root.right is None
    
    def __lt__(self, other):
        return self.freq < other.freq





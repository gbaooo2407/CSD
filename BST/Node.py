from Student import Student
class Node:
    def __init__(self,data:Student,left,right):
        """
        Initialize new node with data and left, right node
        :param data: 1 sinh vien
        :param left:
        :param right:
        """
        self.data = data
        self.left = left
        self.right = right
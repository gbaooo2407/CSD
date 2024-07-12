from Node import Node
from Student import Student
class BST:
    def __init__(self):
        self.root = None
    def visit(self,node:Node):
        """
        In ra gia tri data cua Node
        :param node: node se duoc in ra gia tri
        :return: None
        """
        print(node.data)

    def pre_order(self,node:Node):
        if node == None:
            return
        self.visit(node)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self,node:Node):
        if node == None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        self.visit(node)

    def in_order(self,node:Node):
        if node == None:
            return
        self.in_order(node.left)
        self.visit(node)
        self.in_order(node.right)

    def bft(self,node:Node):
        """
        breadth first traversal
        :param node: node bat dau bft
        :return:
        """
        q = list() # Tao queue
        q.append(node)
        while len(q) > 0:
            # Dequeue
            new_node = q.pop(0) # Dequeue
            if new_node.left is not None:
                q.append(new_node.left) # Enqueue left
            if new_node.right is not None:
                q.append(new_node.right) # Enqueue right
            self.visit(new_node)

    def _insert_node(self,root:Node,node:Node) -> Node :
        """
        Insert node into a tree start from root
        :param root: start node of the tree
        :param node: node to be inserted
        :return: new root
        """
        if root is None: return node
        if node.data.grade > root.data.grade:
            root.right = self._insert_node(root.right,node)
        elif node.data.grade < root.data.grade:
            root.left = self._insert_node(root.left,node)
        return root

    def insert(self,student:Student):
        node = Node(data = student,left = None, right = None)
        self.root = self._insert_node(root = self.root,node=node)

    def bfs(self,id:str,node:Node)->Student:
        """
        breadth-first search
        :param id:
        :param node:
        :return:
        """
        q = list()  # Tao queue
        q.append(node)
        while len(q) > 0:
            # Dequeue
            new_node = q.pop(0)  # Dequeue
            if new_node.data.id == id: return new_node.data
            if new_node.left is not None:
                q.append(new_node.left)  # Enqueue left
            if new_node.right is not None:
                q.append(new_node.right)  # Enqueue right
        return None

    def _balance(self,all_nodes,start_idx,stop_idx):
        if start_idx > stop_idx:
            return
        mid_idx = (start_idx + stop_idx)//2
        self._insert_node(self.root,all_nodes[mid_idx])
        self._balance(all_nodes,start_idx,mid_idx-1) # Lap lai ben trai
        self._balance(all_nodes,mid_idx+1,stop_idx) # Lap lai ben phai
    def balance(self):
        # Buoc 1. Lay toan bo cac node
        q = list()  # Tao queue
        q.append(self.root)
        all_nodes = list()
        while len(q) > 0:
            # Dequeue
            new_node = q.pop(0)  # Dequeue
            all_nodes.append(new_node)
            if new_node.left is not None:
                q.append(new_node.left)  # Enqueue left
            if new_node.right is not None:
                q.append(new_node.right)  # Enqueue right
            self.visit(new_node)
        # Buoc 2. Sort mang theo thu tu tang dan
        all_nodes.sort(key=lambda data:data.grade)
        # Buoc 3. Tao AVL tu danh sach
        self.root = None
        self._balance(all_nodes,0,len(all_nodes)-1)

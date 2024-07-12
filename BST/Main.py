from BST import BST
from Student import Student
from Node import Node
def main():
    bst = BST()
    stu1 = Student(id='SE0001',name='Hieu',grade=6)
    stu2 = Student(id='SE0002',name='Hieu thu 2',grade=1)
    stu3 = Student(id='SE0003',name='Hieu thu 3',grade=2)
    stu4 = Student(id='SE0004',name='Hieu thu 4',grade=5)
    stu5 = Student(id='SE0005',name='Hieu thu 5',grade=3)
    stu6 = Student(id='SE0006',name='Hieu thu 6',grade=9)
    stu7 = Student(id='SE0007',name='Hieu thu 7',grade=7)
    stu8 = Student(id='SE0008',name='Hieu thu 8',grade=8)
    stu9 = Student(id='SE0009',name='Hieu cn',grade=10)
    bst.insert(stu1),    bst.insert(stu2),    bst.insert(stu3),
    bst.insert(stu4),    bst.insert(stu5),    bst.insert(stu6),
    bst.insert(stu7),    bst.insert(stu8),    bst.insert(stu9),
    bst.bft(node=bst.root)
    print("Pre Order:")
    bst.pre_order(node=bst.root)
    print("Post Order:")
    bst.post_order(node=bst.root)
    print("In Order:")
    bst.in_order(node=bst.root)
    print(f'Searching:{bst.bfs(id="SE0007",node=bst.root)}')
def main2():
    bst = BST()
    stu1 = Student(id='SE0001',name='Hieu',grade=1)
    stu2 = Student(id='SE0002',name='Hieu thu 2',grade=2)
    stu3 = Student(id='SE0003',name='Hieu thu 3',grade=3)
    stu4 = Student(id='SE0004',name='Hieu thu 4',grade=4)
    stu5 = Student(id='SE0005',name='Hieu thu 5',grade=5)
    stu6 = Student(id='SE0006',name='Hieu thu 6',grade=6)
    bst.insert(stu1), bst.insert(stu2), bst.insert(stu3),
    bst.insert(stu4), bst.insert(stu5), bst.insert(stu6)
    bst.bft(node=bst.root)
    bst.balance()
    bst.bft(node=bst.root)
if __name__ == '__main__':
    main2()
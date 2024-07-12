class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def addToHead(self, data):
        data = Node(data)
        if self.head is None:
            self.head = data
            return
        current = self.head
        self.head = data
        self.head.next = current

    def addToTail(self, data):
        data = Node(data)
        if self.head is None:
            self.head = data
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = data

    def addAfter(self, p, x):
        new_node = Node(x)
        if self.head is None:
            return
        if self.head.data == p:
            c = self.head
            new_node.next = c.next
            self.head.next = new_node
            return

        current = self.head
        while current is not None:
            if current.data == p:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current.next is not None:
            print(current.data, end=" --> ")
            current = current.next
        print(current.data, end=" --> None")
        return

    def deleteFromHead(self):
        if self.head is None:
            return
        current = self.head
        print(f"deleted {current.data}")
        self.head = current.next

    def deleteFromTail(self):
        if self.head is None:
            return
        current = self.head
        if current.next is None:
            self.head = current.next
            return
        while current.next.next is not None:
            current = current.next
        print(f"deleted {current.next.data}")
        current.next = current.next.next

    def deleteAfter(self, data):
        if self.head is None:
            return

        current = self.head
        c_data = current.data
        while c_data != data:
            current = current.next
            c_data = current.data
        if c_data == data:
            current.next = current.next.next
        else:
            return print(f"{data} is not in linked list.")

    def delete_x(self, x):
        if self.head is None:
            return
        current = self.head
        c_data = current.data
        prev = None
        if c_data == x:
            self.head = current.next
            return

        while c_data != x:
            prev = current
            current = current.next
            c_data = current.data
        prev.next = current.next

    def search(self, x):
        if self.head is None:
            return False
        c = self.head
        while c is not None:
            if c.data == x:
                return True
            c = c.next
        return False

    def count(self):
        current = self.head
        if current is None:
            return 0

        l = 1
        while current.next is not None:
            l += 1
            current = current.next
        return l

    def deleteIndex(self, index):
        if index < 0 or index >= self.count():
            return print("invalid input")
        if index == 0:
            return self.deleteFromHead()

        count = 0
        current = self.head
        while current is not None:
            if count == index - 1:
                current.next = current.next.next
                return
            current = current.next
            count += 1

    def sort(self):
        current = self.head
        if self.head is None:
            return
        elif current.next is self.head:
            return
        else:
            while current.next is not None:
                n = current.next
                while n is not None:
                    if current.data > n.data:
                        temp = current.data
                        current.data = n.data
                        n.data = temp
                    n = n.next
                current = current.next

    def delete_p(self, p):
        if self.head is None:
            return

        current = self.head
        prev = None

        while current:
            if current.data == p:
                if not prev:
                    self.head = current.next
                else:
                    prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next

    def toArray(self):
        lst = []
        if self.head is None:
            return lst
        elif self.head.next is None:
            return lst.append(self.head.data)
        current = self.head
        while current.next is not None:
            lst.append(current.data)
            current = current.next
        lst.append(current.data)
        return lst

    def mergeTwoL(self, l1, l2):
        self.head = l1.head
        current = l1.head
        while current.next is not None:
            current = current.next
        current.next = l2.head
        return self.sort()

    def addBefore(self, p, x):
        data = Node(x)
        if self.head is None:
            return
        if self.head.data == p:
            return self.addToHead(x)

        current = self.head
        prev = current
        while current is not None:
            prev = current
            current = current.next
            if current.data == p:
                data.next = current
                prev.next = data
                return

    def attach(self, l1, l2):
        self.head = l1.head
        current = l1.head
        while current.next is not None:
            current = current.next
        current.next = l2.head
        return

    def max(self):
        if self.head is None:
            return print("None")
        if self.head.next is None:
            return self.head.data
        a = 0
        current = self.head
        while current is not None:
            if a < current.data:
                a = current.data
            current = current.next
        return a

    def min(self):
        if self.head is None:
            return print("None")
        if self.head.next is None:
            return self.head.data
        a = self.head.data
        current = self.head
        while current is not None:
            if a > current.data:
                a = current.data
            current = current.next
        return a

    def sum(self):
        if self.head is None:
            return print("None")
        if self.head.next is None:
            return self.head.data
        a = 0
        current = self.head
        while current is not None:
            a += current.data
            current = current.next
        return a

    def avg(self):
        s = self.sum()
        return round(s / (self.count()), 2)

    def sorted(self):
        prev = None
        current = self.head
        while current:
            if prev and prev.data > current.data:
                return False
            prev = current
            current = current.next
        return True

    def insert(self, z):
        self.addToTail(z)
        return self.sort()

    def reverse(self):
        z = self.toArray()
        z = z[::-1]
        self.head = Node(z[0])
        for i in z[1:]:
            self.addToTail(i)
        return

    def check(self, l1, l2):
        z1 = l1.toArray()
        z2 = l2.toArray()
        if len(z1) != len(z2):
            return False
        for i in range(len(z1)):
            if z1[i] != z2[i]:
                return False
        return True


linked_list = Linked_list()
linked_list.addToTail(1)
linked_list.addToTail(4)
linked_list.addAfter(4, 4)
linked_list.addToTail(2)
linked_list.addToTail(3)
linked_list.addToTail(8)
linked_list.addToTail(5)
# linked_list.addBefore(4, 9)

# linked_list.sort()
# linked_list.delete_p(5)
print(linked_list.search(2))
print(f"L1 count: {linked_list.count()}")
print(linked_list.toArray())

print(linked_list.sorted())

# linked_list.insert(1)
# linked_list.reverse()

l2 = Linked_list()
l2.addToTail(1)
l2.addToTail(4)
l2.addToTail(4)
l2.addToTail(2)
l2.addToTail(3)
l2.addToTail(5)
l2.traverse()

#
# linked_list.attach(linked_list,l2)
# print(f'Max: {linked_list.max()}')
# print(f'Min: {linked_list.min()}')
# print(f'Sum: {linked_list.sum()}')
# print(f'Avg: {linked_list.avg()}')
#
print(f'\n{linked_list.check(linked_list, l2)}')

linked_list.traverse()

# Create nodes
# Create linked list
# add nodes into linked list
# Print the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist():

    def __init__(self):
        self.head = None

    def list_length(self):
        current_node = self.head
        length_list = 0
        while True:
            if current_node.next is None:
                return length_list
            current_node = current_node.next
            length_list +=1

    def addToTail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def addToHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addAfter(self, p, x):
        current_node = self.head
        while current_node is not None:
            if current_node.data == p:
                break
            current_node = current_node.next
        if current_node is None:
            print(f"Node with value {p} not found")
            return
        new_node = Node(x)
        new_node.next = current_node.next
        current_node.next = new_node

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def deleteFromHead(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            del temp

    def deleteFromTail(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            # Only one node in the list
            temp = self.head
            self.head = None
            del temp
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        temp = current_node.next
        current_node.next = None
        del temp

    def deleteAfter(self, target):
        current_node = self.head
        if current_node == None:
            print("Invalid. This linked list is empty")
            return
        while current_node is not None:
            if current_node.data == target:
                if current_node.next is not None:
                    temp = current_node.next
                    current_node.next = temp.next
                    del temp
                    return
                else:
                    print("There isn't any node after this given node")
                    return
            current_node = current_node.next
        print("Node with the given target data not found.")

    def delete_First_node(self, x):
        current_node = self.head
        previous_node = None
        if current_node == None:
            print("This list is empty")
            return
        if current_node.data == x:
            self.head = current_node.next
            del current_node
            return
        while current_node is not None:
            if current_node.data == x:
                previous_node.next = current_node.next
                del current_node
                return True
            previous_node = current_node
            current_node = current_node.next

    def search(self,node):
        current_node = self.head
        position = 0
        if current_node == None:
            print("This list is empty")
            return
        while current_node is not None:
            if current_node.data == node:
                return print(f"This node is find at index {position}")
            current_node = current_node.next
            position += 1
        print("Node with the given target data not found")

    def count(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count +=1
            current_node = current_node.next
        return count

    def delete_position(self,position):
        current_node = self.head
        current_position = 0
        previous_node = None
        if position < 0 or position > self.list_length():
            print("This node is not exist in the list")
            return False
        if current_node == None:
            print("This list is empty")
            return False
        if position == 0:
            self.head = current_node.next
            del current_node
            return True
        while current_position < position:
            previous_node = current_node
            current_node = current_node.next
            current_position += 1
        previous_node.next = current_node.next
        del current_node
        return True

    def sort(self):
        current_node = self.head
        if current_node is None:
            print("This list is empty")
            return False
        if self.list_length() == 1:
            return
        condition = False
        while condition is False:
            condition = True
            current_node = self.head
            while current_node.next is not None:
                if current_node.data > current_node.next.data:
                    temp = current_node.data
                    current_node.data = current_node.next.data
                    current_node.next.data = temp
                    condition = False
                current_node = current_node.next

    def delete_node(self,node):
        current_node = self.head
        previous_node = None
        if current_node is None:
            print("This list is empty")
            return
        while current_node is not None:
            if current_node.data == node:
                if previous_node is None:  # If deleting the head node
                    self.head = current_node.next
                    del current_node
                    current_node = self.head  # Move to the new head node
                else:
                    previous_node.next = current_node.next
                    del current_node
                    current_node = previous_node.next  # Move to the next node
            else:
                previous_node = current_node
                current_node = current_node.next

    def toArray(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    def Merge(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.data <= list2.data:
            merged_head = list1
            list1 = list1.next
        else:
            merged_head = list2
            list2 = list2.next
        current_node = merged_head
        while list1 and list2:
            if list1.data <= list2.data:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next
        current_node.next = list1 or list2
        current_node = merged_head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next

    def addBefore(self, p, x):
        current_node = self.head
        previous_node = None
        if current_node is None:
            print("This list is empty")
            return
        if current_node.data == p:
            new_node = Node(x)
            new_node.next = current_node
            self.head = new_node
            return
        while current_node is not None:
            if current_node.data == p:
                new_node = Node(x)
                previous_node.next = new_node
                new_node.next = current_node
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def Attach(self, list1, list2):
        if not list1.head:
            return list2
        if not list2.head:
            return list1
        current_node = list1.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = list2.head
        return list1

    def max(self):
        current_node = self.head
        max_value = current_node.data
        if current_node is None:
            print("This list is empty")
            return None
        while current_node is not None:
            if current_node.data >= max_value:
                max_value = current_node.data
            current_node = current_node.next
        return max_value

    def min(self):
        current_node = self.head
        min_value = current_node.data
        if current_node is None:
            print("This list is empty")
            return None
        while current_node is not None:
            if current_node.data <= min_value:
                min_value = current_node.data
            current_node = current_node.next
        return min_value

    def avg(self):
        current_node = self.head
        total = 0
        if current_node is None:
            print("This list is empty")
            return None
        while current_node is not None:
            total += current_node.data
            current_node = current_node.next
        return total / self.count()

    def check_sorted(self):
        current_node = self.head
        if current_node is None or current_node.next is None:
            return True
        while current_node.next is not None:
            if current_node.data >= current_node.next.data:
                break
            current_node = current_node.next
        if current_node.next is None:
            return True
        current_node = self.head
        while current_node.next is not None:
            if current_node.data < current_node.next.data:
                return False
            current_node = current_node.next
        return True

    def insert_sortedList(self,data):
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            new_node = self.head
            return
        if current_node.next is None:
            if current_node.data <= new_node.data:
                current_node.next = new_node
            else:
                new_node.next = current_node
                self.head = new_node
            return
        while current_node.next is not None:
            if current_node.data <= new_node.data < current_node.next.data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            else:
                current_node = current_node.next

    def reversed(self):
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def same_linked_list(self,head1,head2):
        while head1 is not None and head2 is not None:
            if head1.data != head2.data:
                return False
            head1 = head1.next
            head2 = head2.next

        if head1 is not None or head2 is not None:
            return False
        return True

def main():
    linked_list = Linkedlist()
    linked_list.addToHead("Bao")
    linked_list.addToTail("Kien")
    linked_list.addAfter("Bao", "Hai Dang")
    linked_list.addBefore("Kien", "An")
    #linked_list.deleteFromTail()
    #linked_list.deleteAfter("Bao")
    #linked_list.delete_First_node("Kien")
    #linked_list.search("An")
    #print(linked_list.count())
    #linked_list.delete_position(2)
    #linked_list.sort()
    #linked_list.delete_node("Kien")
    #print(linked_list.toArray())
    #linked_list.traverse()
    list2 = Linkedlist()
    list2.addToHead(10)
    list2.addToHead(8)
    list2.addToHead(6)
    list2.addToHead(4)
    list2.insert_sortedList(9)

    list3 = Linkedlist()
    list3.addToHead(10)
    list3.addToHead(8)
    list3.addToHead(6)
    list3.addToHead(4)
    list3.insert_sortedList(9)
    #list2.Merge(list2.head,list3.head)
    list2.reversed()
    list3.reversed()
    #list2.traverse()
    #list2.traverse()
    #temp = linked_list.Attach(linked_list,list2)
    #temp.traverse()
    #print(list2.max())
    #print(list2.min())
    #print(list2.avg())
    #print(list2.check_sorted())
    #print(list2.same_linked_list(list2.head, list3.head))
    print(list2)

if __name__ == '__main__':
    main()



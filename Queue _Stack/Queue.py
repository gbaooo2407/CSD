from collections import deque
import time
from queue import Queue

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,value):
        self.buffer.appendleft(value)

    def enqueue_right(self,value):
        self.buffer.append(value)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Cannot dequeue")
            return
        return self.buffer.pop()

    def dequeue_left(self):
        if self.is_empty():
            print("Cannot dequeue")
            return
        else:
            return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def clear(self):
        self.buffer.clear()

    def first(self):
        if self.is_empty():
            print("This queue is empty")
        else:
            return self.buffer[0]

    def traverse(self):
        if self.is_empty():
            print("There is no queue to traverse")
        else:
            for item in self.buffer:
                print(item)

    def orderFood(self):
        while True:
            food = str(input('Please order your food (type "done" to finish): '))
            time.sleep(0.5)
            if food.lower() == "done":
                break
            else:
                self.enqueue(food)

    def serveFood(self):
        while not self.is_empty():
            food = self.dequeue()
            if food is not None:
                print(food)
                time.sleep(2)

def place_orders (orders):
    for order in orders:
        print(order)
        order_q.enqueue(order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while True:
        if len(order_q.buffer) == 0:
            break
        order = order_q.dequeue()
        print("Done: ",order)
        time.sleep(2)

def decimal_to_binary(number):
    q = Queue()
    q.enqueue("1")
    while number:
        number -= 1
        temp = q.first()
        q.dequeue_left()
        q.enqueue_right(temp+ "0")
        q.enqueue_right(temp + "1")

    print(temp)

def main ():
    order = Queue()
    order.orderFood()
    time.sleep(1)
    order.serveFood()




if __name__ == '__main__':
    orders = ["pizza","samosa","pasta","biryani","burger"]
    order_q =Queue()
    place_orders(orders)
    serve_order()
from Queue.node import LinkedListNode


class Queue:
    def __init__(self, value):
        new_node = LinkedListNode(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = LinkedListNode(value)
        if self.length == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        if self.first == self.last:
            self.first = self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.length -= 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next


my_queue = Queue(4)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()


from Stack.node import LinkedListNode


class Stack:
    def __init__(self, value):
        new_node = LinkedListNode(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        node = LinkedListNode(value)
        if self.height == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next


my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack.pop(), '\n')

my_stack.print_stack()

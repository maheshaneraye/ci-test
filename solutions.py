class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def update(self, old, new):
        temp = self.head
        while temp:
            if temp.data == old:
                temp.data = new
                return
            temp = temp.next

    def delete(self, value):
        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp:
            if temp.data == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print(" ".join(result))


ll = LinkedList()

# Input format:
# first line = number of operations
# operations: append x / update old new / delete x / print

n = int(input())

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "append":
        ll.append(int(cmd[1]))

    elif cmd[0] == "update":
        ll.update(int(cmd[1]), int(cmd[2]))

    elif cmd[0] == "delete":
        ll.delete(int(cmd[1]))

    elif cmd[0] == "print":
        ll.display()

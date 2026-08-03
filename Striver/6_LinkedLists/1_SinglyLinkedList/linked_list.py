class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

x = [2, 4, 6, 8]

y = Node(x[0])

print(y.data)
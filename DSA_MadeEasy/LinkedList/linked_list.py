class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
    def add_node(self,data):
        # print("HERE")
        if(self.head is not None):
            node = Node(data)
            node.next = self.head
            self.head = node
        else:
            self.head = Node(data)
    
    def remove_head(self):
        if self.head.next is not None:
            node = self.head
            self.head = self.head.next
            node.next = None
        else:
            self.head = None

    def reverse(self):
        prev = next_n = None
        curr = self.head
        while(curr is not None):
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        self.head = prev

    def print_list(self):
        curr = self.head
        while(curr is not None):
            # print(curr.data,end="->")                    # Python 3
            print(str(curr.data) + "->"),                  # Python 2
            curr = curr.next
        print()

    def reverse_recursively(self,node):
        if node == None or node.next == None:
            return node
        prev = self.reverse_recursively(node.next)
        node.next.next = node
        node.next = None
        return prev
    def wrapper_rev_recursive(self):
        node = self.head
        self.head = self.reverse_recursively(node)    
    
    def remove_last(self):
        prev = curr = self.head

        while(curr.next is not None):
            prev = curr
            curr = curr.next
        prev.next = None

# if __name__ == '__main__()':
s = Sll()
# print("HERE")
s.add_node(1)
s.add_node(2)
s.add_node(3)
s.add_node(4)
s.add_node(5)
s.add_node(6)
s.add_node(7)
s.add_node(8)
s.add_node(9)
s.add_node(10)


s.print_list()

s.remove_head()

s.print_list()

s.reverse()

s.print_list()

print("Wrapper Function")
s.wrapper_rev_recursive()

s.print_list()

s.remove_last()

s.print_list()

        
    

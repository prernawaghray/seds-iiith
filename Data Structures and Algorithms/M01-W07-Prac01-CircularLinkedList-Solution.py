class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self, node):
        self.root = node

    def make_linked_list(self, node, parent):
        if not parent.next or parent.next == self.root:
            node.next = self.root
            parent.next = node
            return
        else:
            self.make_linked_list(node, parent.next)


    def print_cll(self, node):
        print(node.data)
        if node.next and node.next != self.root:
            self.print_cll(node.next)


if __name__ == '__main__':
    Cll = CircularLinkedList(Node(1))
    Cll.make_linked_list(Node(2), Cll.root)
    Cll.make_linked_list(Node(3), Cll.root)
    Cll.make_linked_list(Node(4), Cll.root)
    Cll.make_linked_list(Node(5), Cll.root)
    Cll.make_linked_list(Node(6), Cll.root)
    Cll.make_linked_list(Node(7), Cll.root)
    Cll.make_linked_list(Node(8), Cll.root)


    # Printing the entire list.
    Cll.print_cll(Cll.root)
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def make_linked_list(root, node):
    if root.next is None:
        root.next = node
    else:
        make_linked_list(root.next, node)


def ll_search(root, value):
    """Write your code here to search the Linked List."""


def print_ll(root):
    print(root.data)
    if root.next:
        print_ll(root.next)


if __name__ == '__main__':
    root = Node(1)
    make_linked_list(root, Node(2))
    make_linked_list(root, Node(3))
    make_linked_list(root, Node(4))
    make_linked_list(root, Node(5))

    # Printing the entire list.
    print_ll(root)

    # Searching Linked List
    ll_search(root, 3)
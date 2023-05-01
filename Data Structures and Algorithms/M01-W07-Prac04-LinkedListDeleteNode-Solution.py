class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, node):
        self.root = node

    def make_linked_list(self, node, parent):
        if parent.next is None:
            parent.next = node
        else:
            self.make_linked_list(node, parent.next)

    def ll_search(self, node, value):
        if node.data == value:
            print("Value found!")
            return
        elif node.next:
            self.ll_search(node.next, value)
        else:
            print("Value not found")
            return


    def print_ll(self, node):
        print(node.data)
        if node.next:
            self.print_ll(node.next)

    def node_delete(self, node, parent, value):
        if node.data == value:
            if parent:
                parent.next = node.next
                return
            else:
                self.root = node.next
        else:
            self.node_delete(node.next, node, value)


if __name__ == '__main__':
    ll = LinkedList(Node(1))
    ll.make_linked_list(Node(2), ll.root)
    ll.make_linked_list(Node(3), ll.root)
    ll.make_linked_list(Node(4), ll.root)
    ll.make_linked_list(Node(5), ll.root)
    ll.make_linked_list(Node(6), ll.root)

    # Printing the entire list.
    ll.print_ll(ll.root)

    # Searching Linked List
    ll.ll_search(ll.root, 3)

    # Delete a node
    ll.node_delete(ll.root, None, 3)

    # Deleting value at the root node
    ll.node_delete(ll.root, None, 1)

    # Print after deletion
    ll.print_ll(ll.root)
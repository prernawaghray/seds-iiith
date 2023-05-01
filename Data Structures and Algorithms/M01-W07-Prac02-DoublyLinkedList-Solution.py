class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class DoublyLinkedList:

   def __init__(self):
      self.head = None

   def node_push(self, new_value):
      new_node = Node(new_value)
      new_node.next = self.head
      if self.head is not None:
         self.head.prev = new_node
      self.head = new_node

   def list_print(self, node):
      while node:
         print(node.data)
         last = node
         node = node.next


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.node_push(10)
    dll.node_push(20)
    dll.node_push(40)
    dll.node_push(80)
    dll.node_push(160)
    dll.list_print(dll.head)
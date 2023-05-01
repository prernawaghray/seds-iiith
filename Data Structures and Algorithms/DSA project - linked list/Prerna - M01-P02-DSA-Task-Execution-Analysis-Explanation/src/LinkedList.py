"""
Node Class:
    This is responsible for storing task details in the class and can be added to linked list
"""
class Node:
    #Constructor Implementation
    def __init__(self, Task_Id, Start_Time, End_Time):
        self.Task_Id = Task_Id
        self.Start_Time = Start_Time
        self.End_Time = End_Time
        self.next = None
        self.Exec_Time = self.End_Time - self.Start_Time
"""
LinkedList Class:
    This is responsible for implementing Linked List for the tasks and is used for implementing
    various aggregate operations.

"""
class LinkedList:
    #Constructor Implementation
    def __init__(self):
        self.head = None
        
    #This method will return the head of the linked list
    def get_list_head(self):
        return self.head
    
    #This method is responsible for printing the linked list nodes
    def print_linked_list(self):
        new_dict = {} # creating empty dictionary for printing output in dictionary format
        temp = self.head
        while temp:
            # initialising the dictionary to match the sample output
            new_dict = {"Task_Id": temp.Task_Id, "Start_Time": temp.Start_Time, "End_Time": temp.End_Time}
            print(new_dict)
            temp = temp.next
            
    #This method is responsible for inserting node in the linked list 
    #in the beginning or at end based on the flag as insert_at_starting
    def insert_node(self, node:Node, insert_at_starting=0):
        start_node = node
        if insert_at_starting == 0:
            start_node.next = self.head
            self.head = start_node
        else:
            if self.head == None:
                self.head = start_node
                return
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = start_node


    
    #This method is responsible for printing the linked list nodes in reverse order
    def print_in_reverse(self, node):
        new_dict = {} # creating empty dictionary for printing output in dictionary format
        temp = node
        if node:
            self.print_in_reverse(node.next)
            # initialising the dictionary to match the sample output
            new_dict = {"Task_Id": temp.Task_Id, "Start_Time": temp.Start_Time, "End_Time": temp.End_Time}
            print(new_dict)
        else:
            return

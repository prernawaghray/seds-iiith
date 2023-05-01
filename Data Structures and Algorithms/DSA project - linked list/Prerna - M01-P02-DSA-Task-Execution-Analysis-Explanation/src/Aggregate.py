from src.LinkedList import LinkedList

"""
Aggregate class is responsible for implementating various operations on the linked list
    1. Get Minimum Timed Task Details
    2. Get Maximum Timed Task Details
    3. Get Average of all the execution times of the tasks pushed in the linked list
"""
class Aggregate:
    
    #Initializing linked list object for various operations 
    def __init__(self, linked_list:LinkedList):
        self.linked_list = linked_list
    
    #Function responsible for searching the task having maximum execution time among all the tasks
    def get_maximised_time_task(self):
        temp = self.linked_list.get_list_head()
        max_task_id = temp.Task_Id
        max_task_time = temp.Exec_Time
        while temp is not None:
            if max_task_time < temp.Exec_Time:
                max_task_id = temp.Task_Id
                max_task_time = temp.Exec_Time
            temp = temp.next
        return max_task_id, max_task_time
    
    #Function responsible for searching the task having minimum execution time among all the tasks
    def get_minimised_timed_task(self):
        temp = self.linked_list.get_list_head()
        min_task_id = temp.Task_Id
        min_task_time = temp.Exec_Time
        while temp is not None:
            if min_task_time > temp.Exec_Time:
                min_task_id = temp.Task_Id
                min_task_time = temp.Exec_Time
            temp = temp.next
        return min_task_id, min_task_time


    
    #Function responsible for calculating average of the all execution times of the tasks in the linked list
    def get_average_time_of_all_tasks(self):
        temp = self.linked_list.head
        n = 0
        sum = 0
        while temp is not None:
            n += 1
            sum += temp.Exec_Time
            temp = temp.next
            avg = sum/n

        return avg, sum, n

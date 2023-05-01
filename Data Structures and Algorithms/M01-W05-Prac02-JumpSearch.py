import math

def jump_search(array, x, n):
    """Write your code here."""


if __name__ == '__main__':

    int_arr = list(map(int, input().split(' ')))
    target = int(input())
    
    # Function call
    result = jump_search(int_arr, target, len(int_arr) - 1)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")
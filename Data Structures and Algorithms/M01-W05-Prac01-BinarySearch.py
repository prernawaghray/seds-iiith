# Python Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binary_search(arr, l, r, target):
    """Write your code here"""
    return -1


if __name__ == "__main__":
    # Test array
    int_arr = list(map(int, input().split(' ')))
    n = len(int_arr)
    target = int(input())
    
    # Function call
    result = binary_search(int_arr, 0, len(int_arr) - 1, target)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")
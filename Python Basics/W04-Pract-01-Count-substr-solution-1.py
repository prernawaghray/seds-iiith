def fact(n):
    if (n<=1):
        return 1
    else:
        return n*fact(n-1)


def count_substr(list_len, k):
    # Add your code here
    val1 = fact(list_len)
    val2 = fact(list_len - k)
    return val1/val2

 

if __name__ == '__main__':
    char_list = list(input().split(' '))
    n = len(char_list)
    k = int(input())
    print(int(count_substr(n, k)))
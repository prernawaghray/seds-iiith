def gcd(n1, n2):
	if   n1 == 0: 
		return n2
	elif n2 == 0: 
		return n1
	x = max(n1, n2)
	y = min(n1, n2)

	return gcd(y, x % y)
 

if __name__ == '__main__':
	numbers = list(map(int, input().split(' ')[:2]))
	print(gcd(numbers[0], numbers[1]))

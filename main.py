num = int(input("Input your number: "))
assert num > 0, "Number should be bigger than 0"

while num != 0:
	if num % 2 == 0:
		num /= 2
	else:
		num -= 1
	print(num)

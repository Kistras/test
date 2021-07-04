num = int(input("Input your number: "))
if num <= 0:
	print("Number should be bigger than 0.")
	exit()

while num != 0:
	if num % 2 == 0:
		num /= 2
	else:
		num -= 1
	print(num)

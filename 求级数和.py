def func(x,y):
	s = 1
	for i in range(1,y+1):
		s *= x
	return s
	
def main():
	while 1:
		number = int(input('Please input an even number ranged from 2 to 8(\'0\' for exit):'))
		if number == 0 :
			break
		elif 2 <= number <= 8 and number % 2 == 0:
			n = func(number+1, number) - func(number,number-1)
			print(f"The result is {n}")
		else:
			print("Out of the range")

if __name__ == '__main__':
	main()

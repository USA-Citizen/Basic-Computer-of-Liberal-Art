code = ('s','U','h','a','N','o','G','I','r','k')
while 1:
	ciphertext = input('Please input your ciphertext(\'q\' for exit):\n')
	if 'q' in ciphertext:
		break
	print('The plaintext is:')
	for i in ciphertext:
		if i in code:
			print(list(code).index(i),end='')
		elif i not in code:
			print('?',end='')
	print('\n',end='')
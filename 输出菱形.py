for i in range(1,5,1):
	print('     ',end=' ')
	for j in range(5-i):
		print(' ',end=' ')
	for j in range(1,2*i,1):
		print('*',end=' ')
	print('\n')
for i in range(3,0,-1):
	print('     ',end=' ')
	for j in range(5-i):
		print(' ',end=' ')
	for j in range(1,2*i,1):
		print('*',end=' ')
	print('\n')
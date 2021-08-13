for i in range(1,10):
	for j in range(1,10):
		if j <= i :
			print("{0}*{1}={2}".format(j,i,i*j),end="\t")
	print('\n')
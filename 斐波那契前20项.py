x = 1
y = 1
print(x,y,end=' ')
for i in range(3,21):
	x, y = y, x+y
	print(y,end=' ')
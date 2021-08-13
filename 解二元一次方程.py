print('本程序计算ax^2+bx+c=0的实数根')
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
print('方程%.2fx^2+%.2fx+%.2f=0'%(a,b,c),end='')
delta = b**2-4*a*c
if delta > 0:
	x1 = (-b-delta**0.5)/(2*a)
	x2 = (-b+delta**0.5)/(2*a)
	print('有两个实数根：\n','x1=%.2f x2=%.2f'%(x1,x2))
elif delta == 0:
	x = -b/(2*a)
	print('有一个实数根：\n','x=%.2f'%(x))
else:
	print('无实数根')
input()
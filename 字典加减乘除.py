while 1:
	m = float(input('请输入第一个数字：'))
	n = float(input('请输入第二个数字：'))
	q = input('请输入运算符号加减乘除，若输入其他符号则退出程序:')
	tup = ('+','-','*','/')
	if q not in tup:
		break
	cal = {'+':m+n,'-':m-n,'*':m*n,'/':m/n}
	print('{0}{1}{2}=%.2f'.format(m,q,n)%(cal.get(q)))
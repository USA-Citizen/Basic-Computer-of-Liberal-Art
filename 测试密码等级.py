def secure(password):
	n = len(password)
	step = 0
	if n >= 8:
		step += 1
	for i in range(n):
		if '0' <= password[i] <= '9':
			step += 1
			break
	for i in range(n):	
		if 'a' <= password[i] <= 'z':
			step += 1
			break
	for i in range(n):	
		if 'A' <= password[i] <= 'Z':
			step += 1
			break
	return step
	
while 1:
	password = input('请输入测试密码：（退出请按回车）')
	if password == '':
		break
	result = secure(password)
	print(f'{password}的密码等级是{result}')

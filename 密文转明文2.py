code = ('g','K','a','p','w','x','E','Q','f','t')
while 1:
	d = ''
	s = input('Please input your ciphertext:(\'q\' for exit)\n')
	if (s=='q') :
		break
	for i in range(len(s)):
		if s[i] in code:
			p = code.index(s[i])
			d += str(p)
		else:
			d += '?'
	print('Your plaintext is:\n{0}'.format(d),end='\n')
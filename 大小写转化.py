#>>> ord('a')
#97
#>>> ord('z')
#122
#>>> ord('A')
#65
#>>> ord('Z')
#90

sent = input('输入一串字符:')
for word in sent:
	if 97 <= ord(word) <= 122 :
		word = chr(ord(word)-32)
		print(word,end='')
	elif 65 <= ord(word) <= 90 :
		word = chr(ord(word)+32)
		print(word,end='')
	else:
		print(word,end='')
	
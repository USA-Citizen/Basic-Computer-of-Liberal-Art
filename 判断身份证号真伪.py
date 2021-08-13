factor = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
last = ('1','0','X','9','8','7','6','5','4','3','2')
identity = input('请输入身份证号：')
total = 0
for i in range(0,17,1):
	total += int(identity[i]) *  factor[i]
mod = total % 11
a = last[mod]
b = identity[17]
if a == b :
	if int(identity[16]) % 2 == 0 :
		print('该身份证号为真，且为女性。')
	else:
		print('该身份证号为真，且为男性。')
else:
	print('该身份证号为假。')
import random
def redEnv(k,rest,l):
	m = random.uniform(0,2*rest/l)
	return m

while 1:	
    total = float(input('请输入红包金额：'))
    num = int(input('请输入红包个数：'))
    remain = total
    for i in range(1,num):
        money = redEnv(i,remain,num+1-i)
        remain -= money
        print(f'红包{i}：{money:.2f}')
    print(f'红包{num}: {remain:.2f}')
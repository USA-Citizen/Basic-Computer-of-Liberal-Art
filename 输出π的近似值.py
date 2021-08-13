import math
SumUp = 0
n = 1
num = 1/(2*n-1)
while math.fabs(num) >= 1e-6 :
    if n % 2 == 0:
        SumUp -= num
    else:
        SumUp += num
    n += 1
    num = 1/(2*n-1)
pi = SumUp*4
print("π的近似值为：%.5f"%pi)
input()

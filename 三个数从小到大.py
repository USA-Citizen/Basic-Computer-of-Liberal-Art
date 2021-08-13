x = float(input('x='))
y = float(input('y='))
z = float(input('z='))
LIST = []
LIST.append(x)
LIST.append(y)
LIST.append(z)
LIST.sort(reverse=False)
print(LIST[0],'<',LIST[1],'<',LIST[2],sep='')
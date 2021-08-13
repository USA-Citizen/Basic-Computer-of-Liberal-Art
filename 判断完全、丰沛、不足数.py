while 1:
    integer = int(input('请输入一个整数：'))
    total=0
    for i in range(2,integer):
        if integer % i == 0 :
            total += i
    if total == integer :
        print('{0}为完全数。'.format(integer))
    elif total > integer :
        print('{0}为丰沛数。'.format(integer))
    elif total < integer :
        print('{0}为不足数。'.format(integer))
while 1:
    try:
        x = int(input('please input a number:'))
        print(x)
    except ValueError:
        print('Oops! That wasn\'t a valid number!')
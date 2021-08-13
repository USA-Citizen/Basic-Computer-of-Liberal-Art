def vacant_tri(n):
    if n % 2 == 1:
        x=(n+1)/2-1
        print(' ' * int(x),end='')
        print("#",end='\n')
        for i in range(2, n):
            print(' '*int(((n+1)/2)-i), end = '')
            print ("#", end = '')
            print(int(2*i-1)*" ", end = '')
            print ("#", end = '\n')
        print("#"*n)

if __name__ == '__main__':
    vacant_tri(9)
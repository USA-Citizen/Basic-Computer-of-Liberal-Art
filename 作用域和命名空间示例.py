def scope_test():
    def do_local():
        spam = 'Commercial'
    
    def do_nonlocal():
        nonlocal spam
        spam = 'Industrial'
    
    def do_global():
        global spam
        spam = 'Official'

    spam = 'Farming'
    do_local()
    print(f'After do_local: {spam}')
    do_nonlocal()
    print(f'After do_nonlocal: {spam}')
    do_global()
    print(f'After do_global: {spam}')

scope_test()
print(f'After do_global: {spam}')
# 定义函数的时候，可以指定参数的类型，也可以指定返回的类型
def f(x: int, y: float, z: str = 'trial') -> int: 
    print(f.__annotations__) # 查看函数的每个指定的参数的类型和返回的类型
    print(x, y, z, sep = ' ')

f(19, 10.2, 2)
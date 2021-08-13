class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# 匹配的第一个except语句会被触发
for cls in [B, C, D]:
    try:
        raise cls
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")

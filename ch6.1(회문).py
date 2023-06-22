from LinkedStack import LinkedStack
def pal(str):
    list=LinkedStack()
    ri=LinkedStack()
    str.upper()
    for i in str:
        if (i>="a") & (i<="z"):
            list.push(i)
    for i in str[::-1]:
        if (i>="a") & (i<="z"):
            ri.push(i)
    for i in range(list.size()):
        if not list.pop()==ri.pop():
            return False
    return True
print(pal("ive"))
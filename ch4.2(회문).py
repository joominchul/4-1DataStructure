
#4.2 회문을 검사하는 함수

def pal(str):
    list=[]
    ri=[]
    str.upper()
    for i in str:
        if (i>="a") & (i<="z"):
            list.append(i)
            ri.append(i)
    list.reverse()
    print(list)
    print(ri)
    if list==ri:
        return True
    else:
        return False


print(pal("eye"))

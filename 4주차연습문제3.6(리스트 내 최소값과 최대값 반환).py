def RtSL(li):
    sm=li[0]
    lg=li[0]
    for i in range(len(li)):
        if li[i]>lg:
            lg=li[i]
        if li[i]<sm:
            sm=li[i]
    return (sm,lg)

li=[4,2,6,10,1]
print(RtSL(li))

i = 1
while i < 10:
    print("6 x %d = %d" % (i, 6 * i))
    i += 1
def func(n):
    if n>1:
        return (1/n)+func(n-1)
    else:
        return 1

print(func(10))
from stackClass import Stack

instr = input("문자열 입력:")

str=Stack()
for i in range(len(instr)):
    str.push(instr[i])

print("역순 문자열:",end='')

for i in range(len(instr),0,-1):
    print(str.peek(),end='')
    str.pop()
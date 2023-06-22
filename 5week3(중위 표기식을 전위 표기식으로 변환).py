from stackClass import Stack
from infix2Prefix import precedence,Infix2Prefix

expr = input("입력 수식(공백문자로 분리):")
infix=expr.split(' ')
print(' 중위표기: ',infix)
postfix=Infix2Prefix(infix)
print(' 전위표기:',postfix)


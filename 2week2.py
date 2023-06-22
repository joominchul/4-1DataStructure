global n_recur
global n_iter
import matplotlib.pyplot as plt
# 거듭제곱 순환 함수
def power(x, n):
    global n_recur
    n_recur += 1
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return power(x*x, n/2)
    else:
        return x * power(x*x, (n-1)/2)
# 거듭제곱 반복 함수
def power_iter(x, n):
    global n_iter
    result = 1.0
    for i in range(n):
        n_iter += 1
        result = result * x
    return result
# 실행 횟수 측정
max_n = 2000
step = 100
result_recur = []
for n in range(0, max_n, step): # 2^0, 2^100, 2^200, ... 2^1900
    n_recur = 0
    answer = power(2, n)
    result_recur.append(n_recur) # count
print("순환: ", result_recur)
result_iter = []
for n in range(0, max_n, step): # 2^0, 2^100, 2^200, ... 2^1900
    n_iter = 0
    answer = power_iter(2, n)
    result_iter.append(n_iter) # count
print("반복: ", result_iter)
plt.figure()
plt.plot(result_recur[:], label="Recursion")
plt.plot(result_iter[:], label="Iteration")
plt.xlabel('[Nx100]')
plt.ylabel('[Count]')
plt.show()
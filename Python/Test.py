import time

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# start_time = time.time()
# print(fibo(5))
# end_time = time.time()
# print("time: ", end_time - start_time)

dic = {1:1, 2:1}

def fibo_dp(n):
    if n in dic:
        return dic[n]
    dic[n] = fibo_dp(n-1) + fibo_dp(n-2)
    return dic[n]

start_time = time.time()
print(fibo_dp(5))
end_time = time.time()
print("time: ", end_time - start_time)
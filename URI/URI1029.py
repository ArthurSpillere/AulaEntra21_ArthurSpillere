casos = int(input())

for i in range(casos):
    num = int(input())

    num_fibo = 1
    b = 0

    for j in range(num):
        
        num_fibo_2 = num_fibo + b
        b = num_fibo
        num_fibo = num_fibo_2
    
    calls = 2 * num_fibo_2 - 2
    if num == 1:
        calls = 1

    print(f"fib({num}) = {calls} calls = {b}")

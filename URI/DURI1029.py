#Define função de fibonacci
def fib(num):
    global calls
    calls += 1
    if num == 1:
        return 1

    elif num == 0:
        return 0
    
    else:
        
        return fib(num-1) + fib(num-2)

#Entrada
casos = int(input())
for i in range(casos):
    calls = 0
    num = int(input())
    num_fibo = fib(num)
    #Saída
    print(f"fib({num}) = {calls-1} calls = {num_fibo}")
    # print(f"fib({num}) = {num_fibo} calls = {repeticoes-1}")

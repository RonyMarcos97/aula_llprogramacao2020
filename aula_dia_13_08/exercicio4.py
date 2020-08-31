def fatorial(n):
    x = 1
    for i in range(1, n+1):
        x = x * i
    
    return x

def fatorial_2(n):
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    return f
        
n = int(input('Digite um numero: '))
x = fatorial(n)
print(fatorial_2(n))
print(x)

 

    
    


def fatorial(n):
    x = 1
    for i in range(1, n+1):
        x = x * i
    
    return x
    
def soma_divisores(n):
    soma = 0
    for i in range(1, n+1):
        if n % i == 0:           
            soma += i
    return soma
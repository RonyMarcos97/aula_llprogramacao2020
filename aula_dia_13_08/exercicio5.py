def divisores(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
def soma_divisores(n):
    soma = 0
    for i in range(1, n+1):
        if n % i == 0:           
            soma += i
    return soma

x = int(input('Numero: '))
divisores(x)
print('Soma dos divisores', soma_divisores(x))
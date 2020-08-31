from random import randint
lista = []
for a in range(10):
    n = randint(0, 100)
    lista.append(n)
print(lista)
lista_par = []
lista_impar = []
i = 0
while i <= 9:
    n = lista[i]
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    i += 1
    
print(lista_par)
print(lista_impar)
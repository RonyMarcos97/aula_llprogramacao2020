from random import randint

lista = []
i = 1
while i <= 10:
    n = randint(1, 6)
    lista.append(n)
    i += 1
print(lista)
for a in range(1, 7): # Começa a usar for Rony 
    print('O numero', a, 'aparece', lista.count(a), 'vezes')


'''print(lista)
print('Número 1 foi sorteado', lista.count(1), 'vezes.')
print('Número 2 foi sorteado', lista.count(2), 'vezes.')
print('Número 3 foi sorteado', lista.count(3), 'vezes.')
print('Número 4 foi sorteado', lista.count(4), 'vezes.')
print('Número 5 foi sorteado', lista.count(5), 'vezes.')
print('Número 6 foi sorteado', lista.count(6), 'vezes.')
'''
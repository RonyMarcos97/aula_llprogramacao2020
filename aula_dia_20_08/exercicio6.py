from random import randint

tupla1 = ()
tupla2 = ()

for a in range(5):
    n = randint(1, 100)
    tupla1 += (n, )
    
    n = randint(1, 100)
    tupla2 += (n, )
print(tupla1)
print(tupla2)
tupla3 = tupla1 + tupla2
print(tupla3)
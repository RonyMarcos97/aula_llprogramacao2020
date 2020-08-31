lista = []
i = 1
while i <= 10:
    n = int(input('Digite um número: '))
    lista.append(n)

    i += 1
print(lista)
print('Maior número: ', max(lista))
print('Menor número: ', min(lista))
media = sum(lista) / len(lista)
print('Média da lista:', media)
menores = []
for a in lista:
	if a < media:
		menores.append(a)
print(f'Números menores que a édia: {menores} ')

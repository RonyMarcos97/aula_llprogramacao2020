contatos = {
    'Rony': '(11)2556-1880',
    'Jose': '(11)2557-9018',
    'Frango': '(11)2557-1880'
}
print(contatos['Rony'])  # Para acessar os valores do dicionarios
contatos['Rony'] = '94021-4563'
print()
print(contatos['Rony'])
contatos['Maria'] = '98765-3325'  # Para criar uma chave
print()
print(contatos)
contatos.pop('Maria')  # Remove um valor do dicionario
print()
print(contatos)
print()
a = input('igite a chave: ')
if a in contatos:
    print('A chave existe nos contatos')
else:
    print('A chave não existe')

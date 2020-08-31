salario = float(input('Digite seu salário: '))
if salario > 2000:
    porcento = salario * 7 / 100
    aumento = salario + porcento
    print(f'Seu novo salário será: {aumento} ')
else:
    porcento = salario * 15 / 100
    aumento = salario + porcento
    print(f'Seu novo salário será: {aumento}')

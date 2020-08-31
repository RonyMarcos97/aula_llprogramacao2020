def intercala_numeros(tupla1, tupla2):
    tupla3 = ()

    for a in range(0, 3):
        tupla3 += (tupla1[a], ) + (tupla2[a], )

    return tupla3

tupla1 = (10, 20, 30)
tupla2 = (50, 60, 70)
tupla3 = intercala_numeros(tupla1, tupla2)
print(tupla3)
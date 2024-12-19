listanum = list()
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o valor da POSIÇÂO {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] < menor:
            menor = listanum[c]
        if listanum[c] > maior:
            maior = listanum[c]
print('=-' * 20)
print(f'Numeros digitados: {listanum} ')
print(f'MAIOR numero: {maior} > POSIÇÂO: ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}..', end='')
print()
print(f'Menor numero: {menor} > POSIÇÂO: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}..', end='')
print()

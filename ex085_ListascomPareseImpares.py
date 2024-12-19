from time import sleep
lista = list([[], []])
valor = 0
for c in range(0 , 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor %2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('=-'*30)
print(f'VALORES INPUTADOS: {lista}')
print('Separando PARES e IMPARES e colocando em ordem crescente !!')
sleep(1)
print('...', end ='')
sleep(1)
print('...', end ='')
sleep(1)
print('...')
lista[0].sort()
lista[1].sort()
print(f'PARES: {lista[0]}')
print(f'IMPARES: {lista[1]}')





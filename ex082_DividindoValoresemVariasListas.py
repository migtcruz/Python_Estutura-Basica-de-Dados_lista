lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um valor inteiro: ')))
    resp = str(input('Continuar? [S/N}:'))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print('=-'*25)
print(f'Valores inseridos: {lista}')
print(f'Valores PARES da Lista: {par}')
print(f'Valores IMPARES da Lista: {impar}')




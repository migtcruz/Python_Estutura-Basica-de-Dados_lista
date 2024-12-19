lista = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor repetido! nao adicionada!')
    cont = str(input('Quer continar? [S/N]: ')).strip().upper()
    if cont in 'N':
        break
print('=-' * 25)
lista.sort()
print(f'Valores digitados em ordem crescente: {lista}')



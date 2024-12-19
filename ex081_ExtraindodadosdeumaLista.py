lista = list()
while True:
    n = int(input('Digite um valor inteiro: '))
    lista.append(n)
    cont = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    if cont in 'N':
        break
print('=-' * 20)
print('RESULTADO')
print('=-' * 20)
print (f'QTDE NUMEROS DIGITADOS: {len(lista)}')
lista.sort(reverse=True)
print(f'VALORES DIGITADOS ORDEM DECRESCENTE: {lista}')
if 5 in lista:
    print('Numero 5 aprece na lista.')
else:
    print('Numero 5 nao aparece na lista.')


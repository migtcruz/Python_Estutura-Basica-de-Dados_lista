lista = list()
dados = list()
maisp = maisl = 0
while True:
    lista.append(str(input('Informe seu nome: ')))
    lista.append(float(input('Informe seu peso: ')))
    if len(dados) == 0:
        maisp = maisl = lista[1]
    else:
        if lista[1] > maisp:
            maisp = lista[1]
        if lista[1] < maisl:
            maisl = lista[1]

    dados.append(lista[:])
    lista.clear()
    cont = str(input('Continuar? [S/N]: '))
    if cont in 'Nn':
        break

print('=-' * 30)
print(f'Foram cadastradas {len(dados)} pessoas')
print(f'Maior peso: {maisp} KG <> Nome da pessoa(s): ', end='')
for p in dados:
    if p[1] == maisp:
        print(f' {p[0]} /', end='')
print()
print(f'Menor peso: {maisl} KG <> Nome da pessoa(s): ', end='')
for p in dados:
    if p[1] == maisl:
        print(f' {p[0]} /', end = '')
print()





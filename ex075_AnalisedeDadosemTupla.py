num = (int(input('Digite um valor: ')),
      int(input('Digite mais um valor: ')),
      int(input('Digite outro valor: ')),
      int(input('Digite o ultimo valor: ')))
print('-=-'*20)
print('ANALISE DOS DADOS')
print('-=-'*20)
print(f'Voce digitou os valores: {num}')
print(f'A) O valor 9 aparece: {num.count(9)} vezes')
if 3 in num:
    print(f'B) O valor 3 aparece na {num.index(3)+1}º posição ')
else:
    print('B) O numero 3 não foi digitado !!!')
print(f'C) Os numeros PARES: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')





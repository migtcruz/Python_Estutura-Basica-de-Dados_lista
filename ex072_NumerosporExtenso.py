tupla = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
         'Cinco', 'Seis', 'Sete', 'Oito',
         'Nove', 'Dez')
while True:
    print('-' * 20)
    print('Numeros por Extenso')
    print('-' * 20)
    num = int(input('Digite um numero entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('Tente Novamente !', end = '')
print(f'Numero digitado: {tupla[num]}')
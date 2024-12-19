from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10)
       , randint(1, 10), randint(1, 10))
print(f'O valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO MAIOR valor sorteado: {max(num)}')
print(f'O MENOR valor sorteado: {min(num)}')


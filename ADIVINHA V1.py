from random import randint
from time import sleep
c = randint(0, 5)
v1 = 0

print('-='*20)
print('Bem-Vindo ao seu jogo de adivinhação!')
print('-='*20)

v1 = str(input('Deseja jogar? [S/N]')).upper()
while v1 not in "SsNn":
    print('Por favor, apenas S ou N !!!')
    v1 = str(input('Deseja jogar? [S/N] ')).upper()

if v1 in "Ss":
    print('Maravilha! Vamos começar!')
    sleep(2)
    print('Eu sou o computador e vou escolher um numero entre 0 e 10')
    print('Você terá que adivinhar qual numero é!')
    print('Pensando em um numero...')
    sleep(2)
    v2 = int(input(f'pronto, qual o seu palpite? '))
    while v2 != c:
        if v2 > c:
            print('Quase! Meu numero é menor!')
            v2 = int(input(f'Qual o seu palpite? '))
        if v2 < c:
            print('Quase! Meu numero é maior!')
            v2 = int(input(f'Qual o seu palpite? '))
      
print('Parabéns! Você acertou!')
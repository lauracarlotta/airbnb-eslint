"""
DESAFIO 4
Crie um programa que solicita ao usuário que insira um número inteiro positivo e,
em seguida, calcula e exibe o fatorial desse número. (O fatorial de um número é o
produto de todos os números inteiros positivos de 1 até o próprio número.)
"""

def line():
  print('-' * 30)


def int_number_verify():
  number = False
  while type(number) != int:
    try:
      line()
      number = input('Digite o número de qual fatorial você quer verificar: ')
      number = int(number)
    except (ValueError, TypeError):
      line()
      print(f'ERRO! Por favor, informe um valor inteiro válido!')
  return number


def fatorial(number):
  line()
  fatorial = number

  print(f'{number}! = {number} x ', end='')
  for cont in range(number - 1,  0, -1):
    fatorial *= cont
    print(cont, '= ' if cont == 1 else 'x ', end='')
  print(fatorial)


number_received = int_number_verify()
fatorial(number_received)

def line():
  print('-' * 30)


def int_number_verify():
  number = False
  while type(number) != int:
    try:
      line()
      number = input('Informe um número inteiro: ')
      number = int(number)
    except (ValueError, TypeError):
      line()
      print(f'ERRO! O valor informado anteriormente não é válido!')
  return number


def even_or_odd_number(value):
  if value % 2 == 0:
    print('PAR!')
  else:
    print('ÍMPAR!')


def result():
  int_number = int_number_verify()
  line()
  print(f'O número {int_number} é: ')
  line()
  even_or_odd_number(int_number)


result()

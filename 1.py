"""
DESAFIO 1

Crie um programa que solicita ao usuário que insira três notas (valores de 0 a 10)
e, em seguida, calcule e exiba a média dessas notas.
Além disso, informe ao usuário se ele foi aprovado ou reprovado com base na média
das notas, considerando a média mínima de aprovação como 6.
"""

"""
def float_number_verify(message):
  while True:
    try:
      number = float(input(message))

    except (ValueError, TypeError):
      print('Por favor, digite um número válido!')
      print('-' * 50)
      continue

    else:
      if number < 0 or number > 10:
        print('Por favor, digite um número válido!')
        print('-' * 50)
      else:
        return number
"""

def title(message):
  print('-' * 50)
  print(f'{message:^50}')
  print('-' * 50)
  print()

def float_number_verify(input):
  try:
    number = float(input)

  except (ValueError, TypeError):
    print('Por favor, digite um número válido!')
    print('-' * 50)
    return 0

  else:
    if number < 0 or number > 10:
      print('Por favor, digite um número válido!')
      print('-' * 50)
    else:
      return number

def test_float_number_verify_success_case():
  result = float_number_verify(10)
  expected = 10.0
  assert result == expected

def test_float_number_verify_fail_case():
  result = float_number_verify('a')
  expected = False
  assert result == expected

test_float_number_verify_fail_case()

def grade_point_average(list):
  sum_grade_point = sum(list)
  average_point = sum_grade_point / 3

  print(f'Com média de nota {average_point:.2f}, o(a) aluno(a) foi: ')
  final_color = colors["final"]
  if average_point < 6:
    red = colors["red"]
    message = f'{red}REPROVADA!{final_color}'
  else:
    green = colors["green"]
    message = f'{green}APROVADA!{final_color}'

  return print(message)


notes_list = []
colors = {
    'red' : '\033[31m',
    'green' : '\033[32m',
    'final' : '\033[m'
}

"""title('Por favor, insira as notas do aluno: (Ex: 5.8)')
for cont in range(3):
  number = input(f'Digite a {cont + 1}ª nota: ')
  while True:
    is_valid_float = float_number_verify(number)
    if is_valid_float:
      print('-' * 50)
      notes_list.append(is_valid_float)
      break
    else:
      continue

grade_point_average(notes_list)"""

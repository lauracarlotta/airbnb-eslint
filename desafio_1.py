def title(message):
  print('-' * 50)
  print(f'{message:^50}')
  print('-' * 50)
  print()

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

def grade_point_average(list):
  sum_grade_point = sum(list)
  average_point = sum_grade_point / 3

  print(f'Com média de nota {average_point:.2f}, o(a) aluno(a) foi: ')

  if average_point < 6:
    message = f'{color_list["red"]}'
    message += f'REPROVADA!'
    message += f'{color_list["final"]}'
  else:
    message = f'{color_list["green"]}'
    message += f'APROVADA!'
    message += f'{color_list["final"]}'

  return print(message)


notes_list = []
color_list = {
    'red' : '\033[31m',
    'green' : '\033[32m',
    'final' : '\033[m'
}

title('Por favor, insira as notas do aluno: (Ex: 5.8)')

for cont in range(3):
  student_note = float_number_verify(f'Digite a {cont + 1}ª nota: ')
  print('-' * 50)
  notes_list.append(student_note)


grade_point_average(notes_list)

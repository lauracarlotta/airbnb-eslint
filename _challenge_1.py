def line(symbol):
  print(symbol * 40)


def receveid_numbers():
  numbers_list = []
  cont = 1

  while len(numbers_list) != 3:
    try:
      line('-')
      number = float_number_verify(input(f'Digite a {cont}ª nota: ').strip())
    except (ValueError, TypeError):
      line('-')
      print(f'ERRO! O valor informado anteriormente não é válido!')
    else:
      if number < 0 or number > 10:
        line('-')
        print(f'ERRO! Informe um valor entre o range de 0 até 10.0')
      else:
        line('-')
        numbers_list.append(number)
        cont += 1

  result = sum_three_values(numbers_list)

  return result


def float_number_verify(value):
  input_value = float(value)
  return input_value


def sum_three_values(numbers_list):
    try:
      value = sum(numbers_list)
      return value

    except TypeError:
        msg = "POR FAVOR, digite um valor válido"
        return msg


def grade_point_average(sum_value):
  average_point = sum_value / 3
  print(f'Com média de nota {average_point:.2f}, o(a) aluno(a) foi: ')

  final_color = colors["final"]
  if average_point < 6:
    red = colors["red"]
    message = f'{red}REPROVADA!{final_color}'
  else:
    green = colors["green"]
    message = f'{green}APROVADA!{final_color}'

  return print(f'{message:^40}')

colors = {
  'red' : '\033[31m',
  'green' : '\033[32m',
  'final' : '\033[m'
}

line('=')
print(f'{"INFORME AS NOTAS DOS ALUNOS: ":^40}')
line('=')

grade_point_list  = receveid_numbers()
grade_point_average(grade_point_list)

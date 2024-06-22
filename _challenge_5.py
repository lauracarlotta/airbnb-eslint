from time import sleep

### funções informativas

# Linha de separação
def line():
  print('-' * 50)

# Título
def title(value):
  line()
  print(f'{value:^50}')
  line()

# Contador de Tempo
def time_count():
  cont = 0
  for cont in range(0, 3):
    print(' .', end='')
    sleep(1)
  cont += 1

# Menu de Opções
def menu():
  title('MENU'),
  print("""  1 - Adicionar uma nova tarefa;
  2 - Visualizar todas as tarefas;
  3 - Marcar uma tarefa como concluída;
  4 - Remover uma tarefa;
  5 - Sair do programa.
  """)

  option = int(input('O que você deseja fazer no momento: '))
  return option

# Apresentação de Listas
def items_list(list):
  title('LISTA DE TAREFAS')
  for cont, value in enumerate(list):
    if colors["markee"] in value:
      print(f'[x] {cont + 1} - {value}')
    else:
      print(f'[ ] {cont + 1} - {value}')

# Mensagens ao Usuário
def user_answers(status, item = None, action = None):
  """

  """
  if status == 'positive':
    print(f'{colors["italic"]}{colors["green"]}', end='')
    # time_count()
    message = f'Tarefa {action} com sucesso!'
    print(f'\n{message}', end='')
    print(f'{colors["reset"]}')

  elif status == 'invalid':
    print(f'{colors["red"]}OPÇÃO INVÁLIDA{colors["reset"]}')
    print()

  elif status == 'error':
    print(f'{colors["red"]}POR FAVOR, informe uma opção válida!{colors["reset"]}')
    print()

  elif status == 'informative':
    print(f'{colors["italic"]}{colors["bold"]}', end='')
    # time_count()
    message = f'Ainda não há itens na sua lista de tarefas!'
    print(f'\n{message}', end='')
    print(f'{colors["reset"]}')

  elif status == 'conclude':
    check_item = item
    item_conclude = f'{colors["markee"]}{colors["tachad"]}{check_item}{colors["reset"]}'
    return item_conclude

# ------------------------

### Adicionar, visualizar, marcar e remover tarefas

# Lista vazia
def empty_list():
  user_answers('informative')
  finish_tasks = False
  while finish_tasks != True:
    try:
      print('Deseja adicionar tarefas? ')
      more_tasks = int(input('[1] SIM / [2] NÃO: '))
      if more_tasks == 1:
        add_task()

      elif more_tasks == 2:
        finish_tasks = True

      elif more_tasks < 1 or more_tasks > 2:
        user_answers('invalid')

    except (TypeError, ValueError):
      user_answers('error')


# Adicionar Tarefa - OK
def add_task():
  task = str(input('Informe a tarefa: '))
  task_list.append(task)
  user_answers('positive', action='adicionada')
  return task_list


# Visualizar Tarefa - OK
def view_task():
  if len(task_list) == 0:
    empty_list()

  else:
    return items_list(task_list)


# Concluir tarefa - WIP .
def conclude_task():
  tarefa_concluida = False

  while tarefa_concluida != True:
    items_list(task_list)
    line()

    task_item = int(input('Informe qual das tarefas você deseja concluir: '))
    print(task_item, 'alalalal')

    if task_item == 0 or task_item < 0 or task_item > len(task_list):
      user_answers('invalid')

    else:
      item = task_list[task_item - 1]
      if colors["markee"] in item:
        user_answers('positive', action = 'JÁ ESTÁ CONCLUÍDA')

        # TODO perguntar se quer marcar mais uma tarefa
        """
          Centralizar o markee do conclude dentro da função e solicitar se desejo concluir mais uma tarefa em outra função ou diretamente nos options
        """

      else:
        user_answers('positive', action ='concluída')
        task_list[task_item - 1] = user_answers('conclude', item)
        tarefa_concluida = True

        # TODO perguntar se quer marcar mais uma tarefa
        # TODO Testar todo o index das opções em cenários positivos e negativos


# Remover tarefa - TODO
def remove_task(): # TODO make function
  print(4, 'remove task')
  pass


# Sair do programa - OK
def exit_program():
  print(f'{colors["bold"]}{colors["yellow"]}', end='')
  # time_count()
  print(f'{colors["reset"]}')
  print(f'{colors["bold"]}{colors["yellow"]}{colors["markee"]}', end='')
  print('OBRIGADA POR USAR NOSSO PROGRAMA!', end='')
  print(f'{colors["reset"]}')
  print(f'{colors["bold"]}{colors["yellow"]}{colors["markee"]}', end='')
  print('SISTEMA ENCERRADO.', end='')
  print(f'{colors["reset"]}')

# Escolher opção do programa - OK
def choice_option():
  option = ''
  while not option == 5:
    try:
      option = menu()

      if option == 1:
        add_task()
        finish_tasks = False
        while finish_tasks != True:
          try:
            print('Deseja adicionar mais tarefas? ')
            more_tasks = int(input('[1] SIM / [2] NÃO: '))
            if more_tasks == 1:
              add_task()

            elif more_tasks == 2:
              finish_tasks = True

            elif more_tasks < 1 or more_tasks > 2:
              user_answers('invalid')

          except (TypeError, ValueError):
            user_answers('error')

      elif option == 2:
        view_task()

      elif option == 3:
        if len(task_list) == 0:
          empty_list()

        else:
          conclude_task()

      elif option == 4:
        remove_task()

      # Sair do programa ok
      elif option == 5:
        exit_program()
        break

      else:
        user_answers('invalid')

    except ValueError:
      user_answers('error')

    except KeyboardInterrupt:
      user_answers('error')

# ------------------------

# Variáveis
colors = {
  "bold":   "\33[1m",
  "italic": "\33[3m",
  "markee": "\33[1;3;7;33m",
  "tachad": "\33[9m",
  "red":    "\33[31m",
  "green":  "\33[32m",
  "yellow": "\33[33m",
  "reset":  "\033[0m"
}

task_list = ['lavar a louÇa', 'dAr banho no cachorro', 'pagar as contas']
# task_list = []

# Executar programa
choice_option()

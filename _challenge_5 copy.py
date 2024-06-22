from time import sleep

def add_task():
  line()
  new_task = str(input('Adicione uma tarefa: '))
  task_list.append(new_task.title())
  user_answers('positive', action = 'adicionada')
  line()

  add_more_task = int(input('Deseja adicionar uma nova tarefa? [1] SIM [2] NÃO: '))
  while not add_more_task == 2:
    try:
      if add_more_task == 1:
        new_task = str(input('Adicione uma tarefa: '))
        task_list.append(new_task.title())
        user_answers('positive', action ='adicionada')

        line()
        add_more_task = int(input('Deseja adicionar uma nova tarefa? [1] SIM [2] NÃO: '))

      elif add_more_task == 2:
        pass

      else:
        user_answers('invalid')
        line()
        add_more_task = int(input('Deseja adicionar uma nova tarefa? [1] SIM [2] NÃO: '))

    except ValueError:
      user_answers('error')
      line()
      add_more_task = int(input('Deseja adicionar uma nova tarefa? [1] SIM [2] NÃO: '))

  return task_list


def view_task():
  if len(task_list) == 0:
    user_answers('informative')
    message = 'Deseja adicionar uma tarefa agora? Digite [1] SIM / [2] NÃO: '
    add_new_task = int(input(message))
    try:
      if add_new_task == 1:
        add_task()
      elif add_new_task == 2:
        pass
      else:
        user_answers('invalid')
        print('Deseja adicionar uma tarefa agora? ')
        add_new_task = int(input('Digite [1] SIM / [2] NÃO: '))
        return add_new_task
    except ValueError:
      user_answers('error')
  else:
    items_list(task_list)


def conclude_task():
  if len(task_list) == 0:
    items_list(task_list)
    user_answers('informative')

  else:
      items_list(task_list)
      line()
      conclude_item = False

      while conclude_item != True:
        try:
          task_item = int(input('Informe qual tarefa você deseja concluir: '))
          if task_item == 0:
            user_answers('invalid')

          if task_item >= 1 and task_item <= len(task_list):
            item = task_list[task_item - 1]
            if colors["markee"] in item:
              user_answers('positive', action = 'JÁ ESTÁ CONCLUÍDA')
              conclude_item = True
            else:
              task_list[task_item - 1] = user_answers('conclude', item)
              user_answers('positive', action ='concluída')
              items_list(task_list)
              conclude_item = True

        except (IndexError, ValueError):
          user_answers('error')


def remove_task():
  if len(task_list) == 0:
    items_list(task_list)
    user_answers('informative')

  else:
    items_list(task_list)
    line()
    remove_item = False

    while remove_item != True:
      try:
        task_item = int(input('Informe qual tarefa você deseja remover da lista: '))
        if task_item == 0:
          user_answers('invalid')

        if task_item >= 1 and task_item <= len(task_list):
          del(task_list[task_item - 1])
          user_answers('positive', action='removida')
          items_list(task_list)
          remove_item = True

      except (IndexError, ValueError):
        user_answers('error')

      else:
        if task_item > len(task_list):
          user_answers('invalid')


def exit_program():
  print(f'{colors["bold"]}{colors["yellow"]}', end='')
  time_count()
  print(f'{colors["reset"]}')
  print(f'{colors["bold"]}{colors["yellow"]}{colors["markee"]}', end='')
  print('OBRIGADA POR USAR NOSSO PROGRAMA!', end='')
  print(f'{colors["reset"]}')
  print(f'{colors["bold"]}{colors["yellow"]}{colors["markee"]}', end='')
  print('SISTEMA ENCERRADO.', end='')
  print(f'{colors["reset"]}')


def choice_option():
  option = ''
  while not option == 5:
    try:
      option = menu()

      if option == 1:
        add_task()

      elif option == 2:
        view_task()

      elif option == 3:
        conclude_task()

      elif option == 4:
        remove_task()

      elif option == 5:
        exit_program()
        break

      else:
        user_answers('invalid')

    except ValueError:
      user_answers('error')


def line():
  print('-' * 50)


def title(value):
  line()
  print(f'{value:^50}')
  line()


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


def time_count():
  cont = 0
  for cont in range(0, 3):
    print(' .', end='')
    sleep(1)
  cont += 1


def user_answers(status, item = None, action = None):
  if status == 'positive':
    print(f'{colors["italic"]}{colors["green"]}', end='')
    time_count()
    message = f'Tarefa {action} com sucesso!'
    print(f'\n{message}', end='')
    print(f'{colors["reset"]}')

  elif status == 'invalid':
    print(f'{colors["red"]}OPÇÃO INVÁLIDA{colors["reset"]}')

  elif status == 'error':
    print(f'{colors["red"]}POR FAVOR, informe uma opção válida!{colors["reset"]}')

  elif status == 'informative':
    print(f'{colors["italic"]}{colors["bold"]}', end='')
    time_count()
    message = f'Ainda não há itens na sua lista de tarefas!'
    print(f'\n{message}', end='')
    print(f'{colors["reset"]}')

  elif status == 'conclude':
    check_item = item
    item_conclude = f'{colors["markee"]}{check_item}{colors["reset"]}'
    return item_conclude


def items_list(list):
  title('LISTA DE TAREFAS')
  for cont, value in enumerate(list):
    print(f'{cont + 1} - {value}')


colors = {
  "bold":   '\33[1m',
  "italic": '\33[3m',
  "markee": '\33[1;3;7;33m',
  "tachad": '\33[9m',
  "red":    '\33[31m',
  "green":  '\33[32m',
  "yellow": '\33[33m',
  "reset":  '\033[0m'
}

task_list = []
choice_option()

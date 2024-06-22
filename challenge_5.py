"""
DESAFIO 5
Crie um programa que permita ao usuário gerenciar suas tarefas diárias.
O programa deve oferecer as seguintes funcionalidades:

    Adicionar uma nova tarefa;
    Visualizar todas as tarefas;
    Marcar uma tarefa como concluída;
    Remover uma tarefa;
    Sair do programa.

(Você pode implementar essas funcionalidades usando listas para
armazenar as tarefas e estruturas de controle como loops e condicionais
para interagir com o usuário.)
"""

def menu():
  print("""
  ------------------------------------------------
                        MENU
  ------------------------------------------------
  1 - Adicionar uma nova tarefa;
  2 - Visualizar todas as tarefas;
  3 - Marcar uma tarefa como concluída;
  4 - Remover uma tarefa;
  5 - Sair do programa.
  """)

  option = int(input('O que você deseja fazer no momento: '))

  return option


menu_lista = ['LISTAR PESSOAS', 'CADASTRAR PESSOAS', 'SAIR DO SISTEMA']
arquivo = 'cadastro_de_pessoas.txt'

if not arquivo_existe(arquivo):
	criar_arquivo(arquivo)

menu_list('SISTEMA DE CADASTRO')
while True:
	resposta = menu(menu_lista)
	if resposta == 1:
		# Fazer a leitura do arquivo e listar pessoas já cadastradas
		ler_arquivo(arquivo)

	elif resposta == 2:
		# Cadastrar novos usuários
		menu_list('Novo Cadastro')
		nome = str(input('Nome: '))
		idade = leiaInt('Idade: ')
		cadastrar(arquivo, nome, idade)

	elif resposta == 3:
		# Sair do sistema
		menu_list('Saindo do sistema')
		cont = 0
		for cont in range(0, 3):
			print(' .', end='')
			sleep(1)
		cont += 1
		break

	else:
		print('\033[31mOPÇÃO INVÁLIDA\033[0m')

	sleep(2)

def arquivo_existe(nome_arquivo):
	try:
		# 'rt' - abertura de arquivo para leitura/em em modo texto (read/text)
		abrir_arquivo = open(nome_arquivo, 'rt')
		abrir_arquivo.close()

	except FileNotFoundError:
		return False

	else:
		return True


def criar_arquivo(nome_arquivo):
	try:
		# 'wt+' - neste caso, seria escreva(w - write) um arquivo texto(t - txt) caso ele não exista(+)
		criar_arq = open(nome_arquivo, 'wt+')
		criar_arq.close()

	except:
		print('Houve um erro na criqção do arquivo!')

	else:
		print(f'arquivo {nome_arquivo} criado com sucesso!')


def ler_arquivo(nome_arquivo):
	try:
		arquivo = open(nome_arquivo, 'rt')

	except:
		print('Erro ao ler arquivo')

	else:
		print()
		menu_list('PESSOAS CADASTRADAS')
		print(f'{"NOME:":<30}{"IDADE:":>8}')
		for line in arquivo:
			dado = line.split(';')
			dado[1] = dado[1].replace('\n', '')
			print(f'{dado[0]:<30}{dado[1]:>3} anos')
		# print(arquivo.read())
		# print(arquivo.readlines()) - lista vazia

	finally:
		arquivo.close()

def cadastrar(file, name = 'Desconhecido', age = 0):
	try:
		# 'at+' - neste caso, seria insira(a - append) a info no arquivo texto(t - txt)
		abrir_arquivo = open(file, 'at')

	except:
		print('Houve um erro na abertura do arquivo!')

	else:
		try:
			abrir_arquivo.write(f'{name}; {age}\n')

		except:
			print('Houve um erro na hora de cadastrar os dados!')

		else:
			print(f'NOVO REGISTRO de {name} CADASTRADO!')
			abrir_arquivo.close()




def line(tamanho = 42):
	return "=" * tamanho

def menu_list(txt):
	print(line())
	print(txt.center(len(line())))
	# print(txt.center(42))
	print(line())

def leiaInt(msg):
	while True:
		try:
			num = int(input(msg))

		except (ValueError, TypeError):
			print('\033[31mPor favor, digite uma opção válida!\033[0m')
			continue

		except KeyboardInterrupt:
			print('\nO usuário preferiu não digitar nada!')
			return 0

		else:
			return num

def menu(lista):
	menu_list('MENU')
	cont = 0
	for cont, valor in enumerate(lista):
		print(f'\033[33m{cont + 1}\033[0m - \033[34m{valor}\033[m')
		cont += 1
	print(line())
	opcao = leiaInt('\033[32mOpção: \033[0m')
	return opcao


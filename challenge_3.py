"""
DESAFIO 3
Crie um programa que verifica se uma palavra fornecida pelo usuário é
 um palíndromo ou não.(Um palíndromo é uma palavra que é lida da mesma forma tanto
 da esquerda para a direita quanto da direita para a esquerda.)
"""
def str_word_verify(message):
  while True:
    try:
      word = str(message)

    except (ValueError, TypeError):
      print('Por favor, digite um número válido!')
      print('-' * 50)

    else:
      return word


word = str_word_verify(input('Informe uma palavra (ou frase): '))
word_formatted = word.strip().lower().replace(' ', '')
word_backward = ''.join(reversed(word_formatted))

if word_formatted == word_backward:
  print(f'A palavra ou frase "{word}" \nÉ UM PALÍNDROMO!')
else:
  print(f'A palavra ou frase "{word}" \nNÃO É UM PALÍNDROMO, ', end='')
  print('pois lendo a mesmas de trás para frente, não são iguais!')

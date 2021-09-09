# uso de if, pode ser usado tanto pulando linhas quanto dentro de comandos
# print('?' if ? == ? else '?')
# if ? == ?:
#   print('?')
# else:
# print('?')
# biblioteca time para tempos
# e para datas, date time.

nome = str(input('digite seu nome: ')).strip().lower()
nome = nome.split()

if (nome[0]) == 'felipe':
    print('caraca teu pau deve ser enorme')
else:
    print(f'ah, e ai {nome}')

# listas: são variaveis compostas mutaveis
# para adicionar novos elementos na lista se usa o comando .append('?'), adicionando ao fim da lista
# para adicionar um item antes de algo se usa o .insert(0,'?'), assim todos os ourtos itens vão para o lado
# e o item inserido assume a posição escolhida
# para apagar itens eistem alguns metodos:
# del lanche[?] usa o numero pra apagar
# lanche.pop(?) usado normalmente pra apagar o ultimo mas usando o numero no parenteses se escolhe especificamente,
# se usar sem nada nos parenteses, ele apaga o ultimo item
# lanche.remove('?') remove um item na lista mas com seu nome e não seu numero
# em todos os casos ele vai eliminar a posição do item selecionado e trazer as casas posteriores para tras,
# assim se apaga o 5, o 6 vira 5 e o 7 vira 6 e assim por diante
# se tentar remover um item que não esta la, o programa vai dar erro, para evitar isso é só usar um
# if '?' in lanche:
#   lanche.remove('?')
# para criar uma lista com range da pra fazer assim ?valores = list(range(4,11)) que cria uma lista de 4 até 10
# para organizar uma lista usa se o comando .sort()
# e se quiser na ordem contraria, use .sort(reverse=True)
# para saber a quantidade de elementos na lista use o comando len
# outra forma de usar o for é "for c, v in enumerate(?var):"
# que vai fazer c ser o valor do momento e v ser o valor da variavel
# se quiser criar uma cópia de uma lista pra outra, não use a = b, pois assim as listas se linkam e assim qualquer
# alteração feita em uma será feita na outra também
# para criar uma cópia use a = b[:], pois assim uma cópia é criada e as alterações não alteram uma a outra
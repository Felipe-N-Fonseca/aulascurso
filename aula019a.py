# dicionarios são estruturas semelhante a listas, porem é possivel declarar um indentificador pra
# um valor, para declarar um dicionario: dados = dict() ou dados = {'nome':'josé','idade':25}
# assim pode se chamar ele da seguinte forma: print(dados['nome'])
# o comando append não funciona pra dicionarios ao invés disso, somplesmente declare dados['sexo'] = 'm'
# e se não tiver o elemento 'sexo' ele vai adicionar dentro do dicionario
# para remover elementos de dicionarios usa-se o del
# pode se declarar também ocupando varias linhas, contanto que esteja dentro das chaves
# filme = {
# 'dessa' = 'forma'
# }
# a diferença entre .values() / .keys() / .items()
# é que o values mostra os valores do dicionario
# o keys mostra o indentificador dos valores apenas
# e items mostra tanto os valores quanto as chaves
# pode se usar o for assim: for k,v in dados.items(): print(f'o {k} é {v}') vai mostrar a key e o value
# respectivamente e repetir até chegar no ultimo key
# dentro do dicionario o metodo [:] não funciona, neles é nescessario usar a function .copy()
# para organizar dicionarios, importe de operator o itemgetter, e use ele como key no comando
# sorted(var?, key=?, reverse= true ou false)
# itemgetter(?) coloque o número da parte que quer analizar, nesse caso, key do dicionario é o 0 e o value é 1
# existe uma função para somar todos os valores de uma lista, ele é sum(lista)
# é possivel criar dicionários compostos abrindo chaves dentro dele
# existe uma ajuda interativa no python onde voce pode descobrir pra que serve uma função
# help(?função) ou print(?função.__doc__) e ele vai mostrar tudo sobre o que se procura no prompt
# para adicionar esses docs na sua função para caso outra pessoa use-o, basta dentro da função escrever:
# def função():
#   """
#   COISAS
#   ESCRITAS
#   """
#
# se quiser criar uma variavel opcional numa função basta na declaração dela colocar por exemplo: (a,b,c=0)
# nesse caso se c não receber nada ele vai valer 0
# pode ser declarado qualquer valor no lugar de 0 e esse vai ser assumido pelo sistema
#
# as variaveis podem ser globais ou locais, sendo a global a declarada no programa principal e que pode
# ser usada por todas as funções e a variavel local que só pode ser usada na função que ela foi criada
# quando se usa uma váriavel dentro de uma função que tem o mesmo nome de uma global, é criada uma váriavel local
# naquela função e ela que é usada
# para usar uma variavel global dentro da função ao invés de criar outra, use "global ?var"
#
# para retornar um valor de uma função para o programa principal, use return ?var retornando o valor da
# variavel local usada no return, assim precisa de um receptor assim como quando se chama o input,
# ou simplesmente jogue no print, como: print(funcao())
# para achar o maior e menor é mais facil usando a função max e min
#
#
#
#
# #
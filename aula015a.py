# comando break
# esse comando corta o funcionamento de whille no instante que ele aparece, fazendo assim com que se possa
# criar varias estrulturas condicionais para apenas um whille
# para isso faça whille True: e la no meio dentro de um if por exemplo, digite break que assim que o if for verdadeiro
# o programa encerra o whille

n = s = 0
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    s += n

print(f'a soma dos números digitados é: {s}')

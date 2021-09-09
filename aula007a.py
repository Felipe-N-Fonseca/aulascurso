# os operadores: + adição, - subtração, * multiplicação, /divisão, ** potência,
# //divisão inteira, % resto da divisão
# == para o resultado
# ordem de precedencia: 1° (); 2° **; 3° *, /, //, %; 4° +, -;
# quando quiser fazer uma raiz, use (1/número), porcentagem = (numero por cento) / 100.
# print('q' *5) cria 5 vezes, : coloca entre numero de caracteres, > alinhado a direita,
# < alinhado a esquerda, ^ centralizado, (= entre iguais)
# colocar end='' no ptint para não quebrar linha, e para quebrar \n.
n1 = int(input('digite um número'))
n2 = int(input('digite mais um'))
ns = n1 + n2
nm = n1 * n2
nd = n1 / n2
ndi = n1 // n2
nr = n1 % n2
np = n1 ** n2
print(f'a soma é {ns}, a multiplicação é {nm}, a divisão é {nd}, a divisão inteira é {ndi}, o resto é {nr}')
print(f'e a potência é {np}')
# pra deixar um valor com limite de casas após a virgula, usar dentro das chaves {:.3f} no lugar de 3 o número desejado.

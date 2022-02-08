# os operadores: + adição, - subtração, * multiplicação, /divisão, ** potência,
# //divisão inteira, % resto da divisão
# == para o resultado
# ordem de precedencia: 1° (); 2° **; 3° *, /, //, %; 4° +, -;
# quando quiser fazer uma raiz, use n**(1/2), porcentagem = (numero por cento) / 100.
# print('q' *5) cria 5 vezes,
# em formatação ":" delimita o número de caracteres "print(f'{:20}')" , > alinhado a direita "print(f'{:>20}')",
# < alinhado a esquerda "print(f'{:<20}')", ^ centralizado "print(f'{:^20}')",
# se colocar um simbolo antes do alinhamento, ele assumira os espaços brancos "print(f'{:=^20}')"
# colocar end='' no ptint para não quebrar linha, e para quebrar \n.
n1 = int(input('digite um número: '))
n2 = int(input('digite mais um: '))
ns = n1 + n2
nm = n1 * n2
nd = n1 / n2
ndi = n1 // n2
nr = n1 % n2
np = n1 ** n2
print(f'a soma é {ns}, a multiplicação é {nm}, a divisão é {nd}, a divisão inteira é {ndi}, o resto é {nr}')
print(f'e a potência é {np}')
# pra deixar um valor com limite de casas após a virgula, usar dentro das chaves {:.3f} no lugar de 3 o número desejado.

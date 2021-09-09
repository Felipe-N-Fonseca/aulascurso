# para o python use a "\" seguido do cofigo, o que melhor funciona é o 033
# após isso abra [ e dentro disso você pode mudar 3 caracteristicas, style, text e back.
# style é a fonte que pode ser 0 = nada, 1 = negrito, 4 = sublinhado e 7 = negativo
# text é a cor do texto, que vai de 30 até 37, sendo 30 = branco, 31 = vermelho, 32 = verde
# 33 = amarelo, 34 = azul, 35 = roxo, 36 = ciano e 37 = cinza
# o back é a cor de fundo e segue a mesma linha de cores de text porem de 40 até 47
# funciona assim: print('\033[0;31;44m olá mundo')
# pesquisar sobre a biblioteca colorize
# setar cores assim: cores = {'branco':'\033[0;30', 'azul':'\033[0;34'}

print('\033[1;30;41m eae rapaziada')

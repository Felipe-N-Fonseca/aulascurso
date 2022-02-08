# o python divide os textos em caracteres e vão de 0 até o fim do texto
# frase[?] mostra o caractere com aquele numero, frase[1:12] vai de 1 até 12 excluindo o 12
# se usar frase[1:12:2] ele vai de 1 a 11 pulando de 2 em 2 caracteres
# frase[:5] ele vai do inicio até o 4, e frase[15:] vai até o fim
# pode usar frase[12::4] pra ir até o fim pulando de 3 em 3
# len(frase) mostra a quantidade de caracteres
# frase.count('o') conta quantas vezes a letra o aparece na frase
# frase.count('o', 0, 13) ja conta com fatiamento, conta do 0 até a 12
# frase.find('mas') encontra "mas" dentro da frase e mostra sua posição
# quando usar a função de find e não encontrar o valor desejado, ele retorna -1
# 'mas' in frase, quando usa o in ele mostra True ou False
# frase.replace('mas','mais'), substitui mas por mais
# frase.upper() transforma as letras minusculas em maiusculas e o .lower() faz o inverso
# frase.capitalize() trasforma todas as letras exceto a primeira em minusculas
# frase.title() faz a função de capitalize porem palavra por palavra, indentificando os espaços
# frase.strip() remove os espaços inuteis no inicio e no fim das frases, adicionando l no começo (lstrip)
# ele remove apenas os espaços do começo, da mesma forma com os do fim adicione r (rstrip)
# frase.split() separa as palavras em novas, "eu sou eu" vira "eu" "sou" "eu", dividindo em 0, 1 e 2 respectivamente
# para alcançar um caractere dentro da palavra no split use [?] pra palavra e [?] pro caractere
# '-'.join(frase) junta os elementos de frase com "-" entre cada palavra
# para fazer prints grandes bota (""" antes e """) depois
frase = 'maconha'
print(frase[::2])
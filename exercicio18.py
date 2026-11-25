#exercicio 78
print('Exercicio 78 - Usando listas')
lista = []
maior = menor = 0
for posicao, i in enumerate(range(5)):
    lista.append(int(input(f'Digite um valor para a posição {posicao}: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitafo foi {min(lista)} na posição {lista.index(min(lista))}')


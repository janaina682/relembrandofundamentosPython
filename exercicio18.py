'''
#exercicio 78
print('Exercicio 78 - Usando listas')
lista = []
maior = menor = 0
for posicao, i in enumerate(range(5)):
    lista.append(int(input(f'Digite um valor para a posição {posicao}: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitafo foi {min(lista)} na posição {lista.index(min(lista))}')
print('-*-*' * 20)
'''
#exercicio 79
print('Exercicio 79 - Listas e valores unicos')
numeros = []
while True:
    numero = (int(input('Digite um valor: ')))
    if numero in numeros:
        print('Valor duplicado, não vou adicionar')
    else:
        numeros.append(numero)
        print('Valor adicionado com sucesso!')
    while True:
        continuar = input('Deseja continuar digitando valores? [S/N]').upper().strip()[0]
        if continuar in 'SN':
            break
        print('Opção inválida! Tente novamente')
    if continuar == 'N':
        break

print(f'Você digitou os valores: {numeros}')
numeros.sort()
print(f'Eles em ordem númerica ficam: {numeros}')
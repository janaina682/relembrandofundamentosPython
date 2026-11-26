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

'''
#exercicio 80
print('Exercicio 80 - Inserindo números na lista')
valores = []
for indice, i in enumerate(range(5)):
    while True:
        valor = int(input(f'Digite o {indice +1}° valor: '))
        if valor in valores:
            print(f'Esse valor {valor} já esta na lista, digite outro')
        else:
            break
    if indice == 0:
        print(f'Esse é o primeiro valor adicionado a lista! valor {valor}, posição 0')
        valores.append(valor)
    if indice == 1:
        if valor > valores[0]:
            valores.append(valor)
            print(f'O valor {valor}, foi adicionado na posição 1, posição final da lista')
        else:
            valores.insert(0, valor)
            print(f'O valor {valor}, foi adicionado na posição 0')
    if indice == 2:
        if valor > valores[0]:
            if valor > valores[1]:
                valores.append(valor)
                print(f'O valor {valor}, foi adicionado na posição 2, posição final da lista!')
            else:
                valores.insert(1, valor)
                print(f'O valor {valor}, foi adicionado na posição 1')
        else:
            valores.insert(0, valor)
            print(f'O valor {valor}, foi adicionado na posição 0')
    if indice == 3:
        if valor > valores[0]:
            if valor > valores[1]:
                if valor > valores[2]:
                    valores.append(valor)
                    print(f'O valor {valor}, foi adicionado na posição 3, posição final da lista!')
                else:
                    valores.insert(2, valor)
                    print(f'O valor {valor}, foi adicionado na posição 2')
            else:
                valores.insert(1, valor)
                print(f'O valor {valor}, foi adicionado na posição 1')
        else:
            valores.insert(0, valor)
            print(f'O valor {valor}, foi adicionado na posição 0')
    if indice == 4:
        if valor > valores[0]:
            if valor > valores[1]:
                if valor > valores[2]:
                    if valor > valores[3]:
                        valores.append(valor)
                        print('O valor {valor}, foi adicionado na posição 4, posição final da lista!')
                    else:
                        valores.insert(3, valor)
                        print(f'O valor {valor}, foi adicionado na posição 3')
                else:
                    valores.insert(2, valor)
                    print(f'O valor {valor}, foi adicionado na posição 2')
            else:
                valores.insert(1, valor)
                print(f'O valor {valor}, foi adicionado na posição 1')
        else:
            valores.insert(0, valor)
            print(f'O valor {valor}, foi adicionado na posição 0')
    if indice == 5:
        if valor > valores[0]:
            if valor > valores[1]:
                if valor > valores [2]:
                    if valor > valores[3]:
                        if valor > valores[4]:
                            valores.append(valor)
                            print(f'O valor {valor} foi adicionado na 5° posição, ultima posição da lista')
                        else:
                            valores.insert(4,valor)
                            print(f'O valor {valor}, foi adicionado na posição 4')
                    else:
                        valores.insert(3, valor)
                        print(f'O valor {valor}, foi adicionado na posição 3')
                else:
                    valores.insert(2, valor)
                    print(f'O valor {valor}, foi adicionado na posição 2')
            else:
                valores.insert(1, valor)
                print(f'O valor {valor}, foi adicionado na posição 1')
        else:
            valores.insert(0, valor)
            print(f'O valor {valor}, foi adicionado na posição 0')
print(f'A lista fina é: {valores}')
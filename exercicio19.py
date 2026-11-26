'''
#exercicio 81
print('Exercicio 81 - trabalhando com listas')
lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    while True:
        continuar = str(input('Quer continuar digitando valores? [S/N]')).strip().upper()[0]
        if continuar in 'NS':
            break
        print('Opção inválida!')
    if continuar == 'N':
        break
    
print(f'Você digitou os valores {lista}')
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Ordenados de forma decrescente fica: {lista}')
if 5 in lista:
    print(f'Existe o valor 5 nessa lista, na posição {lista.index(5)}')
else:
    print('Você digitou o valor 5')
'''
#exercicio 82
print('Exercicio 82 - destrinchando listas')
numeros =  []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    while True:
        continuar = str(input('Deseja continuar inserindo numeros a lista? [S/N]')).upper().strip()[0]
        if continuar in 'NS':
            break
        print('Opção inválida')
    if continuar == 'N':
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Os números digitados foram: {numeros}')
print(f'Os numeros pares digitados foram {pares}')
print(f'Os números impares digitados foram {impares}')
            
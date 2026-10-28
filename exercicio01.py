#exercicio 01
print('Exercício 01 - Olá Mundo!')
print('Olá Mundo!')
print('-' * 20)

#exercicio 02
print('Exercício 02 - Input de Dados')
nome = input('Qual é o seu nome? ')
print('Olá ' + nome + '! Prazer em te conhecer')
print('-' * 20)


#exercicio 03
print('Exercício 03 - Operações Aritméticas')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))
print('A subitração de {} e {} é {}'.format(n1, n2, n1-n2))
print('A multipricação de {} por {} é {}'.format(n1, n2, n1*n2))
print('A divisã de {} por {} é {}'.format(n1, n2, n1/n2))
print('{} elevado a {} é {}'.format(n1, n2, n1**n2))
print('-' * 20)


#exercicio 04
print('Exercício 04 - Tipos Primitivos e Saída de Dados')
teste = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(teste))
print('Só tem espaços? ', teste.isspace())
print('É um numero? ', teste.isnumeric())
print('É alfabético? ', teste.isalpha())
print('É alfanumérico? ', teste.isalnum())
print('Está em maiúsculo? ', teste.isupper())
print('Está em minúsculo? ', teste.islower())
print('Está capitalizada? ', teste.istitle())
print('-' * 20)

#exercicio 05
print('Exercício 05 - Antecessor e Sucessor')
numero = int(input('Digite um número: '))
print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}'.format(numero, (numero-1), numero+1))
print('-' * 20)

#exercicio 06
print('Exercício 06 - Dobro, Triplo e Raiz Quadrada')
print('Você digitou o número {}'.format(numero))
print('O dobro é {}, o triplo é {} e a raiz quadrada é {}'.format(numero*2, numero*3, numero**(1/2)))
print('-' * 20)

#exercicio 07
print('Exercício 07 - Média Aritmética')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('A média do aluno é {:.1f}'.format((nota1+nota2)/2))
print('-' * 20)

#exercicio 08
print('Exercício 08 - Conversão de Medidas')
valor = float(input('Digite um valor em metros: '))
deca = valor / 10
hec = valor / 100
km = valor / 1000
deci = valor * 10
centi = valor * 100
mili = valor * 1000
print('O valor é {}m,\n Em decâmetros é {}dam,\n em hectômetros é {}hm,\n em quilometros é {}km\n'.format(valor, deca, hec, km))
print('Em decímetros é {}dm,\n em centímetros é {}cm,\n em milímetros é {}mm'.format(deci, centi, mili))
print('-' * 20)

#exercicio 09
print('Exercício 09 - Tabuada')
numero_int = int(input('Digite um número inteiro: '))
print('Sua tabuada é: ')
print(numero_int, 'x', 1, '=', numero_int*1)
print(numero_int, 'x', 2, '=', numero_int*2)
print(numero_int, 'x', 3, '=', numero_int*3)
print(numero_int, 'x', 4, '=', numero_int*4)
print(numero_int, 'x', 5, '=', numero_int*5)
print(numero_int, 'x', 6, '=', numero_int*6)
print(numero_int, 'x', 7, '=', numero_int*7)
print(numero_int, 'x', 8, '=', numero_int*8)
print(numero_int, 'x', 9, '=', numero_int*9)
print(numero_int, 'x', 10, '=', numero_int*10)
print('-' * 20)

#exercicio 10
print('Exercício 10 - Conversão de Moedas')
dinheiro = float(input('Digite um valor em reais: R$ '))
dolar = dinheiro / 3.27
print('Com esse valor você pode comprar {:.2f} dólares'.format(dolar))
print('-' * 20)
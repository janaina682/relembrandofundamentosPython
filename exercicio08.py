from datetime import date
#exercicio 36
print('Exercicio 36 - Empréstimo bancário')
valor_casa = int(input('Digite o valor da casa: R$'))
salario = int(input('Digite seu salário mensal: R$'))
prazo = int(input('Em quantos anos você pretende pagar esse empréstimo? '))

prestacao_mensal = valor_casa / (prazo * 12)
limite_mensal = salario * 0.3

if prestacao_mensal > limite_mensal:
    print('A prestação excede o limite de 30% do seu sálario')
else:
    print(f'Empréstimo aprovado, valor da prestação: {prestacao_mensal:.2f}')
print('+-*' * 20)

#exercicio 37
print('Exercicio 37 - Base de conversão')
numero = int(input('Que número você quer converter? '))
print('Escolha uma das bases de converção: \n Digite [1] para converter para binário\n Digite [2] para converter para octal\n Digite [3] para converter para hexadecimal ')
base = int(input('Quer converter para qual base? '))

if base == 1:
    print(f'{numero} convertido para BINÁRIO é igual a: ')
    print(bin(numero)[2:])
elif base == 2:
    print(f'{numero} convertido para OCTAL é igual a: ')
    print(oct(numero)[2:])
elif base == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a: ')
    print(hex(numero)[2:])
else:
    print('Você escolheu uma base que não existe no programa')
print('+-*' * 20)

#exercicio 38
print('Exercicio 38 - comparação de numeros inteiros')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um outro número inteiro: '))

if n1 > n2:
    print(f'O primeiro valor {n1} é maior que o segundo {n2}')
elif n1 < n2:
    print(f'O segundo valor {n2} é maior que o primeiro {n1}')
else:
    print(f'Não existe valor maior, os dois são iguais a {n1}')
print('+-*' * 20)

#exercicio 39
print('Exercício 39 - Hora de se alistar')
ano_atual = date.today().year
ano_nascimento = int(input('Qual o seu ano de nascimento? '))
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
    print(f'Ainda não é tempo de se alistar, faltam {18 - idade} anos')
elif idade == 18:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
    print('Hora de se alistar no exercito IMEDIATAMENTE')
else:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
    print(f'Você tinha que ter se alistado há {idade - 18} anos')
print('+-*' * 20)

#exercicio 40
print('Exercicio 40 - Calculando a média')
nota1 = float(input('Digite a nota no primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimeste: '))
nota3 = float(input('Digite a nota do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'1 °Bimestre: {nota1}\n2° Bimestre: {nota2}\n3° Bimestre: {nota3}\n4° Bimestre: {nota4}')
if media < 5:
    print(f'Sua média final foi {media}, você está REPROVADO')
elif media >=5 and media < 7:
    print(f'Sua média final foi {media}, você está de RECUPERAÇÃO')
else:
    print(f'Sua média final foi {media}, você está APROVADO')
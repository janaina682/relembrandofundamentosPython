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
    print('Empréstimo aprovado, valor da prestação: {:.2f}'.format(prestacao_mensal))
print('+-*' * 20)

#exercicio 37
print('Exercicio 37 - Base de conversão')
numero = int(input('Que número você quer converter? '))
print('Escolha uma das bases de converção: \n Digite [1] para converter para binário\n Digite [2] para converter para octal\n Digite [3] para converter para hexadecimal ')
base = int(input('Quer converter para qual base? '))

if base == 1:
    print('{} convertido para BINÁRIO é igual a: '.format(numero))
    print(bin(numero)[2:])
elif base == 2:
    print('{} convertido para OCTAL é igual a: '.format(numero))
    print(oct(numero)[2:])
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a: '.format(numero))
    print(hex(numero)[2:])
else:
    print('Você escolheu uma base que não existe no programa')
print('+-*' * 20)

#exercicio 38
print('Exercicio 38 - comparação de numeros inteiros')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um outro número inteiro: '))

if n1 > n2:
    print('O primeiro valor {} é maior que o segundo {}'.format(n1,n2))
elif n1 < n2:
    print('O segundo valor {} é maior que o primeiro {}'.format(n2,n1))
else:
    print('Não existe valor maior, os dois são iguais a {}'.format(n1))
print('+-*' * 20)

#exercicio 39
print('Exercício 39 - Hora de se alistar')
ano_atual = date.today().year
ano_nascimento = int(input('Qual o seu ano de nascimento? '))
idade = ano_atual - ano_nascimento

if idade < 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, idade, ano_atual))
    print('Ainda não é tempo de se alistar, faltam {} anos'.format(18 - idade))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, idade, ano_atual))
    print('Hora de se alistar no exercito IMEDIATAMENTE')
else:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, idade, ano_atual))
    print('Você tinha que ter se alistado há {} anos'.format(idade - 18))
print('+-*' * 20)

#exercicio 40
print('Exercicio 40 - Calculando a média')
nota1 = float(input('Digite a nota no primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimeste: '))
nota3 = float(input('Digite a nota do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('1 °Bimestre: {}\n2° Bimestre: {}\n3° Bimestre: {}\n4° Bimestre: {}'.format(nota1, nota2, nota3, nota4))
if media < 5:
    print('Sua média final foi {}, você está REPROVADO'.format(media))
elif media >=5 and media < 7:
    print('Sua média final foi {}, você está de RECUPERAÇÃO'.format(media))
else:
    print('Sua média final foi {}, você está APROVADO'.format(media))
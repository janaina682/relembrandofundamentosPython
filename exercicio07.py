from datetime import date
#exercicio 32
print('Exercício 32 - Identificador de ano bissexto')
ano = int(input('Que ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0:
    print('O ano {} É BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
    
#exercicio 33
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
print('-+' * 20)

#exercicio 34
print('Exercício 34 - Aumento múltiplos')
salario = float(input('Digite o salário do funcionário em reais: '))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print('O salário com aumento é de R${:.2f}'.format(salario + aumento))
print('-+' * 20)

#exercicio 35
print('Exercício 35 - Analisando Triângulo')
comp1 = float(input('Digite o comprimento do primeiro lado do triângulo: '))
comp2 = float(input('Digite o comprimento do segundo lado do triângulo: '))
comp3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))
if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('Os lados formam um triângulo!')
else:
    print('Os lados não formam um triângulo!')
from datetime import date
#exercicio 11
print('Exercício 11 - Pintura de Parede')
altura = int(input('Digite a altura da parede em metros: '))
largura = int(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2
print(f'A area da parede é {area} m² e você precisara de {tinta} litros de tinta para pintá-la')
print('-' * 20)

#exercicio 12
print('Exercício 12 - Preço do Produto com Desconto')
preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05
print(f'O preço do produto com desconto de 5% é {preco - desconto}')
print('-' * 20)

#exercicio 13
print('Exercício 13 - Salário com Aumento')
salario = float(input('Digite o salário do funcionário: '))
aumento = salario * 0.15
print(f'O salário com 15% de aumento é {salario + aumento}')
print('-' * 20)

#exercicio 14
print('Exercício 14 - Conversor de Temperatura')
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura em Fahrenheit é {fahrenheit}')
print('-' * 20)

#exercicio 15
print('Exercício 15 - Aluguel de Carro')
km_rodados = float(input('Digite quantos km foram percorridos: '))
dias = int(input('Digite quantos dias o carro foi alugado: '))
preco_total = (km_rodados * 0.15) + (dias * 60)
print(f'O preço total a pagar é R$ {preco_total:.2f}')
print('-' * 20)

#exercicio Bonus
print('Exercício Bonus - Idade do Usuário')
dia = input('Dia = ')
mes = input('Mes = ')
ano = int(input('Ano = '))
ano_atual = date.today().year
idade = ano_atual - ano
print('Você nasceu dia ', dia, ' de ', mes, ' de ', ano, '.Correto?')
print('Então você tem ', idade, ' anos')

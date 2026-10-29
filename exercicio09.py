from datetime import date
import random
#exercicio 41
print('Exercicio 41 - Categoria dos atletas por idade')
ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('O atleta tem {} anos, e está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, e está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos, e está na categoria JUNIOR'.format(idade))
elif idade <= 25: 
    print('O atleta tem {} anos, e está na categoria SENIOR'.format(idade))
else:
    print('O atleta tem {} anos, e está na categoria MASTER'.format(idade))
print('-+*' *20)

#exercicio 42
print('Exercicio 42 - Tipos de triângulos')
print('Exercício 35 - Analisando Triângulo')
comp1 = float(input('Digite o comprimento do primeiro lado do triângulo: '))
comp2 = float(input('Digite o comprimento do segundo lado do triângulo: '))
comp3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))
if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('Os lados formam um triângulo!')
    if comp1 == comp2 == comp3:
        print('Esse é um triangulo Equilátero')
    elif comp1 != comp3 != comp2:
        print('Esse é um triângulo Escaleno')
    else:
        print('Esse é um triângulo Isósceles')
else:
    print('Os lados não formam um triângulo!')
print('-+*' *20)

#exercicio 43
print('Exercício 43 - IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é: {:.2f}, você está abaixo do peso ideal para sua altura'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é: {:.2f}, você está na faixa de peso ideal para sua altura'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é: {:.2f}, você está com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é: {:.2f}, você está com OBESIDADE, isto é acima do peso ideal para sua altura'.format(imc))
else:
    print('Seu IMC é: {:.2f}, você está com OBESIDADE MORBIDA, isto é MUITO acima do peso ideal para sua altura'.format(imc))
print('-+*' *20)

#exercicio 44
print('Exercicio 44 - Preço do produto')
preco = float(input('Digite o preço do produto: '))
condicao = int(input('Digite o número da forma de pagamento: \n Digite 1 para pagamento à vista (dinheiro ou cheque)\n Digite 2 para pagamento à vista no cartão\n Digite 3 para pagar em até 2x no cartão\n Digite 4 para pagar em 3 ou mais vezes no cartão\n'))

if condicao == 1:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print('Pagamento à vista no dinheiro ou cheque tem 10% de desconto')
    print('O produto de R${:.2f}, ganhou R${:.2f} de desconto e ficou por apenas R${:.2f}'.format(preco, desconto, preco_final))
elif condicao == 2:
    desconto = preco * 0.05
    preco_final = preco - desconto
    print('Pagamento à vista no cartão tem 5% de desconto')
    print('O produto de R${:.2f}, ganhou R${:.2f} de desconto e ficou por apenas R${:.2f}'.format(preco, desconto, preco_final))
elif condicao == 3:
    print('Pagamento em até 2x no cartão NÃO TEM ACRESCIMO')
    print('O produto ficou por apenas R${:.2f}'.format(preco))
elif condicao == 4:
    juros = preco * 0.20
    preco_final = preco + juros
    print('Pagamento no cartão parcelado em mais de 3x tem acrescimo de 20% de juros ')
    print('O produto de R${:.2f}, parcelado em 3 ou mais vezes tem R${:.2f} de juros e ficou por apenas R${:.2f}'.format(preco, juros, preco_final))
else:
    print('O numero digitado não corresponde a nenhuma opção de pagamento')
print('-+*' *20)

#exercicio 43
print('Exercicio 43 - Jokenpô')
resposta = input('Vamos brincar de Jokenpô? É sua vez digite sua opção: \n "PEDRA" "PAPEL" ou "TESOURA" : ').upper()
computador = random.randint(1,3)
opcao = ''
if computador == 1:
    opcao = 'PEDRA'
if computador == 2:
    opcao = 'PAPEL'
if computador == 3:
    opcao = 'TESOURA'
if opcao == resposta:
    print('Deu empate nós escolhemos {}'.format(opcao))
elif computador == 1 and resposta == 'PAPEL' or computador == 2 and resposta == 'TESOURA' or computador == 3 and resposta == 'PEDRA':
    print('Você ganhou, escolheu {} e eu tinha escolhido {}'.format(resposta, opcao))
else:
    print('Eu ganhei, eu escolhi {} e você escolheu {}'.format(opcao, resposta))
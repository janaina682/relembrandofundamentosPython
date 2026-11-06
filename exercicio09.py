from datetime import date
import random
#exercicio 41
print('Exercicio 41 - Categoria dos atletas por idade')
ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos, e está na categoria MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos, e está na categoria INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos, e está na categoria JUNIOR')
elif idade <= 25: 
    print(f'O atleta tem {idade} anos, e está na categoria SENIOR')
else:
    print(f'O atleta tem {idade} anos, e está na categoria MASTER')
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
    elif comp1 != comp2 != comp3 != comp1:
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
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é: {imc:.1f}, você está abaixo do peso ideal para sua altura')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é: {imc:.1f}, você está na faixa de peso ideal para sua altura')
elif 25 <= imc < 30:
    print(f'Seu IMC é: {imc:.1f}, você está com sobrepeso')
elif 30 <= imc < 40:
    print(f'Seu IMC é: {imc:.1f}, você está com OBESIDADE, isto é acima do peso ideal para sua altura')
else:
    print(f'Seu IMC é: {imc:.1f}, você está com OBESIDADE MORBIDA, isto é MUITO acima do peso ideal para sua altura')
print('-+*' *20)

#exercicio 44
print('Exercicio 44 - Preço da compra')
print('{:=^40}'.format(' JANAINA STORE '))
preco = float(input('Digite o valor total da compra: '))
condicao = int(input('''Digite o número da forma de pagamento:
Digite [1] para pagamento à vista (dinheiro ou cheque)
Digite [2] para pagamento à vista no cartão
Digite [3] para pagar em até 2x no cartão
Digite [4] para pagar em 3 ou mais vezes no cartão\n'''))

if condicao == 1:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print('Pagamento à vista no dinheiro ou cheque tem 10% de desconto')
    print(f'A compra de R${preco:.2f}, ganhou R${desconto:.2f} de desconto e ficou por apenas R${preco_final:.2f}')
elif condicao == 2:
    desconto = preco * 0.05
    preco_final = preco - desconto
    print('Pagamento à vista no cartão tem 5% de desconto')
    print(f'A compra de R${preco:.2f}, ganhou R${desconto:.2f} de desconto e ficou por apenas R${preco_final:.2f}')
elif condicao == 3:
    parcela = preco / 2
    print('Pagamento em até 2x no cartão NÃO TEM ACRESCIMO')
    print(f'A compra ficou por apenas R${preco:.2f} 2x de R${parcela:.2f}')
elif condicao == 4:
    juros = preco * 0.20
    preco_final = preco + juros
    print('Pagamento no cartão parcelado 3 ou mais vezes tem acrescimo de 20% de juros ')
    total_parcela = int(input('Você quer parcelar em quantas vezes? '))
    parcela = preco_final / total_parcela
    print(f'Sua compra de R${preco:.2f}, foi parcelado no cartão em {total_parcela}x de R${parcela:.2f}')
else:
    print('O numero digitado não corresponde a nenhuma opção de pagamento')
print('-+*' *20)

#exercicio 45
print('Exercicio 45 - Jokenpô')
resposta_jogador = input('Vamos brincar de Jokenpô? É sua vez digite sua opção: \n "PEDRA" "PAPEL" ou "TESOURA" : ').upper()
computador = random.randint(1,3)
if computador == 1:
    resposta_computador = 'PEDRA'
if computador == 2:
    resposta_computador = 'PAPEL'
if computador == 3:
    resposta_computador = 'TESOURA'
print('=='*20)
print(f'''Computador jogou {resposta_computador}
Jogador jogou {resposta_jogador}''')
print('=='*20)
if resposta_computador == resposta_jogador:
    print(f'Deu empate nós escolhemos {resposta_computador}')
elif computador == 1 and resposta_jogador == 'PAPEL' or computador == 2 and resposta_jogador == 'TESOURA' or computador == 3 and resposta_jogador == 'PEDRA':
    print(f'Você ganhou, escolheu {resposta_jogador} e eu tinha escolhido {resposta_computador}')
else:
    print(f'Eu ganhei, eu escolhi {resposta_computador} e você escolheu {resposta_jogador}')
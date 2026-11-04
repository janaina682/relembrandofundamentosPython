#exercicio 57
print('Exercicio 57 - Validação de sexo')
sexo = str(input('Digite o sexo da pessoa: [M] para masculino e [F] para feminino: ')).upper()

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor digite o sexo da pessoa: [M] ou [F]: ')).upper()
    
if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')
print('*-*-' * 20)

#exercicio 58
print('Exercicio 58 - Jogo de adivinhação')
import random
numero_aleatorio = random.randint(0,10)
tentativas = 0
palpite = int(input('Tente adivinhar o número que estou pensando entre 0 e 10: '))
while palpite != numero_aleatorio:
    tentativas += 1
    print('Você errou! Tente novamente.')
    palpite = int(input('Digite outro número entre 0 e 10: '))
print('Parabéns! Você acertou! O número era {}. Você precisou de {} tentativas para acertar'.format(numero_aleatorio, tentativas + 1))
print('*-*-' * 20)

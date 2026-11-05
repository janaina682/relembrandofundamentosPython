#exercicio 57
print('Exercicio 57 - Validação de sexo')
sexo = str(input('Digite o sexo da pessoa: [M] para masculino e [F] para feminino: ')).upper().strip()

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor digite o sexo da pessoa: [M] ou [F]: ')).upper().strip()
    
if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')
print('*-*-' * 20)

#exercicio 58
print('Exercicio 58 - Jogo de adivinhação')
from random import randint
numero_aleatorio = randint(0,10)
print('Estou pensando em um número entre 0 e 10. Tente adivinhar!')
tentativas = 0
palpite = int(input('Tente adivinhar o número que estou pensando entre 0 e 10: '))
while palpite != numero_aleatorio:
    tentativas += 1
    if palpite < numero_aleatorio:
        print('Você errou! O número que estou pensando é maior que {}. Tente novamente.'.format(palpite))
    elif palpite > numero_aleatorio:
        print('Você errou! O número que estou pensando é menor que {}. Tente novamente.'.format(palpite))
    palpite = int(input('Digite outro número entre 0 e 10: '))
print('Parabéns! Você acertou! O número era {}. Você precisou de {} tentativas para acertar'.format(numero_aleatorio, tentativas + 1))
print('*-*-' * 20)

#exercicio 59
from time import sleep
print('Exercicio 59 - Calculadora')
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
escolha_menu = 0
while escolha_menu !=5:
    escolha_menu = int(input('''Escolha a operação que deseja realizar:
[1] - Soma
[2] - Multiplicar
[3] - maior
[4] - Novos números
[5] - Sair do programa '''))
    if escolha_menu == 1:
        print('A soma entre {} + {} é igual a {}'.format(primeiro_numero, segundo_numero, primeiro_numero + segundo_numero))
    elif escolha_menu == 2:
        print('O resultado de {} x {} é igual a {}'.format(primeiro_numero, segundo_numero, primeiro_numero * segundo_numero))
    elif escolha_menu == 3:
        if primeiro_numero > segundo_numero:
            print('O primeiro número [{}] é maior que o segundo número [{}]'.format(primeiro_numero, segundo_numero))
        elif primeiro_numero < segundo_numero:
            print('O segundo número [{}] é maior que o primeiro número [{}]'.format(segundo_numero, primeiro_numero))
        else:
            print('Os dois números são iguais! [{}]'.format(primeiro_numero))
    elif escolha_menu == 4:
        print('Digite os números novamente')
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))
    elif escolha_menu == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida! Tente novamente.')
    sleep(2)
print('*-*-' * 20)

#exercicio 60
print('Exercicio 60 - Fatorial')
numero = int(input('Digite um número para calcular o fatorial: '))
print('{}! = '.format(numero), end = '')
total = 1
while numero > 1:
    print('{} x '.format(numero), end= '')
    total *= numero
    numero -= 1
print('1 - O fatorial do número digitado é: {}'.format(total))
    
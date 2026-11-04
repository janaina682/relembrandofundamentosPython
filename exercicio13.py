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

#exercicio 59
print('Exercicio 59 - Calculadora')
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
escolha_menu = int(input('''Escolha a operação que deseja realizar:
[1] - Soma
[2] - Multiplicar
[3] - maior
[4] - Novos números
[5] - Sair do programa '''))
while escolha_menu !=5:
    if escolha_menu == 1:
        print('A soma entre {} e {} é igual a {}'.format(primeiro_numero, segundo_numero, primeiro_numero + segundo_numero))
        escolha_menu = int(input('''Escolha a operação que deseja realizar:
        [1] - Soma
        [2] - Multiplicar
        [3] - maior
        [4] - Novos números
        [5] - Sair do programa '''))
    elif escolha_menu == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(primeiro_numero, segundo_numero, primeiro_numero * segundo_numero))
        escolha_menu = int(input('''Escolha a operação que deseja realizar:
        [1] - Soma
        [2] - Multiplicar
        [3] - maior
        [4] - Novos números
        [5] - Sair do programa '''))
    elif escolha_menu == 3:
        if primeiro_numero > segundo_numero:
            print('O primeiro número [{}] é maior que o segundo número [{}]'.format(primeiro_numero, segundo_numero))
        elif primeiro_numero < segundo_numero:
            print('O segundo número [{}] é maior que o primeiro número [{}]'.format(segundo_numero, primeiro_numero))
        else:
            print('Os dois números são iguais! [{}]'.format(primeiro_numero))
        escolha_menu = int(input('''Escolha a operação que deseja realizar:
        [1] - Soma
        [2] - Multiplicar
        [3] - maior
        [4] - Novos números
        [5] - Sair do programa '''))
    elif escolha_menu == 4:
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))
        escolha_menu = int(input('''Escolha a operação que deseja realizar:
        [1] - Soma
        [2] - Multiplicar
        [3] - maior
        [4] - Novos números
        [5] - Sair do programa '''))
    else:
        print('Opção inválida! Tente novamente.')
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
    
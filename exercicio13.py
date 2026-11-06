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
        print(f'Você errou! O número que estou pensando é maior que {palpite}. Tente novamente.')
    elif palpite > numero_aleatorio:
        print(f'Você errou! O número que estou pensando é menor que {palpite}. Tente novamente.')
    palpite = int(input('Digite outro número entre 0 e 10: '))
print(f'Parabéns! Você acertou! O número era {numero_aleatorio}. Você precisou de {tentativas + 1} tentativas para acertar')
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
        print(f'A soma entre {primeiro_numero} + {segundo_numero} é igual a {primeiro_numero + segundo_numero}')
    elif escolha_menu == 2:
        print(f'O resultado de {primeiro_numero} x {segundo_numero} é igual a {primeiro_numero * segundo_numero}')
    elif escolha_menu == 3:
        if primeiro_numero > segundo_numero:
            print(f'O primeiro número [{primeiro_numero}] é maior que o segundo número [{segundo_numero}]')
        elif primeiro_numero < segundo_numero:
            print(f'O segundo número [{segundo_numero}] é maior que o primeiro número [{primeiro_numero}]')
        else:
            print(f'Os dois números são iguais! [{primeiro_numero}]')
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
print(f'{numero}! = ', end = '')
total = 1
while numero > 1:
    print(f'{numero} x ', end= '')
    total *= numero
    numero -= 1
print(f'1 - O fatorial do número digitado é: {total}')
    
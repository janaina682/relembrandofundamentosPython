#exercicio 61
print('Exercício 61 - Progressão Aritmética')
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + 9 * razao
while primeiro_termo <= decimo_termo:
    print('{} ->'.format(primeiro_termo), end= ' ')
    primeiro_termo += razao
print('\n' + '*-*-' * 20)

#exercicio 62
print('Exercício 62 - Progressão Aritmética v2.0')
termo = int(input('Digite o primeiro termo da PA: '))
razao =int(input('Digite a razão da PA: '))
ultimo_termo = termo + 9 * razao
qtde_termos = 10
while termo <= ultimo_termo:
    print('{} ->'.format(termo), end= ' ')
    termo += razao
mais_termos = int(input('\nQuantos termos você quer mostrar a mais? '))
qtde_termos += mais_termos
while mais_termos !=0:
    ultimo_termo += mais_termos * razao
    while termo <= ultimo_termo:
        print('{} ->'.format(termo), end = '')
        termo += razao
    mais_termos = int(input('\nQuantos termos você quer mostrar a mais? digite [0] para sair: '))
print('Foram mostrados {} termos'.format(qtde_termos))
print('\n' + '*-*-' * 20) 

#exercicio 63
print('Exercicio 63 - Sequência de Fibonacci')
numero = 0
qtde_termos = int(input('Digite a quantidade de termos que deseja mostrar: '))
prox_termo = 1
resultado = 0
total_termos = 0
while total_termos < qtde_termos:
    print('{} ->'.format(numero), end= ' ')
    resultado = numero + prox_termo
    numero = prox_termo
    prox_termo = resultado
    total_termos += 1
print('\n' + '*-*-' * 20)

#exercicio 64
print('Exercicio 64 - lendo números')
soma = 0
qtde_numeros = 0
numero = int(input('Digite um número inteiro ou [999] para sair: '))
while numero != 999:
    soma += numero
    qtde_numeros += 1
    numero = int(input('Digite um número inteiro ou [999] para sair: '))
print('A soma dos {} numeros digitados é: {}'.format(qtde_numeros, soma))

#exercicio 65
print('Exercicio 65 - Média, maior e menor')
soma = 0
qtde_numeros = 0
maior = menor = 0
validacao = True
while validacao == True:
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    qtde_numeros += 1
    if numero > maior:
        maior = numero
    else:
        menor = numero
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        validacao = False
    elif continuar not in 'SN':
        print('Opção inválida, tente novamente!')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    else:
        validacao = True
media = soma / qtde_numeros
print(f'Foram digitados {qtde_numeros} números, a média entre eles é: {media:.2f}')
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')

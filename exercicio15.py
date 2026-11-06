'''#exercicio 66
print('Exercicio 66 - Soma dos números digitados')
soma = qtde_numeros = 0
while True:
    numero = int(input('Digite um valor inteiro ou [999] para parar: '))
    if numero == 999:
        break
    soma +=numero
    qtde_numeros += 1
print(f'A soma dos {qtde_numeros} valores digitados é: {soma}!') 
print('*-*-' * 20)

#exercicio 67
print('Exercicio 67 - Tabuada')
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    else:
        print(f'A tabuada de {numero} é:')
        for n in range(1, 11):
            print(f'{numero} x {n} = {numero * n}')
print('Programa encerrado! Volte sempre!')
print('*-*-' * 20)

#exercicio 68
print('Exercicio 68 - Jogo do Par ou Impar')
print('*' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('*' * 20)
opçao_jogador = opcao_computador = ''
valor_jogador = valor_computador = 0
vitorias = 0
from random import randint
while True:
    opcao_jogador = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()[0]
    if opcao_jogador == 'P':
        opcao_computador = 'I'
        print('Você escolheu PAR então eu fico com IMPAR!')
    elif opcao_jogador == 'I':
        opcao_computador = 'P'
        print('Você escolheu IMPAR então eu fico com PAR!')
    else:
        print('Opção inválida! Tente novamente.')
    valor_jogador = int(input('Digite seu valor: '))
    valor_computador = randint(0, 10)
    print(f'Eu escolhi o valor {valor_computador}')
    soma = valor_jogador + valor_computador
    if soma % 2 == 0:
        print(f'A soma dos valores é {soma} que é PAR')
        if opcao_jogador == 'P':
            print('Você venceu!')
            vitorias += 1
        else:
            print('Eu venci!')
            break
    else:
        print(f'A soma dos valores é {soma} que é IMPAR')
        if opcao_jogador == 'I':
            print('Você venceu!')
            vitorias += 1
        else:
            print('Eu venci!')
            break
print('GAME OVER! Você venceu {} vezes'.format(vitorias)) 
        
'''
#exercicio 69
print('Exercicio 69 - Estatísticas de idade e sexo')
pessoas_mais18 = homens = mulheres_menos20 = 0
sexo = ''
while True:
    print('--' * 21)
    print('-'*10 + ' CADASTRE UMA PESSOA ' + '-'*10)
    print('--' * 21)
    idade = int(input('Digite a idade da pessoa: '))
    while True:
        sexo = str(input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0])
        if sexo in 'MF':
            break
        print('Opção inválida! Digite apenas [M] para masculino ou [F] para feminino.')
    if idade >= 18:
        pessoas_mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1
    while True:
        continuar = str(input('Deseja continuar cadastrando pessoas? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Opção inválida! Digite apenas [S] para sim ou [N] para não.')
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {pessoas_mais18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menos20}')
    
 
    
    


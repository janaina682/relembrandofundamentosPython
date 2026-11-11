'''
#exercicio 66
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
'''
#exercicio 68
print('Exercicio 68 - Jogo do Par ou Impar')
from random import randint
from time import sleep
print('*' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('*' * 20)
vitoria = 0

while True:
    opcao_jogador = ' '
    valor_pc = randint(0, 10)
    valor_jogador = int(input('Digite um número enquanto penso no meu... '))
    sleep(1)
    print('Ok, já pensei no meu...')
    total = valor_jogador + valor_pc
    while opcao_jogador not in 'PI':
        opcao_jogador = input('Você prefere PAR [P] OU IMPAR [I]? ').strip().upper()
    if opcao_jogador == 'P':
        print('Já que escolheu PAR então eu fico com ÍMPAR')
        sleep(1)
        print(f'Você jogou o número {valor_jogador} e eu o número {valor_pc} dando um total de {total}')
        if total % 2 == 0:
            print('Que é PAR!!! PARABÉNS, VOCÊ GANHOU!!!')
            sleep(1)
            print('Vamos jogar mais uma vez')
            vitoria += 1
        else:
            print('Que é ÍMPAR!!! você perdeu, mas sorte na proxima')
            print(f'Quantidade de vitorias nessa partida: {vitoria}')
            break
    if opcao_jogador == 'I':
        print('Já que você escolheu IMPAR então eu fico com PAR')
        print(f'Você jogou o número {valor_jogador} e eu o número {valor_pc} dando um total de {total}')
        if total % 2 == 0:
            print('Que é PAR!!! você perdeu, mas sorte na proxima')
            print(f'Quantidade de vitorias nessa partida: {vitoria}')
            break
        else:
            print('Que é ÍMPAR!!! PARABÉNS, VOCÊ GANHOU!!!')
            sleep(1)
            print('Vamos jogar mais uma vez')
            vitoria += 1
                
    
  
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
    

 #exercicio 70
print('Exercicio 70 - Estatísticas de produtos')
total = mais_q1000 = 0
produto_mais_barato = ''
menor_preco = 0
print('--' *30)
print('-'*5 + 'LOJA JANA STORE ' +'-' *5)
print('--' *30)
while True:
    print('CADASTRO DE PRODUTO')
    nome = str(input('Nome: '))
    preço = float(input('Preço: '))
    total += preço
    if preço > 1000:
        mais_q1000 += 1
    if preço < menor_preco:
        menor_preco = preço

 '''
    
    
        
        
    

    


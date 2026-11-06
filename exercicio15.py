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


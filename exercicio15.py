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


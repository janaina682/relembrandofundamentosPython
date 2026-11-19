#exercicio 72
print('Exercicio 72 - aprendendo Tuplas')
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num < 0 or num >20:
        print('O número tem que estar entre 0 e 20. Tente novamente')
    else:
        break
print(f'Você digitou o número {numeros[num]}')
print('*-' * 20)


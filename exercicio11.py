#exercicio 51
print('Exercício 51 - Progressão Aritimetica')
termo1 = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A: '))

for n in range(termo1, 10, razao):
    print(n)

print('*-*-' * 20)
#exercicio 52
print('Exercicio 52 - Saber se o número é primo')
numero = int(input('Digite um número para saber se ele é primo '))

if numero <= 1:
    primo = False
elif numero == 2:
    primo = True
elif numero % 2 == 0:
    primo = False
else:
    for n in range(3, numero, 2):
        if numero % n == 0:
            primo = False
            break
        else:
            primo = True
if primo == True:
    print('O número {} é primo'.format(numero))
else:
    print('O número {} não é primo'.format(numero))

print('*-*-' * 20)

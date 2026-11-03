from datetime import date
#exercicio 51
print('Exercício 51 - Progressão Aritimetica')
termo1 = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A: '))
decimo = termo1 + (10 - 1) * razao
for n in range(termo1, decimo + razao, razao):
    print('{}'.format(n), end=' -> ')
print('\n')
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

#exercicio 52 - Correção (feito de outra forma)
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('É por isso que ele é PRIMO!')
else:
    print('É por isso que ele NÃO É PRIMO!')
    
#exercicio 53
print('Exercicio 53 - Verificar se a frase é um palíndromo')
frase = str(input('Escreva uma frase: '))
frase_formatada = frase.upper().replace(' ', '')
frase_contrario = frase_formatada[::-1]
print('A frase: {} escrita ao contrário é: {}'.format(frase_formatada, frase_contrario))

if frase_formatada == frase_contrario:
    print('Por isso é um palíndromo')
else:
    print('Por isso não é um palíndromo')
print('*-*-' * 20)

#exercicio 54
print('Execício 54 - Saber quantas pessoas atingiram a maioridade')
ano_atual = date.today().year
ano = []
total = 0
for n in range(0,7):
    ano.append(int(input('Digite o ano de nascimeto do {}° participante '.format(n+1))))
for a in ano:
    if (ano_atual - a) < 18:
        total += 1
print('Esses são os anos de nascimento dos participantes: {}'.format(ano))
print('{} não atingiram a maioridade ainda'.format(total))
print('{} são maiores de idade'.format(len(ano) - total))
print('*-*-' * 20)

#exercicio 55
print('Exercício 55 - Maior e menor peso')
pesos = []
for i in range(5):
    pesos.append(float(input('Digite o peso do {}° participante: '.format(i+1))))
maior = pesos[0]
menor = pesos[0]
for peso in pesos:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso entre os participante é: {}kg'.format(maior))
print('O menor peso entre os participante é: {}kg'.format(menor))

#exercicio 61
print('Exercício 61 - Progressão Aritmética')
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + 9 * razao
while primeiro_termo <= decimo_termo:
    print('{} ->'.format(primeiro_termo), end= ' ')
    primeiro_termo += razao
print('\n' + '*-*-' * 20)


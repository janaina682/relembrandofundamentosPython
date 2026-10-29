#exercicio 51
print('Exercício 51 - Progressão Aritimetica')
termo1 = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A: '))

for i in range(10):
    termo = termo1 + i * razao
    print('{}° termo : {}'.format(i+1, termo))
print('*-*-' * 20)


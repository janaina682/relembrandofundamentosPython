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
while termo <= ultimo_termo:
    print('{} ->'.format(termo), end= ' ')
    termo += razao
mais_termos = int(input('\nQuantos termos você quer mostrar a mais? '))
while mais_termos !=0:
    ultimo_termo += mais_termos * razao
    while termo <= ultimo_termo:
        print('{} ->'.format(termo), end = '')
        termo += razao
    mais_termos = int(input('\nQuantos termos você quer mostrar a mais? digite [0] para sair: '))
print('\n' + '*-*-' * 20)
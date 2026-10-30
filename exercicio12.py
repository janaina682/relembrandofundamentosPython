#exercicio 56
print('Exercicio 56 - informações de pessoas')

idades = 0
mais_velho = 0
nome_mais_velho = ''
mulher_nova = 0
for i in range(4):
    print('##### Cadastro da {}° pessoa #####'.format(i+1))
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite "F" para feminino ou "M" para masculino: ').upper()
    idades += idade
    media = idades /4
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade > 20:
        mulher_nova += 1
    

print('A média de idade do grupo é: {}'.format(media))
print('O homem mais velho é o {}, com {} anos'.format(nome_mais_velho,mais_velho))
print('Tem {} mulheres com menos de 20 anos'.format(mulher_nova))


    

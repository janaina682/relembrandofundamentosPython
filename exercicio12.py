#exercicio 56
print('Exercicio 56 - informações de pessoas')

idades = 0
mais_velho = 0
nome_mais_velho = ''
mulher_nova = 0
for i in range(4):
    print(f'##### Cadastro da {i+1}° pessoa #####')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input(f'Digite "F" para feminino ou "M" para masculino: ').upper()
    idades += idade
    media = idades /4
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulher_nova += 1
    

print(f'A média de idade do grupo é: {media}')
print(f'O homem mais velho é o {nome_mais_velho}, com {mais_velho} anos')
print(f'Tem {mulher_nova} mulheres com menos de 20 anos')


    

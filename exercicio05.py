#exercicio 22
print('Exercício 22 - Analisando um nome')
nome = input('Digite seu nome: ').strip()
print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
print(f'Quantidade de letras no nome: {len(nome.replace(" ", ""))}')
print(f'Quantidade de letras do primeiro nome: {len(nome.split()[0])}')
print('-' * 20)

#exercicio 23
print('Exercício 23 - Separando digitos de um número')
numero = int(input('Digite um número entre 0 e 9999: '))
print(f'Unidade: {numero // 1 % 10}')
print(f'Dezena: {numero // 10 % 10}')
print(f'Centena: {numero // 100 % 10}')
print(f'Milhar: {numero // 1000 % 10}')
print('-' * 20)

#exercício 24
print('Exercício 24 - Analisar strings')
cidade = input('Digite o nome da cidade: ').strip()
print(f'A cidade começa com "Santo"? {cidade[:5].upper() == "SANTO"}')
print('-*' * 20)

#exercício 25
print('Exercício 25 - Procurando uma string dentro de outra')
nome_completo = input('Digite seu nome completo: ').strip()
print(f'Seu nome tem Silva? {"SILVA" in nome_completo.upper()}')
print('-' * 20)

#exercicio 26
print('Exercicio 26 - primeira e última ocorecia na string')
frase = input('Digite uma frase qualquer: ').strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes na frase')
print(f'O primeiro "A" está na posição {frase.find("A") + 1}')
print(f'E o último "A" está na posição {frase.rfind("A") + 1}')
print('-*' * 20)

#exercicio 27
print(f'Primeiro e ultimo nome: {nome_completo.split()[0]} {nome_completo.split()[-1]}')
print(f'Primeiro nome: {nome_completo.split()[0]}')

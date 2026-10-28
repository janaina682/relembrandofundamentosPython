#exercicio 22
print('Exercício 22 - Analisando um nome')
nome = input('Digite seu nome: ').strip()
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras no nome: {}'.format(len(nome.replace(' ', ''))))
print('Quantidade de letras do primeiro nome: {}'.format(len(nome.split()[0])))
print('-' * 20)

#exercicio 23
print('Exercício 23 - Separando digitos de um número')
numero = int(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(numero // 1 % 10))
print('Dezena: {}'.format(numero // 10 % 10))
print('Centena: {}'.format(numero // 100 % 10))
print('Milhar: {}'.format(numero // 1000 % 10))
print('-' * 20)

#exercício 24
print('Exercício 24 - Analisar strings')
cidade = input('Digite o nome da cidade: ').strip()
print('A cidade começa com "Santo"? {}'.format(cidade[:5].upper() == 'SANTO'))
print('-*' * 20)

#exercício 25
print('Exercício 25 - Procurando uma string dentro de outra')
nome_completo = input('Digite seu nome completo: ').strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome_completo.upper()))
print('-' * 20)

#exercicio 26
print('Exercicio 26 - primeira e última ocorecia na string')
frase = input('Digite uma frase qualquer: ').strip().upper()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('O primeiro "A" está na posição {}'.format(frase.find('A') + 1))
print('E o último "A" está na posição {}'.format(frase.rfind('A') + 1))
print('-*' * 20)

#exercicio 27
print('Primeiro e ultimo nome: {} {}'.format(nome_completo.split()[0], nome_completo.split()[-1]))
print('Primeiro nome: {}'.format(nome_completo.split()[0]))

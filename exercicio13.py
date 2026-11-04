#exercicio 57
print('Exercicio 57 - Validação de sexo')
sexo = str(input('Digite o sexo da pessoa: [M] para masculino e [F] para feminino: ')).upper()

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor digite o sexo da pessoa: [M] ou [F]: ')).upper()
    
if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')
print('*-*-' * 20)

#exercicio 58

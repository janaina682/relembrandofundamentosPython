#exercicio 71
print('Exercicio 71 - Caixa eletronico')
print('-' * 40)
print('{:-^40}'.format('Banco Vale'))
print('-' * 40)
valor = int(input('Quanto você deseja sacar? '))
total = valor
cedula = 50
qtde_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        qtde_cedula += 1
    else:
        if qtde_cedula > 0:
            print(f'{qtde_cedula} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        qtde_cedula = 0
        if total == 0:
            break
print(f'Vc sacou {valor}')

    
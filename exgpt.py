'''processos = [
    {"numero": 801, "ativo": True, "valor": 800},
    {"numero": 802, "ativo": False, "valor": 400},
    {"numero": 803, "ativo": True, "valor": 250},
    {"numero": 804, "ativo": True, "valor": 900}
]
processos_revisao = [
    processo["numero"]
    for processo in processos
    if not processo["ativo"] or processo["valor"] < 500
]
print(processos_revisao)

valores_ativos = [
    processo["valor"] * 2
    for processo in processos
    if processo["ativo"]
]
print(valores_ativos)
'''
'''
processos = [
    {"numero": 801, "ativo": True, "valor": 800},
    {"numero": 802, "ativo": False, "valor": 400},
    {"numero": 803, "ativo": True, "valor": 250},
    {"numero": 804, "ativo": True, "valor": 900}
]
resultado = [
    processo["numero"]
    for processo in processos
    if processo["ativo"] and processo["valor"] >= 500
]
print(resultado)
'''
'''
processos = [
    {"numero": 801, "ativo": True, "valor": 800},
    {"numero": 802, "ativo": False, "valor": 400},
    {"numero": 803, "ativo": True, "valor": 250}
]
processos_relevantes = {
    processo["numero"] : processo["valor"]
    for processo in processos
    if processo["ativo"] and processo["valor"] >300
}
print(processos_relevantes) 
'''
'''
processos = [
    {"numero": 901, "ativo": True, "valor": 150},
    {"numero": 902, "ativo": False, "valor": 600},
    {"numero": 903, "ativo": True, "valor": 900},
    {"numero": 904, "ativo": True, "valor": 450}
]
processos_selecionados = {
    processo["numero"] : processo["valor"]
    for processo in processos
    if processo["ativo"] and processo["valor"] < 500
}
print(processos_selecionados)
'''
processos = [
    {"numero": 901, "ativo": True, "valor": 150},
    {"numero": 902, "ativo": False, "valor": 600},
    {"numero": 903, "ativo": True, "valor": 900},
    {"numero": 904, "ativo": True, "valor": 450}
]
valores_por_status = {
    processo["numero"]: ('Ativo' if processo["ativo"] else 'Inativo')
    for processo in processos
}
print(valores_por_status)
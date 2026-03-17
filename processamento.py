def processar_alunos(alunos):
    print("sucesso")

def calcular_media(notas):
    return sum(notas) / len(notas)

def processar_alunos(alunos):
    for nome, notas in alunos:
        if notas:
            media = calcular_media(notas)
            print(f"{nome} - Média: {media:.2f}")

def calcular_media(notas):
    return sum(notas) / len(notas)

def validar_notas(notas):
    return isinstance(notas, list) and len(notas) > 0

def processar_alunos(alunos):
    for nome, notas in alunos:
        if not validar_notas(notas):
            print(f"{nome} - Dados inválidos")
            continue

        media = calcular_media(notas)
        print(f"{nome} - Média: {media:.2f}")
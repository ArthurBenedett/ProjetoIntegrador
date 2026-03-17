def processar_alunos(alunos):
    print("sucesso")

def calcular_media(notas):
    return sum(notas) / len(notas)

def processar_alunos(alunos):
    for nome, notas in alunos:
        if notas:
            media = calcular_media(notas)
            print(f"{nome} - Média: {media:.2f}")
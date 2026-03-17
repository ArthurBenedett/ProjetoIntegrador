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
    top_aluno = None
    maior_media = 0

    for nome, notas in alunos:
        if not validar_notas(notas):
            print(f"{nome} - Dados inválidos")
            continue

        media = calcular_media(notas)

        if media < 7:
            print(f"{nome} - Média: {media:.2f} (Recuperação)")
        else:
            print(f"{nome} - Média: {media:.2f}")

        if media > maior_media:
            maior_media = media
            top_aluno = nome

    print(f"\nTop Student: {top_aluno} com média {maior_media:.2f}")
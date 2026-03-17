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
    relatorio = []
    top_aluno = None
    maior_media = 0

    for nome, notas in alunos:
        if not validar_notas(notas):
            relatorio.append(f"{nome} - Dados inválidos")
            continue

        media = calcular_media(notas)

        status = "Recuperação" if media < 7 else "Aprovado"
        relatorio.append(f"{nome} - Média: {media:.2f} ({status})")

        if media > maior_media:
            maior_media = media
            top_aluno = nome

    relatorio.append(f"\nTop Student: {top_aluno} com média {maior_media:.2f}")

    with open("resultado.txt", "w") as f:
        for linha in relatorio:
            f.write(linha + "\n")

    print("Relatório gerado com sucesso!")
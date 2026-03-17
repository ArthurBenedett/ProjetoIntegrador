def validarNotas(notas):
    if not isinstance(notas, list) or len(notas) == 0:
        return False
    for nota in notas:
        if not isinstance(nota, (int, float)):
            return False
    return True

#aqui eu caculo a media
def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)

# validacao da notas
def processarAlunos(dados):
    resultados = []
    recuperacao = []
    topStudent = None
    maiorMedia = 0

    for nome, notas in dados:
        if not validarNotas(notas):
            print(f"Dados invalidos para {nome}")
            continue

        media = calcularMedia(notas)
        resultados.append((nome, media))

        if media < 7:
            recuperacao.append((nome, media))

        if media > maiorMedia:
            maiorMedia = media
            topStudent = (nome, media)

    return resultados, recuperacao, topStudent

#geracao do arquivo txt
def gerarRelatorio(resultados, recuperacao, topStudent):
    with open("resultado.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE DESEMPENHO\n")
        f.write("-"*30)

        f.write("media dos aluno:\n")
        for nome, media in resultados:
            f.write(f"{nome}: {media:.2f}\n")

        f.write("\nalunos em recuperação:\n")
        for nome, media in recuperacao:
            f.write(f"{nome}: {media:.2f}\n")

        f.write("\nbom aluno:\n")
        if topStudent:
            f.write(f"{topStudent[0]}: {topStudent[1]:.2f}\n")
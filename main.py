from processamento import processarAlunos, gerarRelatorio

alunos = [
    ("Arthur Benedetti", [8, 7.5, 9]),
    ("Esther Scartozzoni", [4, 5, 6]),
    ("Fabio Henrique Pacheco", [6, 5, 6.5]),
    ("Bruno Pezzolato", []),
    ("Giovanni Buscarino", [10, 9, 9.5]),
]

resultados, recuperacao, topStudent = processarAlunos(alunos)

gerarRelatorio(resultados, recuperacao, topStudent)

print("Relatorio gerado com sucesso!!!")
from processamento import processar_alunos

def main():
    alunos = [
        ("Arthur", [8, 7, 9]),
        ("Maria", [5, 6, 5]),
        ("João", [])
    ]

    processar_alunos(alunos)

if __name__ == "__main__":
    main()
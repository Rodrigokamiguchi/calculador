def main():
    nome_aluno = input("Informe o nome do aluno: ")
    nota = []
    menorNota = maiorNota = 0.0
    posicaoMenor = posicaoMaior = 0
    somaNotas = 0.0

    while True:
        qtd = int(input("Informe a quantidade de provas: "))
        if 1 <= qtd <= 10:
            break
        print("Atenção!!! Entre 1 e 10 ")

    for i in range(qtd):
        notaAtual = float(input(f"Informe a {i + 1}ª nota do aluno: "))
        nota.append(notaAtual)
        somaNotas += notaAtual

        if i == 0:
            menorNota = maiorNota = notaAtual
            posicaoMenor = posicaoMaior = 1
        
        else:
            if notaAtual < menorNota:
                menorNota = notaAtual
                posicaoMenor = i + 1
            elif notaAtual > maiorNota:
                maiorNota = notaAtual
                posicaoMaior = i+1

    media = somaNotas / qtd

    if media >= 6:
        print("\nAprovado")
    else:
        print("\nReprovado")

    print(f"\nA soma das notas: {somaNotas: .2f}")
    print(f"\nA meida das notas: {media: .2f}")
    print(f"\nA maior nota de {nome_aluno}: {maiorNota: .2f}, que esta na prova número {posicaoMaior}")
    print(f"\nA menor nota de {nome_aluno}: {menorNota: .2f}, que esta na prova número {posicaoMenor}")

if __name__ == "__main__":
    main()
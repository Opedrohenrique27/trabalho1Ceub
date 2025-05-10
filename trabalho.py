def analise_valores():
    valores = []
    while True:
        try:
            valor = float(input("Digite um valor real (ou '0' para encerrar): "))
            if valor == 0:
                break
            valores.append(valor)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    quantidade = len(valores)
    soma = sum(valores)
    media = soma / quantidade if quantidade > 0 else 0
    maiores_que_20 = sum(1 for v in valores if v > 20)

    print(f"Quantidade de valores digitados: {quantidade}")
    print(f"Soma dos valores: {soma}")
    print(f"Média aritmética: {media:.2f}")
    print(f"Quantidade de valores maiores que 20: {maiores_que_20}")


def analise_notas():
    aprovados = reprovados = total_alunos = 0
    while True:
        try:
            nota = float(input("Digite a nota do aluno (ou '-1' para encerrar): "))
            if nota == -1:
                break
            total_alunos += 1
            if nota >= 5:
                aprovados += 1
            else:
                reprovados += 1
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    print(f"Total de alunos que fizeram a prova: {total_alunos}")
    print(f"Quantidade de alunos aprovados: {aprovados}")
    print(f"Quantidade de alunos reprovados: {reprovados}")


def media_pares_impares():
    pares = []
    impares = []
    while True:
        try:
            numero = int(input("Digite um número inteiro (ou '0' para encerrar): "))
            if numero == 0:
                break
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    media_pares = sum(pares) / len(pares) if pares else 0
    media_impares = sum(impares) / len(impares) if impares else 0

    print(f"Média dos números pares: {media_pares:.2f}")
    print(f"Média dos números ímpares: {media_impares:.2f}")


if __name__ == "__main__":
    print("\n--- Problema 1 ---")
    analise_valores()
    print("\n--- Problema 2 ---")
    analise_notas()
    print("\n--- Problema 3 ---")
    media_pares_impares()

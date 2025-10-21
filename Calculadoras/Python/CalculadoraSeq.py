import re

print("Esta é uma calculadora sequencial de python. Ela executa operações estritamente da esquerda para a direita")
print("Digite a sequência de operações a serem realizadas ou 'q' ou 'Ctrl + C' para sair.")

Ans = []

while (1):
    print("Digite as operações: ")
    seq = input()
    if ('q' in seq):
        break

    if (len(seq) == 0):
        continue
    arga = re.split(r'(\+) | (\-) | (\*) | (\\) | \s+', seq, maxsplit = 0)
    if (len(seq) == 0):
        print(arga)
        continue

    op = re.split(r'(\d+)', seq, maxsplit = 0)
    if (len(seq) == 0):
        print("Sequência de operações incompleta, tente novamente!")
        continue
    argb = re.split(r'(\+) | (\-) | (\*) | (\\) | \s+', seq, maxsplit = 0)

    print(arga)
    numa = int(arga)
    numb = int(argb)

    if (op == '+'):
        res = numa + numb
    elif (op == '-'):
        res = numa - numb
    elif (op == '*'):
        res = numa * numb
    elif (op == '/'):
        try:
            res = numa / numb
        except ZeroDivisionError:
            print("Erro! Divisão por zero")
            continue
    else:
        print("Operação Inválida! Operações Disponíveis: '+', '-', '*', '/'.")
        continue

    
import re

print("Esta é uma calculadora sequencial de python. Ela executa operações estritamente da esquerda para a direita.")
print("Digite a sequência de operações a serem realizadas ou 'q' ou 'Ctrl + C' para sair.")

Ans = []

while (1):
    print("Digite as operações: ")
    seq = input()
    if ('q' in seq):
        break

    if (len(seq) == 0):
        continue

    ops = seq.split()

    #print(ops)
    i = 0
    valid = True
    while ((len(ops) > 1) and (i <= len(ops))):

        if ((not isinstance(ops[i], int)) or (not isinstance(ops[i + 2], int))):
            print("Operando não é um número!")
            valid = False
            i += 3
            break
        
        numa = int(ops[i])
        op = ops[i + 1]
        numb = int(ops[i + 2])

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

        ops.insert(0, res)
        i += 3

    if (valid):
        print(f"Seu resultado é: {res}")
        Ans.insert(0, res)
        

    
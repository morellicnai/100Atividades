nota = -1
while nota < 0 or nota > 10:
    nota = float(input("Digite a nota (entre 0 e 10): "))
    if nota < 0 or nota > 10:
        print("Valor inválido! Digite uma nota entre 0 e 10.")

print(f"A nota digitada foi {nota}.")

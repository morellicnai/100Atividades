num = int(input("Digite um número inteiro: "))
fat = 1

if num < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif num == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, num+1):
        fat *= i
    print("O fatorial de", num, "é", fat)

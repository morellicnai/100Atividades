n = int(input("Quantas pessoas serão incluídas na turma? "))

soma_idades = 0

for i in range(n):
    idade = int(input("Informe a idade da pessoa {}: ".format(i+1)))
    soma_idades += idade

media_idades = soma_idades / n

if media_idades <= 25:
    print("A turma é jovem, com média de idade {:.1f} anos".format(media_idades))
elif media_idades <= 60:
    print("A turma é adulta, com média de idade {:.1f} anos".format(media_idades))
else:
    print("A turma é idosa, com média de idade {:.1f} anos".format(media_idades))

numero = int(input("Digite um numero"))
soma = 0
for x in range(0, 6):
    if numero % 2 == 0:
        soma += numero
print(soma)

num = 1
triangular = 0
contador = 0

while contador <= 500:
    contador = 0
    triangular += num
    num += 1

    for i in range(1, int(triangular**0.5) + 1):
        if triangular % i == 0:
            if i * i == triangular:
                contador += 1
            else:
                contador += 2

print(triangular)

#Localiza o primeiro número que tenha mais de 500 divisores
n = 2
soma = 0


for p in range(2, 2000000):
    primo = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break

    if primo == True:
        soma += n

    n += 1

print(soma)

#Soma todos os primos abaixo de 2 milhões
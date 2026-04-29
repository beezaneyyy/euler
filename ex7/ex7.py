contador = 0
n = 2

while contador != 10001:
    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break

    if primo == True:
        contador += 1
        resultado = n
        

    n += 1

print (resultado)

#Acha o 10001º número primo
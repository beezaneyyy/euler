num = 1
max = 0
numero = 0

while num < 1000000: 
    chain = 0
    i = num
    i = i

    while i != 1:
        if i % 2 == 0:
            i = i / 2
        else:
            i = i * 3 + 1

        chain += 1

    if max < chain:
        max = chain
        numero = num

    num = num + 1

print (numero)

#Acha um número abaixo de 1000000 que produz a maior corrente de Collatz
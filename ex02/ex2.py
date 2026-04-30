a = 1
b = 2
soma = 0

while a <= 4000000:
    if a % 2 == 0:
        soma += a
    a, b = b, a + b
print(soma)

#soma os termos pares da sequência de fibonacci
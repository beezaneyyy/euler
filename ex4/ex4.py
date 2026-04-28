maior = 0
for a in range (999, 99, -1):
    for b in range (999, 99, -1):
        produto = a * b 
        invertido = str(produto)[::-1]
        if produto <= maior:
            break
        if str(produto) == invertido:
            if produto > maior:
                maior = produto
print(maior)
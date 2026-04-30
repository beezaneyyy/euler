soma = 0
soma_quadrados = 0

for i in range(1, 101):
    soma += (i ** 2)

for i in range(1, 101):
    soma_quadrados += i

quadrados = soma_quadrados ** 2

resultado = quadrados - soma

print(resultado)

"""
Diferença da soma dos quadrados e do quadrado das somas
dos 100 primeiros números naturais
"""
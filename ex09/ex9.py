for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b

        if (a ** 2) + (b ** 2) == (c ** 2):
            produto = a * b * c

print(produto)

#Acha o produto entre a, b, c que somam 1000 e satisfazem o pitágoras
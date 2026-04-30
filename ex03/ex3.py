n = 600851475143

while n != 1:
    for i in range(2, int(n+1)):
        if n % i == 0:
            n = n / i
            print(i)
            break

#acha o maior fator primo do número 600851475143 
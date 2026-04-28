num = 20
while True:
    divisivel = True
    for i in range(20, 0, -1):
        if num % i != 0:
            divisivel = False
            break
    if divisivel:
        print(num)
        break
    else:
        num += 20
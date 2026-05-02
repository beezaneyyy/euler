unidades = {
    0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
}

dezenas = {
    2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 
    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
}

soma = 0

for n in range(1, 1001):
    palavra = ""
    
    if n == 1000:
        palavra = "onethousand"
    else:

        if n >= 100:
            palavra += unidades[n // 100] + "hundred"
            if n % 100 != 0:
                palavra += "and"
        
        resto = n % 100
        if 0 < resto < 20:
            palavra += unidades[resto]
        elif resto >= 20:
            palavra += dezenas[resto // 10] + unidades[resto % 10]
    
    soma += len(palavra)

print(soma)
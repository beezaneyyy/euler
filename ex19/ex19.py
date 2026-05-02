meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dia_da_semana = 1
domingos_no_dia_primeiro = 0

for ano in range(1900, 2001):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        meses[1] = 29
    else:
        meses[1] = 28
    
    for mes in meses:
        if ano >= 1901 and dia_da_semana == 0:
            domingos_no_dia_primeiro += 1
        
        dia_da_semana = (dia_da_semana + mes) % 7

print(domingos_no_dia_primeiro)

#Retorna quantos domingos cairam no dia primeiro no século 20
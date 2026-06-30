def calculate(x, percent_decimal, aug):
    y: int = int(x + x * percent_decimal + aug)
    return y

def nb_year(p0, percent, aug, p):
    percent_decimal = percent / 100
    valor = calculate(p0, percent_decimal, aug)
    year = 1
    
    while valor < p:
        valor = calculate(valor, percent_decimal, aug)
        year += 1
        
    return year

calculate(1000,0.02,50)
print(nb_year(1000,2,50,1200))
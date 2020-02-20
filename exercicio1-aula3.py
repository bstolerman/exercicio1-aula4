import datetime
def calcular_dias_de_vida(year, month, day): 

    hoje = datetime.date.today()
    data = datetime.date(year, month, day)
    retorno = hoje - data

    return retorno

year = int(input('Ano de nascimento: '))
month = int(input('Mês de nascimento: '))
day = int(input('Dia de nascimento: '))

retorno = calcular_dias_de_vida(year, month, day)
print(retorno)




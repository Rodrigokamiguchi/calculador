def calcular_idade_dias_mes(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    dias = idade * 365
    mes = dias / 30

    return idade, dias, mes

def ano_bissexto(ano):
    return(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def calcular_dias_mes_com_bissexto(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    anos_bissexto = 0
    for ano in range(ano_nascimento, ano_atual + 1):
        if ano_bissexto(ano):
            anos_bissexto += 1
    dias = (idade * 365) + anos_bissexto
    mes = (dias / 30) + anos_bissexto

    return idade, dias, mes

def main():
    ano_atual = int(input("Digite o ano atual: "))
    ano_nascimento = int(input("Digite o ano de nascimento: "))

    idade, dias, mes = calcular_idade_dias_mes(ano_atual, ano_nascimento)
    print(f"\n Sua idade é: {idade} anos")
    print(f"\n Isso corresponde a aproximadamente: {dias} dias")
    print(f"\n Isso corresponde a aproximadamente: {mes: .2f} meses\n")
    
    idade, dias, mes = calcular_dias_mes_com_bissexto(ano_atual, ano_nascimento)
    print(f"\n Sua idade é: {idade} anos")
    print(f"\n Isso corresponde a aproximadamente: {dias} dias")
    print(f"\n Isso corresponde a aproximadamente: {mes: .2f} meses\n")

if __name__ == "__main__":
    main()
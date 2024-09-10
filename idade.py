def calcular_idade_e_dias(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento

    dias = idade *365

    return idade, dias

def ano_bissexto(ano):
    return(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def calcular_dias_com_bissexto(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    anos_bissextos = 0

    for ano in range(ano_nascimento, ano_atual + 1):
        if ano_bissexto(ano):
            anos_bissextos +=1
    dias = (idade * 365) + anos_bissextos
    
    return idade, dias
def main():
    ano_atual = int(input("Digite o ano atual: "))

    ano_nascimento = int(input("Digite o ano de nascimento: "))

    idade, dias = calcular_idade_e_dias(ano_atual, ano_nascimento)
    print(f"\n Sua idade é: {idade} anos")
    print(f"\n Isso corresponde a aproximadamente: {dias} dias")

    idade, dias = calcular_dias_com_bissexto(ano_atual, ano_nascimento)
    print(f"\n Considerando anos busssextos, sua idade é: {idade} anos")
    print(f"\n Isso corresponde a aproximadamente: {dias} dias\n")

if __name__ == "__main__":
    main()
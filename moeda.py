import requests
def obter_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor númerico.")

def obter_taxa(moeda_base, moeda_destino):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{moeda_base}"
        response = requests.get(url)
        dados = response.json()

        return dados['rates'][moeda_destino]
    except Exception as e:
        print(f"erro ao obter a taxa de câmbio: {e}")
        return None

def converter_valor(valor, taxa):
    return valor * taxa

def exibir_resultado(valor, taxa, valor_convertido, moeda_destino):
    print(f"\nValor original: R${valor: .2f}")
    print(f"Taxa de conversão: {taxa: .4f}")
    print(f"Valor convertido: {moeda_destino} {valor_convertido: .2f}")

def main():
    valor = obter_valor("Informe o valor do produto em reais: R$")
    moeda_destino = input("Informe o codigo da moeda estrangeira(ex.: USD, EUR, GBP): ").upper()

    moeda_base = "BRL"
    taxa = obter_taxa(moeda_base, moeda_destino)

    if taxa:
        valor_convertido = converter_valor(valor, taxa)
        exibir_resultado(valor, taxa, valor_convertido, moeda_destino)
    else:
        print("Não foi possivel obter a taxa de câmbio. Tente novamente mais tarde.")

if __name__ == "__main__":
    main()
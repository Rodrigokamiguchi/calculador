def main():
    nome = input("Qual o seu nome? ")
    print(f"olá, {nome}! Bem-vindo á calculadora.")
if __name__ == "__main__":
    main()

def adicionar (a, b):
    return a + b
def subtrair (a, b):
    return a - b 
def multiplicar (a , b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Erro!!, Divisão por zero"
    return a / b
def porcentagem(a, b):
    return (a * b) / 100
def resto_divisao(a , b):
    if b == 0:
        return "Erro, Divisao por zero"
    return a % b
def media_aritmetica(numeros):
    if len(numeros) == 0:
        return "Erro, sem números para calcular a média"
    return sum(numeros) / len(numeros)

def mostrar_menu():
    print("Escolha uma operação")
    print("1, Adição")
    print("2, Subtração")
    print("3, Multiplicação")
    print("4, Divisão")
    print("5, Porcetagem")
    print("6, Resto da Divisão")
    print("7, Media Aritmetica")


while True:
    mostrar_menu()
    escolha = input("Digite o número da operação (1,2,3,4,5,6) ou sair para encerrar: ")

    if escolha.lower() == 'sair':
        print(f"Até mais!")
        break
    if escolha in ['1', '2', '3', '4', '5', '6', '7']:
        try:
            if escolha == '5':
                num3 = float(input("Digite o número: "))
                porcentagem_valor = float(input("Digite a porcetagem: "))
                resultado = porcentagem(num3, porcentagem_valor)
                print(f"Resultado {resultado}")
            elif escolha == '6':
                num1 = float(input("Digite o dividendo: "))
                num2 = float(input("Digite o divisor: "))
                resultado = resto_divisao(num1, num2)
                print(f"Resultado{resultado}")
            elif escolha == '7':
                qtd_numeros = int(input("Quantos numeros deseja calcular a média? "))
                numeros = []
                for i in range(qtd_numeros):
                    numero = float(input(f"Digite o {i+1}º número: "))
                    numeros.append(numero)
                resultado = media_aritmetica(numeros)
                print(f"Media Aritmetica: {resultado}")
            else:
                num1 = float(input("Digite o primeiro numero: "))
                num2 = float(input("Digite o segundo numero: "))

            if escolha == '1':
                print(f"Resultado: {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {dividir(num1, num2)}")
        except ValueError:
            print("Entrada inválida, Por favor, insira números válidos.")
    else:
        print("Escolha invalida. Tente novamente.")


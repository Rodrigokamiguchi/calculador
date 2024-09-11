#Bibliotecas

import math
import tkinter as tk
from tkinter import messagebox

#Apresentação

def main():
    global nome
    nome = input("Qual o seu nome? ")
    print(f"olá, {nome}! Bem-vindo á calculadora.")
if __name__ == "__main__":
    main()

# Funções de cálculo

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

def numero_maior(a, b):
    
    if a > b:
        return f"O maior numero é: {a:.2f}\nO menor numero é: {b:.2f}"
    elif b > a:
        return f"O maior numero é: {b:.2f}\nO menor numero é: {a:.2f}"
    else:
        return "Os numeros são iguais"
    
def idade(ano_atual, ano_nascimento):
   
    return ano_atual - ano_nascimento

def area_do_triangulo(largura, comprimento):
    
   return largura * comprimento

def antecessor_sucessor(numero):
  
  return (numero - 1, numero + 1)

def celsius_to_fahrenheit(celsius):
    
    return (celsius*9/5)+32

def fahrenheit_to_celsius(fahrenheit):
   
    return (fahrenheit-32)*9/5

def expotenciacao(a, b):
    
    return a ** b

def raiz_quadrada(a):
    
    if a < 0:
        return "Erro! Raiz quadrada negativa"
    return math.sqrt(a)

#função para exibir resultados

def exibir_resultados(resultado):
    if isinstance(resultado, str):
        messagebox.showerro("Erro", resultado)
    else:
        messagebox.showinfo("Resultado", f"Resultado: {resultado:.2f}")

#função chamada quando o botão é pressionado

def calcular():
    try:
        operacao = operacao_var.get()
        if operacao in ["1", "2", "3", "4" , "5", "6", "7", "8","9", "10", "11", "12", "13", "14", "15"]:
            if operacao in ["1", "2", "3", "4","5", "6", "8", "14"]:
                num1 = float(entry_num1.get())
                num2 = float(entry_num2.get())
                if operacao == "1":
                    resultado = adicionar(num1, num2)
                elif operacao == "2":
                    resultado = subtrair(num1, num2)
                elif operacao == "3":
                    resultado = multiplicar(num1, num2)
                elif operacao == "4":
                    resultado = dividir(num1, num2)
                elif operacao == "5":
                    resultado = porcentagem(num1, num2)
                elif operacao == "6":
                    resultado = resto_divisao(num1, num2)
                elif operacao == "8":
                    resultado = numero_maior(num1, num2)
                elif operacao == "14":
                    resultado = expotenciacao(num1, num2)
            elif operacao == "7":
                numeros = list(map(float, entry_numeros.get().split()))
                resultado = media_aritmetica(numeros)
            elif operacao == "9":
                ano_atual = int(entry_num1.get())
                ano_nascimento = int(entry_num2.get())
                resultado = idade(ano_atual, ano_nascimento)
            elif operacao == "10":
                
            elif operacao == "11":
            elif operacao == "12":
            elif operacao == "13":
            elif operacao == "15":
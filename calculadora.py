import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Divisão por zero não é permitida"
    else:
        return a / b

print("Calculadora")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")
opcao = int(input("Digite o número da operação desejada: "))

if opcao == 1:
    resultado = somar(num1, num2)
elif opcao == 2:
    resultado = subtrair(num1, num2)
elif opcao == 3:
    resultado = multiplicar(num1, num2)
elif opcao == 4:
    resultado = dividir(num1, num2)
else:
    resultado = "Opção inválida"

print("O resultado da operação é:", resultado)

print("=== Calculadora ===")
print("1 - Adicao")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

opcao = int(input("Escolha (1 a 4): "))
valor1 = float(input("Primeiro valor: "))
valor2 = float(input("Segundo valor: "))

if opcao == 1:
    resultado = valor1 + valor2
    print("Resultado:", resultado)
elif opcao == 2:
    resultado = valor1 - valor2
    print("Resultado:", resultado)
elif opcao == 3:
    resultado = valor1 * valor2
    print("Resultado:", resultado)
else:
    resultado = valor1 / valor2
    print("Resultado:", resultado)

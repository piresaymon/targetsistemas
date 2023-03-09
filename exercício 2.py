# Define o número a ser verificado
numero_verificar = int(input("Digite um número: "))

# Inicializa as variáveis da sequência de Fibonacci
fibonacci_anterior = 0
fibonacci_atual = 1

# Verifica se o número informado pertence à sequência de Fibonacci
while fibonacci_atual < numero_verificar:
    fibonacci_proximo = fibonacci_anterior + fibonacci_atual
    fibonacci_anterior = fibonacci_atual
    fibonacci_atual = fibonacci_proximo

if fibonacci_atual == numero_verificar:
    print(numero_verificar, "pertence à sequência de Fibonacci.")
else:
    print(numero_verificar, "não pertence à sequência de Fibonacci.")

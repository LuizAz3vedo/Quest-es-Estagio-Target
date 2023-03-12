# 2 Questão
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return b == n

# Exemplo:
n = int(input("Informe um número para a verificação: "))
if fibonacci(n):
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")
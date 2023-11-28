def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Gerar os primeiros 15 números da sequência de Fibonacci
result = fibonacci(15)

# Imprimir o resultado
print(result)
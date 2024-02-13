def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def main():
    secuencia = 10
    print("Secuencia de Fibonacci:")
    for i in range(secuencia):
        print(fibonacci(i))


main()

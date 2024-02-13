def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def main():
    num = factorial(5)
    print(num)


main()

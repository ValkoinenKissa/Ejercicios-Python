def convertirBinario(num, base):
    if(num < base):
        print(num, end="")
    else:
        convertirBinario(num//base, base)
        print(num % base, end="")


def main():
    num = int(input("Introduce un numero: "))
    # Aqui puedes modificar la base por otra, para poder calcular por ejemplo el octal o el hex
    base = 2
    convertirBinario(num, base)

main()
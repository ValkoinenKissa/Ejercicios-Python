password = "contrasena"

valor = input("Introduce una contraseña: ")

while valor != password:
    valor = input("La password no es correcta vuelve a introducirla: ")

print("La contraseña introducida es correcta")

aeropuerto = input("introduce el nombre del aeropuerto:")
match aeropuerto:
    case "Barajas":
        ciudad = "Madrid"
    case "Orly":
        ciudad = "París"
    case "Heathrow":
        ciudad = "Londres"
    case "Schiphol":
        ciudad = "Amsterdam"
    case _:
        ciudad = "No sé a que ciudad corresponde"

print(ciudad)



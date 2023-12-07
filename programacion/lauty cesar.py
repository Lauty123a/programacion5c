def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ''
    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                texto_cifrado += chr((ord(caracter) - 65 + desplazamiento) % 26 + 65)
            else:
                texto_cifrado += chr((ord(caracter) - 97 + desplazamiento) % 26 + 97)
        else:
            texto_cifrado += caracter
    return texto_cifrado

def obtener_desplazamiento():
    while True:
        try:
            desplazamiento = int(input("Ingrese el número de desplazamientos (1-26): "))
            if 1 <= desplazamiento <= 26:
                return desplazamiento
            else:
                print("Por favor, ingrese un número entre 1 y 26.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

texto_original = input("Ingrese el texto a cifrar: ")
desplazamiento = obtener_desplazamiento()

texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)
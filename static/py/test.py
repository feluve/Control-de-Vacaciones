
# genera un programa que encripte una cadena de texto

def encrypt(plain_text):
    # convertir la cadena de texto a una lista de caracteres
    plain_text = list(plain_text)
    # convertir cada caracter a su valor ASCII
    plain_text = [ord(c) for c in plain_text]
    # encriptar cada caracter
    plain_text = [c + 2 for c in plain_text]
    # convertir cada caracter encriptado a su valor ASCII
    plain_text = [chr(c) for c in plain_text]
    # convertir la lista de caracteres encriptados a una cadena de texto
    plain_text = ''.join(plain_text)
    return plain_text


# genera una cadena de texto aleatoria de 32 caracteres que contenga letras mayusculas, minusculas numeros del 0-9 y caracteres especiales como @, ?, }
def generate_random_text():
    import random
    # lista de caracteres permitidos
    allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@?}'
    # generar una cadena de texto aleatoria de 32 caracteres
    random_text = ''.join(random.choice(allowed_chars) for i in range(32))
    return random_text

# genera un programa que desencripte una cadena de texto


def descrypt(plain_text):
    # convertir la cadena de texto a una lista de caracteres
    plain_text = list(plain_text)
    # convertir cada caracter a su valor ASCII
    plain_text = [ord(c) for c in plain_text]
    # desencriptar cada caracter
    plain_text = [c - 2 for c in plain_text]
    # convertir cada caracter desencriptado a su valor ASCII
    plain_text = [chr(c) for c in plain_text]
    # convertir la lista de caracteres desencriptados a una cadena de texto
    plain_text = ''.join(plain_text)
    return plain_text


# genera una cadena de texto aleatoria de 32 caracteres
text = generate_random_text()

print(f'La cadena de texto aleatoria es: {text}')

# imprieme la encriptacion de la cadena de texto
enc = encrypt(text)

# imprime enc
print(f'La cadena de texto encriptada es: {enc}')

# desencripta la cadena de texto
des = descrypt(enc)

# imprime des
print(f'La cadena de texto desencriptada es: {des}')

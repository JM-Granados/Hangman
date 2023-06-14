intentos_max = 10

def limpiarPantalla():
    """
    Subrutina que imprime las líneas en blanco para limpiar la pantalla.
    Entradas y restricciones: Ninguna
    Salida:
    40 líneas en blanco.
    """
    print("\n" * 40)

def imprimirEntrada():
    """
    Subrutina que imprime un mensaje de bienvenida.
    Entradas y restricciones: ninguna.
    Salidas:
    Mensaje de bienvenida.
    """
    print("Bienvenido a ")
    print("      ___           ___           ___           ___           ___           ___           ___           ___      ")     
    print("     /\  \         /\__\         /\  \         /\  \         /\  \         /\  \         /\  \         /\  \     ")
    print("    /::\  \       /:/  /        /::\  \       /::\  \       /::\  \       /::\  \       /::\  \       /::\  \    ")
    print("   /:/\:\  \     /:/__/        /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \   ")
    print("  /::\~\:\  \   /::\  \ ___   /:/  \:\  \   /::\~\:\  \   /:/  \:\  \   /::\~\:\  \   /:/  \:\__\   /:/  \:\  \  ")
    print(" /:/\:\ \:\__\ /:/\:\  /\__\ /:/__/ \:\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/\:\ \:\__\ /:/__/ \:|__| /:/__/ \:\__\ ")
    print(" \/__\:\/:/  / \/__\:\/:/  / \:\  \ /:/  / \/_|::\/:/  / \:\  \  \/__/ \/__\:\/:/  / \:\  \ /:/  / \:\  \ /:/  / ")
    print("      \::/  /       \::/  /   \:\  /:/  /     |:|::/  /   \:\  \            \::/  /   \:\  /:/  /   \:\  /:/  /  ")
    print("      /:/  /        /:/  /     \:\/:/  /      |:|\/__/     \:\  \           /:/  /     \:\/:/  /     \:\/:/  /   ")
    print("     /:/  /        /:/  /       \::/  /       |:|  |        \:\__\         /:/  /       \::/__/       \::/  /    ")
    print("     \/__/         \/__/         \/__/         \|__|         \/__/         \/__/         ~~            \/__/     ")
    print("Elaborado por Jose Manuel Granados.")
    
def leerTextoOriginal():
    """
    Función que lee de la consola la palabra o frase a ser adivinada y retorna como resultado el texto leído.
    Entradas y restricciones:
    - texto del usuario. Ninguna restricción.
    Salidas:
    Texto ingresado.
    """
    texto = input("Ingrese la palabra o frase a adivinar para comenzar el juego :). Recuerda que sólo puede contener letras y espacios: ")
    while not esTextoValido(texto):
        print("El texto solo puede contener letras y espacios :c ")
        texto = input("De nuevo, ingresa la palabra o frase a adivinar >:/. Y recuerda que sólo puede contener letras y espacios: ")
    return texto

def esTextoValido(texto):
    """
    Función booleana que dice si un string es un texto válido para adivinar en el juego.
    Entradas y restricciones:
    - texto a analizar, string.
    Salidas:
    True si el texto contiene sólo letras, espacios y tiene al menos un caracter, Flase si no.
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    if texto == "":
        return False
    for letra in texto:
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúvwxyz":
            return False
    return True

def preparar(texto):
    """
    Convierte el texto a miúsculas, sustituye acentos y elimina espacios al inicio y al final.
    Entradas y restricciones:
    - texto a procesar. String.
    Salidas:
    Tesxto sin mayúsculas, acentos y espacios al inicio y al final.
    """
    if type(texto) != str:
        raise Esception("Texto debe ser un string.")
    texto = texto.lower()
    texto = texto.strip()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("u", "u")
    return texto

def adivino(texto, intentadas):
    """
    Función booleana que dice si el usuario ya adivinó el texto.
    Entradas:
    - Texto: texto preparado (sin tildes, ni acentos). String
    - Intentadas: letras que el usuario ha intentado. 
    Salidas:
    True si todas las letras texto ya han sido intentadas
    False si no.
    """
    if type(texto) != str or type(intentadas) != str:
        raise Exception("El texto y las letras intentadas deben ser strings. ")
    if not esTextoValido(texto):
        raise Exception("El texto y las intentadas contienen caracteres no validos. ")
    for letra in texto:
        if letra != " ":
            if letra not in intentadas:
                return False
    return True

def imprimirRonda(texto, intentadas, intentos, ronda):
    """
    Función imprime los mensajes requeridos para cada ronda del juego. I
    mprime el número de ronda actual, un mensaje que indica las letras que ya fueron utilizadas,
    cantidad de intentos fallidos y también escribe el texto enmascarado.
    Entradas y restricciones:
    - texto : texto preparado sin tildes ni acentos.
    - intentadas : letras que el usuario ha intentado.
    - ronda : número de ronda por la que va el juego.
    Salidas:
    Impresión en pantalla de la información de la ronda.
    """
    print("\n" * 20)
    print("RONDA: ", ronda)
    print("Letras que ya fueron utilizadas: ", intentadas)
    print("Cantidad de intentos fallidos: ", intentos)
    print()
    print(enmascarar(texto, intentadas))
    print()

def enmascarar(texto, intentadas):
    """
    Retorna un string con un guión bajo por cada letra que no ha sido adivinada. Si una letra del texto aparece en las
    letras intentadas, entonces le agrega como tal en lugar del guión.
    Si el texto original tiene espacios, los sustituye con guiones normales.
    Entradas:
    - texto : texto a adivinar.
    - intentadas : letras qie eñ usuario ha intentado.
    Salidas:
    String con el texto enmascarado.
    """
    listaPalabras = texto.split()
    resultado = " "
    for palabra in listaPalabras:
        for letra in palabra:
            if letra in intentadas:
                resultado += letra + " "
            else:
                resultado += " _ "
        resultado += " - "
    return resultado[:-2] 

def leerIntento(intentadas):
    """
    Función que pide al usuario que escriba una letra para adivinar. Si ya se encuentra en las intentadas o no es una
    letra, debe imprimir un mensaje de error y volver a pedir la letra.
    Entradas y restricciones:
    - intentadas: letras que el usuario ha intentado.
    Salidas:
    String con la letra elegida por el usuario.
    """
    print()
    letra = input("Digita la letra que creas correcta: ")
    letra = letra.lower()
    while len(letra) != 1 or letra < "a" or letra not in "abcdefghijklmnñopqrstuvwxyz" \
          or letra in intentadas:
        print("Por favor ingrese una letra que no haya intentado. Intentadas: ")
        letra = input("Digita de nuevo una letra que creas correcta: ")
        letra = letra.lower()
    print()
    return letra

def aciertaIntento(texto, letra):
    """
    Función booleana que dice si un intento es correcto o no.
    Entradas:
    - texto que se está adivinando.
    - letra que intentó el usuario.
    Salidas:
    True si la letra se encuentra en el texto a adivinar.
    False si no.
    """
    return letra in texto

def imprimirMensajeAcierto():
    """
    Función que imprime en pantalla el mensaje de acierto cuando el usuario logró adivinar la letra.
    Entradas y restricciones: ningunas
    Salidas:
    Impresión en pantalla de haber acertado.
    """
    print("¡Has adivinado! :D")

def imprimirMensajeNoAcierto():
    """
    Función que imprime en pantalla el mensaje de que no acertó cuando el usuario no logró adivinar la letra.
    Entradas y restricciones: ningunas
    Salidas:
    Impresión en pantalla de no haber acertado.
    """
    print("¡La letra no fue encontrada :c!")

def imprimirMensajeVictoria(textoOriginal):
    """
    Función que imprime en pantalla el mensaje de victoria, cuando el usuario logró adivinar la palabra o frase y no
    gastó sus intentos.
    Entradas y restricciones:
    - texto procesado, string. 
    Salidas:
    Impresión en pantalla de victoria.
    """
    print("¡Felicidades :D! Has adivinado el texto: ", textoOriginal)
        
def imprimirMensajeDerrota(textoOriginal):
    """
    Función que imprime en pantalla el mensaje de que perdió, cuando el usuario no logró adivinar la palabra o frase y/o
    gastó sus intentos.
    Entradas y restricciones:
    - texto procesado, string. 
    Salidas:
    Impresión en pantalla de derrota.
    """
    print("Has perdido :c. El texto a adivinar era: ", textoOriginal)

def leerJugarNuevamente():
    """
    Función booleana que pregunta al usuario si desea jugar de nuevo. Sólo acepta "S" o "N" como respuesta.
    Entradas y restricciones: Ningunas.
    Salidas:
    True si el usuadio escribe "S", False si no.
    """
    print()
    respuesta = input("¿Deseas jufgar nuevamente? (S/N): ")
    respuesta = respuesta.lower()
    while respuesta not in ["s", "n"]:
        respuesta = input("¿Deseas jufgar nuevamente? (S/N): ")
        respuesta = respuesta.lower()
    return respuesta == "s"
        
def imprimirMensajeDespedida():
    """
    Función que imprime en pantalla el mensaje de despedida.
    Entradas y restricciones: Ningunas.
    Salidas:
    Impresión en pantalla de despedida.
    """
    print("Gracias por jugar ahorcado. Nos vamos pronto.")

def ahorcado():
    """
    Subrutina principal del juego de ahorcado.
    Entradas y restricciones: ningunas
    Salidas:
    El juego de ahorcado.

    Elaborado por Jose Manuel Granados V.
    """
    global intentos_max
    limpiarPantalla()
    imprimirEntrada()
    continuar = True
    while continuar:
        textoOriginal = leerTextoOriginal()
        limpiarPantalla()
        texto = preparar(textoOriginal)
        intentadas = ""
        intentos = 0
        ronda = 1
        while intentos < intentos_max and \
              not adivino(texto, intentadas):
            imprimirRonda(texto, intentadas, intentos, ronda)
            letraIntento = leerIntento(intentadas)
            if aciertaIntento(texto, letraIntento):
                imprimirMensajeAcierto()
            else:
                imprimirMensajeNoAcierto()
                intentos += 1
            intentadas += letraIntento
            ronda += 1
        if adivino(texto, intentadas):
            imprimirMensajeVictoria(textoOriginal)
        else:
            imprimirMensajeDerrota(textoOriginal)
        continuar = leerJugarNuevamente()
    imprimirMensajeDespedida()
    input()
ahorcado()

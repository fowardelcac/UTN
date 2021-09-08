#Turno 04 – Enunciado 01 [T4E1]
#1)Determinar la cantidad de palabras que tienen una o dos vocales (minúsculas o mayúsculas) y 5 caracteres o más en total.
#Por ejemplo, en el texto "Extraño salir a navegar los fines de semana.", hay 2 palabras que cumplen con la condición ("salir" y "fines").
#Por "caracteres", se entiende "cualquier tipo de símbolo, sea este un dígito, una letra, o cualquier otro que pueda aparecer".

#2)Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que comienzan con el primer caracter de
#todo el texto (en minúscula o mayúscula si es letra). Por ejemplo, en el texto: "El mar es solitario." hay 2 palabras en total que cumplen ("El" y "es")
#sobre un total de 4 palabras. Por lo tanto, el porcentaje pedido es del 50%. Por "caracteres",
#se entiende "cualquier tipo de símbolo, sea este un dígito, una letra, o cualquier otro que pueda aparecer"

#3)Determinar la cantidad de palabras que incluyeron dos letras ele ("l") (aunque no necesariamente seguidas) pero entre las cuatro primeras posiciones de la palabra.
# Por ejemplo, en el texto: "Allá en la altura la falta de aire te deja lelo.”, hay 2 palabras que cumplen: "Allá" y "lelo

#4)Determinar la cantidad de palabras que contienen la expresión "on" (con cualquiera de sus letras en minúscula o en mayúscula,
# acentuada o no) pero de forma que la palabra tenga además una "x" (minúscula o mayúscula). Por ejemplo, en el texto: "La canción es una conexión con el contexto.”,
# hay 2 palabras que cumplen la condición ("conexión" y "contexto")

#Funciones
#Funcion para vocales.
def es_vocal(letra):
    vocal = "aeiouáéíóú"
    return letra in vocal
#Funcion para calcular el porcentaje.
def porcentaje(cantidad, total):
    media = round((cantidad * 100) / total, 2)
    return media
#Funcion principal

def test():
    #Contadores y banderas.
    cont_let, cont_pal = 0, 0
    cant_vocales, puntoa = 0, 0
    cont_l, eles = 0, 0
    cont_band_x = 0
    cont_coincidencia = 0
    letra_uno = 0
    primer_caracter, primer_letra = None, None

    primer_vuelta = True
    coinciden = False
    ban_o, band_on, band_x = False, False, False
    #Input.
    texto = input("Ingresar texto: ").lower()
    #Ciclo for para iterar caracter por caracter.
    for letra in texto:
        #Espacios en blancos y fin del texto.
        if letra == " " or letra == ".":
            cont_pal += 1
            if cant_vocales <= 2:
                if cont_let >= 5:
                    puntoa += 1
            if cont_l == 2:
                eles += 1
            if band_x:
                cont_band_x += 1
            if coinciden:
                cont_coincidencia += 1
            #Reinicio de contadores y banderas.
            cont_let = 0
            cant_vocales = 0
            cont_l = 0
            ban_o, band_on, band_x = False, False, False
            coinciden = False
            letra_uno = 0

        #Dentro de la palabra
        else:
            cont_let += 1
            if es_vocal(letra):
                cant_vocales += 1
            if cont_let <= 4:
                if letra == "l":
                    cont_l +=1
            if letra == "o":
                ban_o = True
            else:
                if letra == "n" and ban_o:
                    band_on = True
                else:
                    if band_on and letra == "x":
                        band_x = True
                    else:
                        pass
            if primer_vuelta:
                primer_caracter = letra
                primer_vuelta = False
            else:
                if cont_let == 1:
                    letra_uno = letra
                    if letra_uno == primer_caracter:
                        coinciden = True

    #Funcion para el calculo del promedio
    prom = porcentaje(cont_coincidencia, cont_pal)
    #visualizacion de los resultados.
    print("Resultados:")
    print("." * 80)
    print("1) Cantidad de palabras con al menos una o dos vocales y mayor o igual a cinco caracteres:", puntoa)
    print(f"2) La primer palabra es: {primer_caracter}, coinciden: {cont_coincidencia} palabras, en el texto hay {cont_pal} palabras, por lo tanto equivale: {prom}%.")
    print("3) La cantidad de palabras con dos 'l' antes del cuarto caracter son:", eles)
    print("4) Cantidad de palabras que cuentan con la expresion 'on' y 'x':", cont_band_x)
    print("-" * 20)
    print("Fin.")

test()
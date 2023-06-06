# RETO 12

file = open('mbox-short.txt') # Extrae la información de un archivo de texto. 
texto = file.read()


# Punto 1

def contarVocales(*args): 

    a = (texto.count("a"))
    e = (texto.count("e"))
    i = (texto.count("i"))
    o = (texto.count("o"))
    u = (texto.count("u"))
    A = (texto.count("A"))
    E = (texto.count("E"))
    I = (texto.count("I"))
    O = (texto.count("O"))
    U = (texto.count("U"))

    totalVocales = a + e + i + o + u + A + E + I + O + U

    return (f"El total de vocales en el texto es: {totalVocales}")

# Punto 2

def contarConsonantes(*args): 
    B = (texto.count("B")) 
    C = (texto.count("C"))
    D = (texto.count("D"))
    F = (texto.count("F"))
    G = (texto.count("G"))
    H = (texto.count("H"))
    J = (texto.count("J"))
    K = (texto.count("K"))
    L = (texto.count("L"))
    M = (texto.count("M"))
    N = (texto.count("N"))
    Ñ = (texto.count("Ñ"))
    P = (texto.count("P"))
    Q = (texto.count("Q"))
    R = (texto.count("R"))
    S = (texto.count("S"))
    T = (texto.count("T"))
    V = (texto.count("V"))
    X = (texto.count("X"))
    Z = (texto.count("Z"))
    W = (texto.count("W"))
    Y = (texto.count("Y"))
    b = (texto.count("b")) 
    c = (texto.count("c"))
    d = (texto.count("d"))
    f = (texto.count("f"))
    g = (texto.count("g"))
    h = (texto.count("h"))
    j = (texto.count("j"))
    k = (texto.count("k"))
    l = (texto.count("l"))
    m = (texto.count("m"))
    n = (texto.count("n"))
    ñ = (texto.count("ñ"))
    p = (texto.count("p"))
    q = (texto.count("q"))
    r = (texto.count("r"))
    s = (texto.count("s"))
    t = (texto.count("t"))
    v = (texto.count("v"))
    x = (texto.count("x"))
    z = (texto.count("z"))
    w = (texto.count("w"))
    y = (texto.count("y"))
  
    totalConsonantes = B + C + D + F + G + H + J + K + L + M + N + Ñ + P + Q + R + S + T + V + X + Z + W + Y + b + c + d + f + g + h + j + k + l + m + n + ñ + p + q + r + s + t + v + x + z + w + y
    return(f"El total de consonantes en el texto es: {totalConsonantes}")


# Punto 3

def listarPalabras(*args): 
    listaConPalabras = texto.split()  # Va extraer cada palabra del texto que se encuentre antes de un espacio y la agrega a una lista.
    listaNueva = [] # Generamos diccionario vacio.
    lista = [] # Generamos lista vacia.

    for numeroPalabra in range(len(listaConPalabras)): # Itera correspondiendo al tipo
        if listaConPalabras[numeroPalabra].isalpha(): # Indica condición. Que los elementos de la lista correspondan a letras del alfabeto. 
            limpiarPalabra = listaConPalabras[numeroPalabra].strip(";.:-,()1234567890></")  # Va tomar dichas
            listaNueva.append(limpiarPalabra) # Agrega palabra a la lista. 

    

    diccionario = {}
    for palabra in listaNueva: 
        if palabra in diccionario: 
            diccionario[palabra] +=1
        else: 
            diccionario[palabra] = 1
    

    for i in range(len(diccionario)): 
        x = list(diccionario.items())[i][::-1]
        lista.append(x)

    return lista


if __name__ == "__main__": # Permite inicializar la función. 
    print(contarConsonantes(texto)) #Llama e imprime la función. 
    print(contarVocales(texto)) 
    print(listarPalabras(texto))  


file.close()
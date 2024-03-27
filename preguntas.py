"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
data = open("data.csv", "r").readlines()

data = [x.replace("\n", "") for x in data]
data = [x.replace("\t", ",") for x in data]
data =  [x.split(",") for x in data]



def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
   
    lista = list([x[1] for x in data])
    lista = sum([int(x) for x in lista])
    return lista



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista = list([x[0] for x in data])
    from collections import Counter
    lista = sorted(list(Counter(lista).items()))
    return lista


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    from collections import defaultdict

    lista = [(x[0], x[1]) for x in data]

    sumas = defaultdict(int)
    for letra, numero in lista:
        sumas[letra] += int(numero)


    tuplas_suma = sorted([(letra, suma) for letra, suma in sumas.items()])


    return(tuplas_suma)
        



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    list1 = [x[2].split("-") for x in data]
    from collections import Counter
    list2 = sorted(list(Counter([x[1] for x in list1]).items()))
    
    return list2


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    
    from collections import defaultdict

    lista = [(x[0], x[1]) for x in data]
    # Diccionario para almacenar los números mínimo y máximo por cada letra
    dictionary = defaultdict(lambda: [float('-inf'), float('inf')])

    # Calcular el número mínimo y máximo para cada letra
    for letra, numero in lista:
        num = int(numero)
        dictionary[letra][0] = max(dictionary[letra][0], num) # máximo
        dictionary[letra][1] = min(dictionary[letra][1], num) # mínimo


    tuplas_min_max = sorted([(letra, min_max[0], min_max[1]) for letra, min_max in dictionary.items()])
    return tuplas_min_max


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    columna5 = []

    # Iterar sobre cada lista y extraer los elementos que contienen ":"
    for sublista in data:
        for elemento in sublista:
            if ":" in elemento:
                columna5.append(elemento)

    componentes = {}


    for componente in columna5:
        letra, numero = componente.split(':')
        numero = int(numero)
        if letra not in componentes:
            componentes[letra] = [numero]
        else:
            componentes[letra].append(numero)

    # Calcular el mínimo y el máximo por cada clave
    resultados = sorted([(letra, min(numeros), max(numeros)) for letra, numeros in componentes.items()])

    return resultados



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    lista = [(x[0], x[1]) for x in data]
    dictionary = {}

    for letra, numero in lista:
        if numero not in dictionary:
            dictionary[numero] = [letra]
        else:
            dictionary[numero].append(letra)
    
    
    resultado = sorted([(int(numero), letras) for numero, letras in dictionary.items()])

    return resultado
  


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista = [(x[0], x[1]) for x in data]
    dictionary = {}

    for letra, numero in lista:
        if numero not in dictionary:
            dictionary[numero] = [letra]
        else:
            dictionary[numero].append(letra)
    
    for numero, letras in dictionary.items():
        newlist = sorted(set(letras))
        dictionary[numero] = newlist

    resultado = sorted([(int(numero), letras) for numero, letras in dictionary.items()])

    return resultado
    


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from collections import Counter

    columna5 = []
    for sublista in data:
        for elemento in sublista:
            if ":" in elemento:
                columna5.append(elemento)

     
    claves = sorted([componente.split(':')[0] for componente in columna5])
    conteo_claves = Counter(claves)

    diccionario_conteo = dict(conteo_claves)

    return diccionario_conteo
   
data2 = open("data.csv", "r").readlines()
data2 = [x.replace("\n", "") for x in data2]
data2= [x.split("\t") for x in data2]

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    resultado = [(x[0], len(x[3].split(",")), len(x[4].split(","))) for x in data2]
    return resultado

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    from collections import Counter

    lista = [(x[1], x[3].split(",")) for x in data2]
    l=[]
    for tupla in lista:
        for letra in tupla[1]:
            l.append((letra, int(tupla[0])))


    resultado = {}

    for key, value in sorted(l):
        if key in resultado:
            resultado[key] += value
        else:
            resultado[key] = value
    
    return resultado


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    lista= [(x[0], x[4].split(",")) for x in data2]
    l=[]

    for elemento in lista:
        for letra in elemento[1]:
            _, numero = letra.split(':')
            l.append((elemento[0], int(numero)))

    resultado = {}

    for key, value in sorted(l):
        if key in resultado:
            resultado[key] += value
        else:
            resultado[key] = value
    
    return resultado
    


    

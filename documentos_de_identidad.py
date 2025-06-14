from collections import Counter

def definir_conjuntos(d, c):

    for i in d:
        c.append(set(i))

def union(c, nc):

    for i in range(len(c)):
        for j in range(i+1, len(c)):
            res = c[i].union(c[j])
            print(f"{nc[i]} ∪ {nc[j]}: {res}")

def interseccion(c, nc):

    for i in range(len(c)):
        for j in range(i+1, len(c)):
            res = c[i].intersection(c[j])
            print(f"{nc[i]} ∩ {nc[j]}: {res}")

def diferenciacion_simetrica(c, nc):

    for i in range(len(c)):
        for j in range(i+1, len(c)):
            res = c[i].symmetric_difference(c[j])
            print(f"{nc[i]} △ {nc[j]}: {res}")

def frecuencia(d, freq):

    contadores = []

    for dni in d:
        contadores.append(Counter(dni))

    for i in range(len(contadores)):
        freq += contadores[i]

    print(freq)

def suma_digitos(d):

    acum = []

    for dni in d:
        aux = 0
        for digito in dni:
            aux += int(digito)
        acum.append(aux)
    print(acum)

def diversidad_numerica(c):

    for conjunto in c:
        if len(conjunto) > 6:
            print(f"El conjunto {conjunto} presenta mas de 6 digitos diferentes!")

def conjuntos_sin_cero(c):

    band = False

    for conjunto in c:
        for elemento in conjunto:
            if elemento == '0':
                band = True
                break
        if not band:
            print(f"{conjunto}, es un conjunto sin ceros!")
        
if __name__ == '__main__':

    documentos = ["44527599", "37802919", "29823434", "17529275"]

    conjuntos = []
    nombre_conjuntos = ["A", "B", "C", "D"]

    definir_conjuntos(documentos, conjuntos)
    conjuntos_sin_cero(conjuntos)
    
    '''
    union(conjuntos, nombre_conjuntos)
    interseccion(conjuntos, nombre_conjuntos)
    diferenciacion_simetrica(conjuntos, nombre_conjuntos)

    freq = Counter()

    frecuencia(documentos, freq)

    suma_digitos(documentos)
    diversidad_numerica(conjuntos)
    conjuntos_sin_cero(conjuntos)
    '''
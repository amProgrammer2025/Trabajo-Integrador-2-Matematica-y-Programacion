
import datetime

def edades_actuales(anios):

        edades_act = []

        fecha_actual = datetime.date.today()
        anio_actual = fecha_actual.year

        for a in anios:
            edad = anio_actual - a
            edades_act.append(edad)

        return edades_act

def producto_cartesiano(anios, edades_act):

    C = set()

    for a in anios:
        for e in edades_act:
            C.add((a, e))

    print(C)

def anio_bisiesto(anios):

    for a in anios:

        if a % 4 == 0:
            if a % 100 == 0:
                if a % 400 == 0:
                    print(f"El integrante nacido en {a}, nacio en un año bisiesto!")
            else:
                print(f"El integrante nacido en {a}, nacio en un año bisiesto!")


def grupo_z(anios):

    band = True
    cont = 0

    while band and cont < len(anios):

        if anios[cont] <= 2000:
            band = False

        cont += 1

    if band:
        print(f"{anios} = Grupo Z")

def anios_pares_impares(anios):

    sum_pares = 0
    sum_impares = 0

    for a in anios:
        if (a % 2) == 0:
            sum_pares += 1
        else:
            sum_impares += 1

    print(f"Cantidad de integrantes nacidos en años pares: {sum_pares}")
    print(f"Cantidad de integrantes nacidos en años impares: {sum_impares}")

if __name__ == '__main__':

    anios_de_nac = [1999, 2004, 2003, 2008]
    edades = edades_actuales(anios_de_nac)

    producto_cartesiano(anios_de_nac, edades)
    


    '''
    anio_bisiesto(anios_de_nac)
    grupo_z(anios_de_nac)
    anios_pares_impares(anios_de_nac)
    producto_cartesiano(anios_de_nac, edades)
    '''
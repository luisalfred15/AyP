import random

def comprobar_str(msg):
    string = input(msg)
    if string.replace(' ', '').isalpha():
        return string
    else:    
        return comprobar_str('Error, ingrese palabras validas: ')

def comprobar_opcion(msg, cantidad_opciones):
    opcion = input(msg)
    if opcion.isnumeric() and int(opcion) in range(1, cantidad_opciones + 1):
        return opcion
    else:
        return comprobar_opcion('Error, seleccione una opcion que este dentro del rango: ', cantidad_opciones)

def comprobar_num(msg):
    num = input(msg)
    if num.isnumeric() and 0 < int(num):
        return num
    else:
        return comprobar_num('Error, ingrese un numero valido: ')

def comprobar_fecha(msg):
    fecha = input(msg)
    if fecha.replace('/', '').isnumeric():
        return fecha
    else:
        return comprobar_fecha('Error, ingrese una fecha valida: ')

def victoria_plancha(carnet):
    num_votantes = int(carnet[-4] + carnet[-3] + carnet[-2] + carnet[-1])
    num_random = random.randint(0, 100)
    porcentaje = num_random / 100
    votos_v = int(num_votantes * porcentaje)
    votos_j = int(num_votantes * (1 - porcentaje))
    if votos_v > votos_j:
        ganador = 'Victor'
    else:
        ganador = 'Joel'
    return votos_v, votos_j, ganador

def imprimir_victoria(votos_v, votos_j, ganador):
    resultados = f'''*** RESULTADOS ***
        GANADOR: Plancha {ganador}
        VOTOS:
            Plancha Victor: {votos_v}
            Plancha Joel: {votos_j}'''
    print(resultados)
    return resultados

def generar_bd_planchas():
    planchas = []
    archivo_1 = open('planchas.txt')
    lineas_1 = archivo_1.readlines()
    for linea_1 in lineas_1:
        plancha = linea_1.split('//')
        plancha[-1] = plancha[-1].replace('\n', '')
        dict_plancha = {
            'nombre': plancha[0],
            'numero': plancha[1]
        }
        planchas.append(dict_plancha)

    return planchas

def generar_bd_jds():
    jds = []
    archivo_2 = open('jds.txt')
    lineas_2 = archivo_2.readlines()
    for linea_2 in lineas_2:
        jd = linea_2.split('//')
        jd[-1] = jd[-1].replace('\n','')
        if jd[0] == 'G':
            dict_jd = {
                "tipo": jd[0],
                "plancha": jd[1],
                "presidente": jd[2],
                "coordinador general": jd[3],
                "tesorero": jd[4],
                "sg": jd[5],
                "sai": jd[6]
            }
        elif jd[0] == 'E':    
            dict_jd = {
                "tipo": jd[0],
                "plancha": jd[1],
                "escuela": jd[2],
                "presidente": jd[3],
                "coordinador general": jd[4],
                "tesorero": jd[5],
            }

        jds.append(dict_jd)

    return jds

def guardar_resultados(resultados):
    archivo_res = open('resultados.txt', 'w')
    archivo_res.write(resultados)
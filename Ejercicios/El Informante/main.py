from Redactor_ import Redactor
from JefeRedactor_ import JefeRedactor
from Seccion_ import Seccion
from Articulo_ import Articulo
from Anuncio_ import Anuncio
from AnuncioComercial_ import AnuncioComercial
from AnuncioClasificado_ import AnuncioClasificado
from AnuncioClasificadoCarro_ import AnuncioClasificadoCarro
from AnuncioClasificadoVivienda_ import AnuncioClasificadoVivienda
from funciones import *

def main():
    print('Bienvenido a El Informante!')
    redactores = []
    secciones = {}
    articulos = []
    anuncios_comerciales = []
    anuncios_viviendas = []
    anuncios_carros = []
    while True:
        opcion = comprobar_opcion('''Seleccione la opción deseada:
        1. Añadir una sección
        2. Añadir un artículo
        3. Añadir un anuncio
        4. Salir del sistema
        -> ''', 4)

        if opcion == '1':
            seccion = 1
            agregar_redactor = '1'
            opcion_seccion = '1'
            
            
            while opcion_seccion == '1':
                nombre_jefe = comprobar_str('Ingrese el nombre del jefe redactor: ')
                cedula_jefe = comprobar_num('Ingrese la cédula del jefe redactor: ')

                nuevo_jefe = JefeRedactor(nombre_jefe, cedula_jefe, seccion)
                
                while agregar_redactor == '1':
                    nombre_redactor = comprobar_str('Ingrese el nombre del redactor: ')
                    cedula_redactor = comprobar_num('Ingrese la cédula del redactor: ')

                    nuevo_redactor = Redactor(nombre_redactor, cedula_redactor, seccion)

                    redactores.append(nuevo_redactor)

                    agregar_redactor = comprobar_opcion('''Desea agregar otro redactor?
                    1. Si
                    2. No
                    -> ''', 2)

                nueva_seccion = Seccion(nuevo_jefe, redactores)

                secciones[seccion] = nueva_seccion

                seccion += 1

                opcion_seccion = comprobar_opcion('''Desea agregar otra seccion?
                1. Si
                2. No
                -> ''', 2)

                print('Seccion creada con exito')

        elif opcion == '2':
            opcion_articulo = '1'
            
            while opcion_articulo == '1':
                titulo = comprobar_str('Ingrese el titulo del articulo: ')
                resumen = comprobar_str('Ingrese el resumen del articulo: ')
                cuerpo = comprobar_str('Ingrese el cuerpo del articulo: ')
                imagenes = comprobar_num('Ingrese la cantidad de imagenes del articulo: ')
                fecha_publicacion = comprobar_fecha('Ingrese la fecha de publicacion del articulo: ')
                fecha_creacion = comprobar_fecha('Ingrese la fecha de creacion del articulo: ')

                print('*** REDACTORES ***')
                for key in redactores:
                    print(f'--- {redactores.index(key) + 1} ---')
                    key.imprimir_redactor(key)
                
                redactor = comprobar_opcion('Seleccione el redactor que escribio el articulo: ', len(redactores))

                nuevo_articulo = Articulo(titulo, resumen, cuerpo, imagenes, fecha_publicacion, fecha_creacion, redactor)

                articulos.append(nuevo_articulo)
                
                print('Articulo creado con exito')

                opcion_articulo = comprobar_opcion('''Desea agregar otro articulo?
                1. Si
                2. No
                -> ''', 2)
        
        elif opcion == '3':
            
            
            nombre_vendedor = comprobar_str('Ingrese el nombre del vendedor: ')
            cedula_vendedor = comprobar_num('Ingrese la cedula del vendedor: ')
            seccion_anuncio = comprobar_str('Ingrese la seccion donde estara el anuncio: ')
            titulo_anuncio = comprobar_str('Ingrese el titulo del anuncio: ')
            cuerpo_anuncio = comprobar_str('Ingrese el cuerpo del anuncio: ')
            tipo_anuncio = comprobar_opcion('''Seleccione el tipo de anuncio que desea agregar:
            1. Comercial
            2. Clasificado
            -> ''', 2)

            if tipo_anuncio == '1':
                nuevo_anuncio_comercial = AnuncioComercial(nombre_vendedor, cedula_vendedor, seccion_anuncio, titulo_anuncio, cuerpo_anuncio)
                anuncios_comerciales.append(nuevo_anuncio_comercial)
            else:
                precio = comprobar_num('Ingrese el precio del anuncio: ')
                fecha = comprobar_fecha('Ingrese la fecha de publicacion del anuncio: ')
                tiempo = comprobar_num('Ingrese el tiempo en que estara disponible el anuncio: ')
                tipo = comprobar_opcion('''Seleccione el tipo de anuncio:
                1. Vivienda
                2. Carro
                -> ''', 2)
                if tipo == '1':
                    
                    m2 = comprobar_num('Ingrese la cantidad de metros cuadrados: ')
                    cuartos = comprobar_num('Ingrese la cantidad de cuartos de la vivienda: ')
                    baños = comprobar_num('Ingrese la cantidad de baños de la vivienda: ')
                    puestos_estaciona = comprobar_num('Ingrese la cantidad de puestos de estacionamiento de la vivienda: ')
                    politica_hab = comprobar_opcion('''Cuenta con politica habitacional?
                    1. Si
                    2. No
                    -> ''', 2)
                    nuevo_anuncio_vivienda = AnuncioClasificadoVivienda(nombre_vendedor, cedula_vendedor, seccion_anuncio, titulo_anuncio, cuerpo_anuncio, precio, fecha, tiempo, 'Vivienda', m2, cuartos, baños, puestos_estaciona, politica_hab)
                    anuncios_viviendas.append(nuevo_anuncio_vivienda)

                    print('Anuncio de vivienda agregado con exito')

                else:
                    marca = comprobar_str('Ingrese la marca del carro: ')
                    modelo = comprobar_str('Ingrese el modelo del carro: ')
                    año = comprobar_num('Ingrese el año del carro: ')
                    color = comprobar_str('Ingrese el color del carro: ')
                    kms = comprobar_num('Ingrese el kilometraje del carro: ')

                    nuevo_anuncio_carro = AnuncioClasificadoCarro(nombre_vendedor, cedula_vendedor, seccion_anuncio, titulo_anuncio, cuerpo_anuncio, precio, fecha, tiempo, 'Carro', marca, modelo, año, color, kms)
                    anuncios_carros.append(nuevo_anuncio_carro)

                    print('Anuncio de carro agregado con exito')

        elif opcion == '4':
            break

main()
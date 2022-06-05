pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300     
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800     
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350     
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }
    ],   
}
pacientes = {}
numero_paciente = 0

print('Bienvenio a la clinica!')

while True:
	opcion = input('''Seleccione la opcion:
		1. Registrar y cobrar
		2. Ver pacientes
		3. Salir del programa
		->''')

	if opcion.isnumeric() and 1 <= int(opcion) <= 3:
		if opcion == '1':    
			numero_paciente += 1
			nombre = input('Ingrese su nombre: ')
			apellido = input('Ingrese su apellido: ')
			cedula = input('Ingrese su cedula: ')
			for key, value in pathologies.items(): # Usar siempre este tipo de for con diccionarios
				for enfermedades in value:
					print(enfermedades["id"], enfermedades["name"])
			id_seleccionado = input('Ingrese el id de la enfermedad que padece: ')
			for key_2, value_2 in pathologies.items():
				for dict in value_2:
					if dict['id'] == int(id_seleccionado):
						nombre_enfermedad = dict['name']
						precio_enfermedad = dict['price']
						break
				if dict['id'] == int(id_seleccionado):
					break
			pacientes[int(numero_paciente)] = {
				'nombre': nombre,
				'apellido': apellido,
				'cedula': cedula,
				'id_enfermedad': id_seleccionado,
				'nombre_enfermedad': nombre_enfermedad
			}
			print(f'''                  *** FACTURA ***
				Nombre del paciente: {nombre}
				Apellido del paciente: {apellido}
				Cedula del paciente: {cedula}
				Patologia que padece: {nombre_enfermedad}
				Monto a pagar: {precio_enfermedad}''')
		elif opcion == '2':
			for key_3, value_3 in pathologies.items(): # Usar siempre este tipo de for con diccionarios
				for dict_2 in value_3:
					print(dict_2["id"], dict_2["name"])
			busqueda_enfermedad = input('Que base de datos de enfermedad desea ver? \n ->')
			for key_4, value_4 in pacientes.items():
				if int(value_4['id_enfermedad']) == int(busqueda_enfermedad):
					print(f'''
				Nombre del paciente: {value_4['nombre']}
				Apellido del paciente: {value_4['apellido']}
				Cedula del paciente: {value_4['cedula']}''')
		else:
			break
	else:
		print('Por favor, introduzca un valor valido')
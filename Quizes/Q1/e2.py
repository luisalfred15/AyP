infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}

db={}
infringer_counter = 1

print('Welcome to the Infractions Database!')

while True:
    is_palindromic = True
    i = 0
    
    option = input('''Please, enter one of the options:
                        1: Add an infringer to the database
                        2: Delete an infringer from the database
                        3: Show all the registered infractions by infringer
                        4: Show all the registered infractions by officer
                        5: Close the database
                        -> ''')
    
    if option == '1':
        name = input('Please, enter the name of the infringer: ')
        last_name = input('Please, enter the last name of the infringer: ')
        dni = input('Please, enter the DNI of the infringer: ')
        
        print('             *** INFRACTIONS LIST ***')
        for key, value in infraction.items():
            print(f'''                          ID {key}: {value.get('name')}
                            Cost: {value.get('cost')}''')
        type_infraction = int(input('Please, enter the infraction ID committed by the infringer: '))
        
        numbers = [dni[-3], dni[-2], dni[-1]]
        list = ''.join(numbers)
        while i <= len(list) // 2:
            data_1 = list[-len(list)+i]
            data_2 = list[len(list)-i-1]
            if data_1 != data_2:
                is_palindromic = False
            i += 1
        if is_palindromic:
            infraction_cost = 0
        else:
            infraction_cost = infraction[type_infraction]['cost']

        print('                 *** OFFICERS LIST ***')
        for key_2, value_2 in officers.items():
                print(f'''                          ID {key_2}: {value_2.get('name')} {value_2.get('lastName')}
                                DNI: {value_2.get('ci')}''')
        officer_id = int(input('Please, enter the ID of the officer: '))
        
        db[infringer_counter] = {
            'name': name,
            'last_name': last_name,
            'dni': dni,
            'type_infraction': type_infraction,
            'officer_id': officer_id,
            'infraction_cost': infraction_cost
        }
        
        infringer_counter += 1

    elif option == '2':
        while True:    
            print('                 *** INFRINGERS DATABASE ***')
            for key_3, value_3 in db.items():
                print(f'''                              ID {key_3}: {value_3.get('name')} {value_3.get('last_name')}
                                    DNI: {value_3.get('dni')}
                                    Type of infraction: {value_3.get('type_infraction')}
                                    Officer ID: {value_3.get('officer_id')}
                                    Infraction cost: {value_3.get('infraction_cost')}''')
            infraction_pop = int(input('Please, enter the infraction you want to delete: '))
            money = int(input('Please, pay the bill of the infraction in order to delete it from the database: '))

            if money == db[infraction_pop]['infraction_cost']:
                db.pop(infraction_pop)
                break
            else:
                print('There is not enough money to delete the infraction')

    elif option == '3':
        print('                 *** INFRINGERS DATABASE ***')
        for key_4, value_4 in db.items():
            print(f'''                              ID {key_4}: {value_4.get('name')} {value_4.get('last_name')}
                                DNI: {value_4.get('dni')}
                                Type of infraction: {value_4.get('type_infraction')}
                                Officer ID: {value_4.get('officer_id')}
                                Infraction cost: {value_4.get('infraction_cost')}''')
    
    elif option == '4':
        print('*** OFFICERS LIST ***')
        for key_5, value_5 in officers.items():
                print(f'''                          ID {key_5}: {value_5.get('name')} {value_5.get('lastName')}
                                DNI: {value_5.get('ci')}''')
        officer_id = int(input('Please, enter the ID of the officer to see the infractions by officer: '))
        print('                     *** INFRINGERS DATABASE ***')
        for key_6, value_6 in db.items():
            if officer_id == db[key_6]['officer_id']:
                print(f'''                              ID {key_6}: {value_6.get('name')} {value_6.get('last_name')}
                                    DNI: {value_6.get('dni')}
                                    Type of infraction: {value_6.get('type_infraction')}
                                    Officer ID: {value_6.get('officer_id')}
                                    Infraction cost: {value_6.get('infraction_cost')}''')
    
    if option == '5':
        break

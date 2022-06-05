from account import Account

name = input('Por favor, introduzca su nombre: ')
dni = input('Por favor, introduzca su cedula: ')
username = input('Por favor, introduzca su nombre de usuario: ')
password = input('Por favor, introduzca su contrasena: ')
answer_1 = input('Por favor, introduzca el segundo nombre de su mama: ')
answer_2 = input('Por favor, introduzca donde nacio su mama: ')


account_1 = Account(name, dni, username, password, answer_1, answer_2)

print(account_1.get_password())


def comprobar_str(msg):
    string = input(msg)
    if string.replace(' ', '').isalpha():
        return string
    else:
        return comprobar_str(msg)

def comprobar_opcion(msg, cantidad_opciones):
    num = input(msg)
    if num.isnumeric() and 0 < int(num) <= cantidad_opciones:
        return num
    else:
        return comprobar_opcion(msg, cantidad_opciones)

def comprobar_num(msg):
    num = input(msg)
    if num.isnumeric() and 0 < int(num):
        return num
    else:
        return comprobar_num(msg)
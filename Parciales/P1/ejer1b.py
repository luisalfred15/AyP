def calcular_mayor_riqueza():
    cuentas = [[1,2,3,4],[4,5,6,7]]
    mayor_riqueza = 0
    for cliente in cuentas:
        riqueza = 0
        for banco in cliente:
            riqueza += banco
    if riqueza > mayor_riqueza:
        mayor_riqueza = riqueza
    return mayor_riqueza

print(calcular_mayor_riqueza())
from vehicle import Vehicle

def main():
    print('WELCOME')
    car = Vehicle('Toyota', 'Camry', 'Azul', '2020')
    car.set_brand('Hyundai')
    print(car)

main()
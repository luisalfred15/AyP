from evento import Event
from carreras import Race
from caballo import Horse

def main():
    horse_1 = Horse('Rayo','Antonio')
    horse_2 = Horse('Centella','Jesus')
    horse_3 = Horse('Bolido','Luis')
    horse_4 = Horse('A','Isa')
    horse_5 = Horse('B','Camila')
    horse_6 = Horse('C','Andres')
    horse_list = [horse_1, horse_2, horse_3, horse_4, horse_5, horse_6]

    race = Race(horse_list, 1)

    race.start()
    print(f'The horse winner is {race.winner()}')



main()
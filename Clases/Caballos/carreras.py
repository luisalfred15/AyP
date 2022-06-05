import random
from caballo import Horse

class Race:
    def __init__(self, horses, number):
        self.horses = list(horses)
        self.number = number
    
    def start(self):
        print('SALIDAAAAAA')
    
    def winner(self):
        winner = random.randint(0, 5)
        print(f'Y el ganador es {self.horses[winner]} con el jinete {self.joker[winner]}')
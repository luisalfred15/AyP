class Office:
    def __init__(self, adress):
        self.__adress = adress
    
    def getAdress(self):
        return self.__adress
    
    def setAdress(self, adress):
        self.__adress = adress
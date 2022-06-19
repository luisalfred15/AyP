class Employee:
    def __init__(self, name, title):
        self.__name = name
        self.__title = title

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title
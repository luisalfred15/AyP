class Account():
    def __init__(self, full_name, dni, username, password, answer_1, answer_2):
        self.__full_name = full_name
        self.__dni = dni
        self.__username = username
        self.__password = password
        self.answer_1 = answer_1
        self.answer_2 = answer_2
    
    def get_full_name(self):
        return self.__full_name
    
    def get_password(self):
        user_answer_1 = input('Por favor, ingrese el segundo nombre de su mama: ')
        user_answer_2 = input('Por favor, ingrese donde nacio su mama: ')
        if user_answer_1 == self.answer_1 and user_answer_2 == self.answer_2:
            return self.__password
        else:
            return 'USUARIO NO AUTORIZADO'
    
    def set_password(self):
        return 
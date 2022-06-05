class Vehicle:
    def __init__(self, brand_parameter, model_parameter, color_paramater, year_parameter):
        self.__brand = brand_parameter
        self.__model = model_parameter
        self.__color = color_paramater
        self.__year = year_parameter

    def get_brand(self):
        return self.__brand
    
    def set_brand(self, new_brand):
        self.__brand =  new_brand
    
    
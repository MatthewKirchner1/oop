class Car:
    def __init__(self):
        self.__make = input("Enter car make: ")
        self.__model = input("Enter car model: ")
        self.__year = input("Enter car model year: ")

    def set_make(new_make):
        self.__make = new_make

    def set_model(new_model):
        self.__model = new_model

    def set_year(new_year):
        self.__year = new_year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

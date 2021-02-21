class Car:
    def __init__(self):
        self.__year_model = input("Car model:")
        self.__make = input("Car make:")
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

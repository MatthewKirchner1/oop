class Customer:
    def __init__(self):
        self.__name = input("Enter customer name: ")
        self.__addres = input("Enter customer address: ")
        self.__phone = input("Enter customer phone number: ")

    def set_name(new_name):
        self.__name = new_name

    def set_address(new_address):
        self.__address = new_address

    def set_phone(new_phone):
        self.__phone = new_phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

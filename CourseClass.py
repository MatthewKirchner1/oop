class Course:
    def __init__(self):
        self.__title = "default title"
        self.__CRN = 00000
        self.__capacity = 00000
        self.__code = "00000"

    def assign_title(given_title):
        self.__title = given_title

    def assign_CRN(given_CRN):
        self.__CRN = given_CRN

    def assign_capacity(given_capacity):
        self.__capacity = given_capacity

    def assign_code(given_code):
        self.__code = given_code

    def get_CRN():
        return self.__CRN

    def get_capacity():
        return self.__capacity

from datetime import date


class Student:

    def __init__(self, id, name, dob, classification):
        self.__studentID = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__registration = ""

    def age(self):
        today = date.today()
        # This will give me a date time format
        today_year = today.year

        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        self.__age = today_year - dob_year
        # DDBMonth = dob[0]

    def calc_registration(self):
        if self.__classification == "senior":
            self.__registration = '4/1 thru 4/3'
        elif self.__classification == "junior":
            self.__registration = '4/4 thru 4/6'
        elif self.__classification == "sophomore":
            self.__registration = '4/7 thru 4/9'
        elif self.__classification == "freshmen":
            self.__registration = '4/10 thru 4/12'
        else:
            self.__registration = 'Classification not found'

    def get_age(self):
        return self.__age

    def get_register(self):
        return self.__registration

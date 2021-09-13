class Person:
    '''Human class'''
    total_persons = 0
    __birth_year = 2000  # maybe input?
    __current_year = 2021
    __name = "Bek"
    __language = "spanish"

    def __init(self, name, birth_year, **kwargs):
        self.name = name
        self.birth_year = birth_year
        # self.__current_year = kwargs
        self.__language = kwargs

        #self.__total_persons += 1
        if self.birth_year >= self.__current_year:
            raise TypeError("Bigger than current year!")

    def is_adult(self):
        if self.__current_year - self.birth_year >= 18:
            print(True)
        else:
            print(False)

    def get_age(self):
        print(self.__current_year - self.birth_year)  # Person's age

    @classmethod
    def get_total_persons(cls):  # общее число созданных Человеков
        pass

    def talk(self):
        print("Hello World")


class Teacher(Person):

    def new_talk(self, ntalk):  # Переопределние метода talk
        self.talk = ntalk
        print("Greetings, I'm your teacher")

    def tech(self):
        print("Lesson started by Teacher")


person1 = Person('My', 2004)
person2 = Person('Rys', 1999)
person3 = Person('Bek', 1990)

print(person2.name)
print(person2.is_adult())
print(person2.get_age())



teacher1 = Teacher('Aman', 2001)
teacher2 = Teacher('Daniiar', 2000)
teacher3 = Teacher('Abil', 1998)

print(teacher1.name)
print(teacher1.is_adult())
print(teacher1.get_age())
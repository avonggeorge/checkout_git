#!/usr/bin/python3

class Person:
    def __init__(self, name, sex, profession):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        # Behaviour (instance methods)
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)


    def work(self):
        print(self.name, 'working as a', self.profession)


# create object of a class
jessa = Person('Jessa', 'Female', 'Software Engineer')

# call methods
jessa.show()
jessa.work()

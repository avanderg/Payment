from Person import *


class PersonStorage:
    def __init__(self, total):
        self.people = {}
        self.defaultFlag = False
        self.total = total

    def addPerson(self, person):
        self.people[person] = Person(person)

    def getPerson(self, person):
        return self.people[person]

    def default(self):
        """ Default People, if you want to change the default, just change the names. Can add and delete so you can
        have a different total amount by default."""

        self.addPerson('Aaron')
        self.addPerson('Abbey')
        self.addPerson('Chase')
        self.addPerson('Keith')

    def printDefault(self):
        self.default()
        for person, items in self.people.items():
            print(person)
        self.people = {}

    def parser(self, string, fun):
        string = string.split()
        for person in string:
            fun(person)

    def makePeople(self):
        people = input('Input the people. Just press enter for default; press d to display the default. ')

        if people == '':
            self.defaultFlag = True
            return self.default()
        elif people == 'd':
            self.printDefault()
            self.makePeople()
        else:
            self.parser(people, self.addPerson)

    def getDues(self):
        pass

    def printResult(self):
        for person in self.people:
            print(self.people[person].name + ' owes ' + str(self.people[person].owe))

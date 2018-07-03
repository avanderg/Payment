from PersonStorage import PersonStorage


class GroceryCustomerStorage(PersonStorage):
    def __init__(self, total):
        PersonStorage.__init__(self, total)
        self.exempt = []

    def addExempt(self, person):
        self.exempt.append(person)

    def defaultExempt(self):
        """ If you have someone that usually doesn't contribute to the total bill, add them here. Make sure they are
        in the default people."""

        self.addExempt(self.getPerson('Chase').name)

    def exemptFromTotal(self):

        exemptInput = input(
            "Input the people who don't contribute to the whole bill (eg Chase). Press enter for default; "
            "press d to display the ... default ")
        if (exemptInput == '') and (self.defaultFlag is True):
            self.defaultExempt()
        elif exemptInput == 'd':
            print('Chase')
            self.exemptFromTotal()
        elif exemptInput == '':
            pass
        else:
            self.parser(exemptInput, self.addExempt)

    def getDues(self):
        for person in self.people:
            self.people[person].createItems()
            self.total -= self.people[person].owe

    def getTotalDues(self):
        for person in self.people:
            if not (person in self.exempt):
                self.people[person].owe += self.total / (len(self.people) - len(self.exempt))

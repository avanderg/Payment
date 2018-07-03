from PersonStorage import PersonStorage


class RestaurantCustomerStorage(PersonStorage):
    def __init__(self, total):
        PersonStorage.__init__(self, total)
        self.tip = 0.2
        self.tax = 0.0775
        self.testTotal = 0

    def setTax(self, tax):
        self.tax = tax

    def setTip(self, tip):
        self.tip = tip

    def getTotal(self, owe):
        return owe + owe * self.tax + owe * self.tip

    def queryTipTax(self):
        answer = input('If you would like to change the tip or tax, input the values. Type tip to change tip and tax to'
                       ' change tax. Press d to display the default. ')

        if answer == '':
            pass
        elif answer == 'd':
            print('Tip: ', self.tip, ' & Tax: ', self.tax)
            self.queryTipTax()
        elif answer == 'tip':
            answer2 = input('Enter the tip percentage as a decimal. ')
            self.setTip(float(answer2))
            self.queryTipTax()
        elif answer == 'tax':
            answer2 = input('Enter the tax percentage as a decimal. ')
            self.setTax(float(answer2))
            self.queryTipTax()

    def getDues(self):
        for person in self.people:
            self.people[person].createItems()
            self.people[person].owe = self.getTotal(self.people[person].owe)
            self.testTotal += self.people[person].owe

    def checkTotal(self):
        print('Total: ', self.testTotal)
    
    def totalTip(self):
        print('Total tip : ', self.testTotal - self.total)



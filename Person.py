class Person:
    def __init__(self, name):
        self.name = name
        self.owe = 0

    def createItems(self):
        myItems = input('Input price of ' + self.name + '\'s things: ')
        myItems = myItems.split()
        myItems = [float(i) for i in myItems]
        self.owe = sum(myItems)

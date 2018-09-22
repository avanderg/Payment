class Person:
    def __init__(self, name):
        self.name = name
        self.owe = 0

    def createItems(self):
        myItems = input('Input price of ' + self.name + '\'s things: ')
        myItems = myItems.split()
        myItems = self.parse(myItems)
        self.owe = sum(myItems)

    def parse(self, myItems):
        parsedList = []
        for item in myItems:
            try:
                thisItem = float(item)
                parsedList.append(thisItem)
            except ValueError:
                num, denom = item.split('/')
                parsedList.append(float(num)/float(denom))
        return parsedList
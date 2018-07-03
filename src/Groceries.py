from GroceryCustomers import GroceryCustomerStorage


def run(People):
    People.makePeople()
    People.exemptFromTotal()
    People.getDues()
    People.getTotalDues()
    People.printResult()


def main():
    total = float(input('Input the total bill '))
    People = GroceryCustomerStorage(total)
    run(People)


if __name__ == '__main__':
    main()
    input()

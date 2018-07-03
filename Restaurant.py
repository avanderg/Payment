from RestaurantCustomers import RestaurantCustomerStorage


def run(People):
    People.queryTipTax()
    People.makePeople()
    People.getDues()
    People.printResult()
    # print(type(People))
    People.checkTotal()


def main():
    total = float(input('Input the total bill '))
    People = RestaurantCustomerStorage(total)
    run(People)


if __name__ == '__main__':
    main()
    input()
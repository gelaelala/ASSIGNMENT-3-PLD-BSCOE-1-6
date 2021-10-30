def money ():
    money_ = int(input('Enter the amount of money: '))
    return money_

def price_apple ():
    price = int(input('Enter the price of the apple: '))
    return price

def applesyoucanbuy (_money, _price):
    numberofapples = int(Money/Price)
    return numberofapples

def total (_applesyoucanbuy, _price):
    total_ = int(Apples*Price)
    return total_

def change (_money, _total):
    change_ = int(Money-Total)
    return change_

def display (_apples, _change):
    print (f'You can buy {_apples} apples and your change is {_change} pesos.')

Money = money ()
Price = price_apple ()
Apples = applesyoucanbuy (Money, Price)
Total = total (Apples, Price)
Change = change (Money, Total)
display (Apples, Change)
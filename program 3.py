def money_ ():
    money = int(input('Enter the amount of money: '))
    return money

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

Money = money_ ()
Price = price_apple ()
Apples = applesyoucanbuy ()
Total = total (Apples, Price)
Change = change (Money, Total)
display (Apples, Change)
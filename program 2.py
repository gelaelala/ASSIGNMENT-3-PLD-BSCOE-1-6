def amntofapples ():
    Apples = int(input("Enter the amount of apples: "))
    return Apples

def amntoforanges ():
    Oranges = int(input("Enter the amount of oranges: "))
    return Oranges

def totalapples (_apple):
    total_apples = int(apples*20)
    return total_apples

def totaloranges (_orange):
    total_oranges = int(oranges*25)
    return total_oranges

def total (Totalapples, Totaloranges):
    Total_amount = int(applestotal+orangestotal)
    return Total_amount

def display (amount):
    print (f'The total amount is {amount}.') 

apples = amntofapples ()
oranges = amntoforanges ()
applestotal = totalapples
orangestotal = totaloranges
Total = total
display (Total)
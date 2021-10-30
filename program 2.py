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
    Total_amount = int(apples_total+oranges_total)
    return Total_amount

def display (total_):
    print (f'The total amount is {total_}.')

apples = amntofapples ()
oranges = amntoforanges ()
apples_total = totalapples (apples)
oranges_total = totaloranges (oranges)
Total = total (apples_total, oranges_total)
display (Total)
def amntofapples ():
    Apples = int(input("Enter the amount of apples: "))
    return Apples

def amntoforanges ():
    Oranges = int(input("Enter the amount of oranges: "))
    return Oranges

def totalapples ():
    total_apples = int(amntofapples*20)
    return total_apples

def totaloranges ():
    total_oranges = int(amntoforanges*25)
    return total_oranges

def totalprice ():
    total_price = int(totalapples+totaloranges)
    return total_price
    
def display 
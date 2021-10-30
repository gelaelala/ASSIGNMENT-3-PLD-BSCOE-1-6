def GetName():
    name = input ("Enter name: ")
    return name

def GetAge():
    age = input ("Enter age: ")
    return age

def GetAddress ():
    address = input ("Enter address: ")
    return address

def display (_name, _age, _address):
    print(f'Hi, my name is {_name}. I am {_age} years old and I live in {_address}.')

Name = GetName ()
Age = GetAge ()
Address = GetAddress ()
display (Name, Age, Address)
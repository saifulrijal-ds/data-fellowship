# function to print result
def introduce(name, address, dob):
    return print("My name is {}, I live in {}, I was born on {}".format(name, address, dob))

# function to input value and call introduce function
def form():
    name = input("Input name: ")
    address = input("Input Address: ")
    dob = input("Input D.O.B: ")
    introduce(name, address, dob)

# call form function
form()
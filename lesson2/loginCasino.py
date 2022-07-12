print("_______________________________\n\n\n")
print ("Welcome to the login page of the casino web site!")
print("_______________________________\n\n\n")


name=input("Please, input your name: ")
surname=input("Please, input your surname: ")
age=int(input("Please, input your age: "))

while len(name)<=1 or len(surname)<=1:# or age<18:
    print("One or more inserted datas are wrong")
    name=input("Please, input your name: ")
    surname=input("Please, input your surname: ")
    #age=int(input("Please, input your age: "))

while age<18:
    print("You cannot access because you are underage!")
    age=int(input("Please, input your age: "))

if len(name)>1 and len(surname)>1 and age>=18:
    print(f"Your name is: {name.capitalize()}")
    print(f"Your surname is: {surname.capitalize()}")
    print(f"Your age is: {str(age)}")
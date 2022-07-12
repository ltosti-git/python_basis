'''
Create python script that emulates casino website login.
Data requests to user: name, surname, age.
Verify that name and surname are more length than 1 character and the age is equal or major of 18 years old.
If so, print a confirmation string. Else print an error in the output.
Notice that users always provide corrected data, in this case.

BONUS: print in output all datas with name and surname in which the first letter must be a capitol letter.
'''

##############################################################################################
##############################################################################################
print("_______________________________\n\n\n")
print ("Welcome to the login page of the casino web site!")
print("_______________________________\n\n\n")

#To Do: INPUT function
name=input("Please, input your name: ")
surname=input("Please, input your surname: ")
age=int(input("Please, input your age: "))

str_age=str(age)

if name and surname and age>=18:
    print(f"your name is {name.capitalize()}")
    print(f"your surname is {surname.capitalize()}")
    print(f"your age is {str_age}")
elif name and surname and age<18:
    print("You cannot access because you are underage!")
else:
    print("Wrong inserted data! Please, re-register again.")
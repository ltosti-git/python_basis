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
import sys

print("_______________________________\n\n\n")

#To Do: INPUT function
name=input("Please, input your name: ")
surname=input("Please, input your surname: ")
age=int(input("Please, input your age: "))

namelen=len(name)
surnamelen=len(surname)
str_age=str(age)

if namelen>1 and surnamelen>1 and age>=18:
    #print("Your name is: "+name,"\nYour surname is: "+surname,"\nYour age is: "+str_age)
    print("Thank you for registering! \nRegards")
    #original_stdout = sys.stdout
    with open('db', 'a') as db:
        sys.stdout = db
        print(name, surname, age)
elif namelen>1 and surnamelen>1 and age<18:
    print("You cannot access because you are underage!")
else:
    print("Wrong inserted data! Please, re-register again.")




# if name and surname and age>=18:
#     print(f"your name is {name}")
#     print(f"your surname is {surname}")
#     print(f"your age is {str_age}")
# elif name and surname and age<18:
#     print("You cannot access because you are underage!")
# else:
#     print("Wrong inserted data! Please, re-register again.")
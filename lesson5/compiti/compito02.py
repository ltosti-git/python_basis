try:
    number=int(input("Insert number > 10: ")) 
    if number <= 10:
        raise Exception(f"Number {number} is minor than 10")
    else:
        print(f"The number you inserted is:\n{number}")
except ValueError as type_error:
    print(f"{type_error} is not an integer!")
    #print("is not an integer!")
except Exception as exception:
    print(exception)
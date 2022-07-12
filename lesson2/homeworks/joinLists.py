## dichiarare due liste di numeri con cinque elementi ciascuna
## creare una lista concatenata che le includa entrambe
list1=[]
list2=[]
joinLists=[]
maxRange=5

for i in range(maxRange):
    num1=input(f"Inserire elemento nr. {i+1} per la prima lista:")
    list1.append(num1)
    
for i in range(maxRange):
    num2=input(f"Inserire elemento nr. {i+1} per la seconda lista:")
    list2.append(num2)

joinLists.append(list1)
joinLists.append(list2)
print(joinLists)



number_of_students=int(input("enter numbers"))
money_of_1_student=int(input("enter money"))
a=(number_of_students*money_of_1_student*30)
if a<=50000:
    print(a,"hum buged ke ander hai")
else:
    print(a,"hum buged ke bhaher hai")

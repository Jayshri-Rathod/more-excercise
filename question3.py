# string_name = "navgurukul"
# if "n" in string_name:
#     print ("n hai")
# else:
#     print ("n nahi hai")
 
# print ("n" in string_name)
# print (type("n" in string_name)) 

password=input("enter password")
if len(password)>=6 and len(password)<=16:
    if "$" in password:
        if "2" or "8" in password:
            if "A" or "Z" in password:
                print(password,"strong password")
            else:
                print("weak password")
        else:
            print("weak password")
    else:
            print("weak password")
else:
    print("weak password")
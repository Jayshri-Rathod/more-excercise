# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai'] 
i=0
a=[]
while i<len(string_list):
    same=string_list[i]
    if same not in a:
        a.append(same)
    i+=1
print(a)



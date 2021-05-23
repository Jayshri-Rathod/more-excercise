# def is_harshad_number(n):
#     num=n
#     sum=0
#     while n>0:
#         sum=sum+(n%10)
#         n=n//10
#     if num%sum==0:
#         return "true"
#     else:
#         return "false"
# result=is_harshad_number(147)
# print(result)


def is_harshad_number(num):
    x=num
    x_digits=list(str(x))
    i=0
    sum=0
    while i<len(x_digits):
        a=int(x_digits[i])
        sum=sum+a
        i+=1
    if num%sum==0:
        return "True"
    else:
        return "False"
result=is_harshad_number(42)
print(result)

# def is_harshad_number():
#     i=1
#     while i<=1000:
#         x=i
#         x_digits=list(str(x))
#         j=0
#         sum=0
#         while j<len(x_digits):
#             b=int(x_digits[j])
#             sum=sum+b
#             j+=1
#         if i%sum==0:
#             print(i)
#         else:
#             pass
#         i+=1
# is_harshad_number()
# print(result)





        
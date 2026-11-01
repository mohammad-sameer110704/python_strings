str=input("Enter any string : ")
name=""
l=len(str)
n=l-1
for i in range(l):
    name=name+str[n]
    n -= 1
print("Reversed string : ",name)

# string=input("Enter any string : ")
# lis=list(string)
# l=0
# r=len(string)-1
# while l<r :
#     lis[l],lis[r]=lis[r],lis[l]
#     l +=1
#     r -=1
# reversed_text = "".join(lis)
# print("Reversed string:", reversed_text)
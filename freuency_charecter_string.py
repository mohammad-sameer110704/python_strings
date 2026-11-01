string=str(input("Enter any Thing : "))
frquency={}
for i in string:
    if i in frquency:
        frquency[i]=frquency[i]+1
    else:
        frquency[i]=1
print(f"frquency of each charecter in the given string {string.upper()} is {frquency}")
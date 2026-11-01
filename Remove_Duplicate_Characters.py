string=str(input("Enter any Thing : ")).replace(" ","")
duplicates=""
for i in string:
    if i in string[string.index(i) + 1:]:
        if i not in duplicates:
            duplicates=duplicates+i
if len(duplicates) > 0:
    print(duplicates)
else :
    print(string)


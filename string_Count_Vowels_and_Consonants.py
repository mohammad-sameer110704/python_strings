string=str(input("Enter any thing : "))
v=0
c=0
for i in string:
    if i in "AEIOUaeiou":
        v +=1
    else :
        c +=1
print(f'There are {v} vowels in {string}')
print(f'There are {c} consonents in {string}')
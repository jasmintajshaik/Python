'''Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

'''

inp=input()
upper,lower=0,0
for i in inp:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("UPPER CASE",upper)
print("LOWER CASE",lower)
'''

#Another way using dictionary:

inp=input()
d={"lower":0,"upper":0}
for i in inp:
    if i.isupper():
        d["upper"]+=1
    elif i.islower():
        d["lower"]+=1
print("UPPER CASE",d["upper"])
print("LOWER CASE",d["lower"])
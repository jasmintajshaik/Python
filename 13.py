'''Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

'''
inp=input()
letters,digits=0,0
for letter in inp:
    if letter.isalpha():
        letters+=1
    elif letter.isdigit():
        digits+=1
print("LETTERS",letters)
print("DIGITS",digits)'''


#Another way using dictionary:
inp=input()
d={"letters":0,"digits":0}
for letter in inp:
    if letter.isalpha():
        d["letters"]+=1
    elif letter.isdigit():
        d["digits"]+=1
    else:
        pass
print("LETTERS",d["letters"])
print("DIGITS",d["digits"])



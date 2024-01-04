'''Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''
'''length=int(input())
inp=[]
for i in range(length):
    inp.append(input())
for i in range(length):
    print(str.upper(inp[i]))'''

inp=[]
while(True):
    s=input()
    if s:
        inp.append(s.upper())
    else:
        break
for i in inp:
    print(i)




'''Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
'''


'''
Code1:
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=",")''' #This prints comma at the end as well which is not as expected.
#Code2
l=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print (','.join(l)) #Join method can only be used on string instance

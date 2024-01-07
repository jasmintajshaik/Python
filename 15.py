'''Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

'''
#One way

a=int(input())
sum=0
temp=1
res=0
for i in range(4):
    sum+=a*temp #generates 9,99,999,9999
    temp*=10
    res+=sum #adds 9+99+999+9999
print(res)
'''

#Another way:
a=int(input())

n1="%s" %(a) #9 as string
n2="%s%s" %(a,a) #99 as string
n3="%s%s%s" %(a,a,a) #999 as string
n4="%s%s%s%s" %(a,a,a,a) #9999 as string
print(int(n1)+int(n2)+int(n3)+int(n4))


n=int(input())
l=[]
for i in range(n):
    l.append(input())
print(l)
my_dict={}

for i in l:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1
print(my_dict)
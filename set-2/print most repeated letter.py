s=str(input())
s1=set(s)
m=0
for i in s1:
    if(s.count(i)>m):
        m=s.count(i)
        c=i
print(c)
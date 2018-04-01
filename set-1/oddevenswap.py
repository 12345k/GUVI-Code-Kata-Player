s =str(input())
l=len(s)
for i in range(0,l-1):
    j=i+1
    tem=s[i]
    s[i]=s[j]
    s[j]=tem
    i=i+2
print(s)
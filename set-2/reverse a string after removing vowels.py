s=str(input())
s1=""
for i in range(len(s)):
    if(s[i]!="a" and s[i]!="e" and s[i]!="i" and s[i]!="o" and s[i]!="u" and s[i]!="A" and s[i]!="E" and s[i]!="I" and s[i]!="O" and s[i]!="U" ):
        s1=s1+s[i]
print(s1[::-1])
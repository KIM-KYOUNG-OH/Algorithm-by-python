n,s = int(input()), input()
s= input()
bonus, result = 0,0

for i in range(len(s)):
    if (s[i]=='O'):
        result+=(i+1)+bonus
        bonus+=1
    else:
        bonus=0
    
print(result)
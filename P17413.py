s, temp = input(), ''

ck = False

for i in s:
    if i == ' ':
        if not ck:
            print(temp[::-1], end=' ')
            temp=''
        else:
            print(' ', end='')
    elif i == '<':
        ck = True
        print(temp[::-1], end='')
        temp=''
        print('<', end='')
    elif i == '>':
        ck = False
        print('>', end='')
    else:
        if ck:
            print(i, end='')
        else:
            temp+=i
print(temp[::-1], end='')
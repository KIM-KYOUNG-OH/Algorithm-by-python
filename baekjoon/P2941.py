s = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for cro in croatia:
    s = s.replace(cro, 'a')
print(len(s))
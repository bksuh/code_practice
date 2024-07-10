d = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
a = list(input().split())

for element in d:
    if element in a[1:]:
        a.remove(element)

for i in range(len(a)):
    print(a[i][0].capitalize(), end='')
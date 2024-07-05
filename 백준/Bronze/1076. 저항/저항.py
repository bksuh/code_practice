d = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue':6, 'violet':7,'grey':8, 'white':9}
c1 = input()
c2 = input()
c3 = input()
c12 = int(str(d[c1]) + str(d[c2]))
down = pow(10, d[c3])
print(c12*down)
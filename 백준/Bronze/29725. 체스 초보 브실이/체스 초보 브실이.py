ans1, ans2 = 0, 0
moves = ['k','p', 'n', 'b', 'r', 'q']
scores = [0, 1, 3, 3 ,5,  9]

for _ in range(8):
    a = input()
    for i in range(len(moves)):
        x =a.count(moves[i])
        y = a.count(moves[i].upper())
        if x != 0:
            ans1 += (x*scores[i])
        if y != 0:
            ans2 += (y*scores[i])
print(ans2-ans1)
darts = list(map(int, input().split()))

idx = darts.index(20)
alice = 20
if idx == 0:
    alice += darts[1]
    alice += darts[-1]
elif idx == 19:
    alice += darts[18]
    alice += darts[0]
else:
    alice += (darts[idx-1] + darts[idx+1])

alice /= 3
bob = sum(darts)/len(darts)

if bob == alice:
    print('Tie')
elif bob > alice:
    print('Bob')
else:
    print("Alice")
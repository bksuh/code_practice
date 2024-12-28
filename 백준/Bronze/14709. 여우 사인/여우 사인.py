t = int(input())
fingers = [[] for _ in range(6)]

ping = True

for _ in range(t):
    a, b = map(int, input().split())
    fingers[a].append(b)
    fingers[b].append(a)

if (3 and 4 not in fingers[1]) or len(fingers[1]) !=2:
    ping = False
elif (1 and 4 not in fingers[3]) or len(fingers[3]) !=2:
    ping = False
elif (1 and 3 not in fingers[4]) or len(fingers[4]) !=2:
    ping = False
    
if ping:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")
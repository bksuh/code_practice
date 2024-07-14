import collections

n = int(input())
card = collections.deque(i for i in range(1, n+1))
while True:
    print(card.popleft(), end = ' ')
    if len(card) == 0:
        break
    card.append(card.popleft())

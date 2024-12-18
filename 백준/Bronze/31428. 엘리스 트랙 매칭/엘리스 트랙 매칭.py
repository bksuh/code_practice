t = int(input())

picks = list(input().split())
pick = input()

if pick in picks:
    print(picks.count(pick))
else:
    print(0)
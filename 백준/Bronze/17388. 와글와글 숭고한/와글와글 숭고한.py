score = list(map(int, input().split()))
school =['Soongsil', 'Korea', 'Hanyang']

if sum(score) >= 100:
    print('OK')
else:
    ans = score.index(min(score))
    print(school[ans])
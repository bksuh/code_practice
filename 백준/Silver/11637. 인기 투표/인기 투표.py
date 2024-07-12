n = int(input())
for _ in range(n):
    t = int(input())
    votes = list(int(input()) for _ in range(t))
    max_val = max(votes)
    if votes.count(max_val) == 1:
        if  sum(votes)- max_val < max_val:
            print(f"majority winner {votes.index(max_val)+1}")
        else:
            print(f"minority winner {votes.index(max_val)+1}")
    else:
        print("no winner")
        
import sys
input = sys.stdin.readline
dc = {}
cnt = 0

while True:

    tree_name = input().rstrip()
    if not tree_name:
        break
    cnt += 1
    if tree_name in dc:
        dc[tree_name] += 1
    else:
        dc[tree_name] = 1
        
 

reals = [(k, v) for k, v in dc.items()]
reals.sort(key=lambda x: x[0])
for tree, num in reals:
    print(f"{tree} {(num/cnt)*100:.4f}")
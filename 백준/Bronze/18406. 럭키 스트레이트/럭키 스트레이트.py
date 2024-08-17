tmp = list(int(c) for c in input())
left = tmp[0:len(tmp)//2]
right = tmp[len(tmp)//2:]
print("LUCKY" if sum(left) == sum(right) else "READY")
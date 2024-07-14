scores = [int(input()) for _ in range(10)]
    
total = 0
closest = 0
    
for score in scores:
    total += score
    if abs(100 - total) <= abs(100 - closest):
        closest = total
    
print(closest)
t = int(input())
for i in range(t):
    score = int(input())
    if score <= 25:
        result = 'World Finals'
    elif score <= 1000:
        result = 'Round 3'
    elif score <= 4500:
        result = 'Round 2'
    else:
        result = 'Round 1'
    print(f"Case #{i+1}: {result}")
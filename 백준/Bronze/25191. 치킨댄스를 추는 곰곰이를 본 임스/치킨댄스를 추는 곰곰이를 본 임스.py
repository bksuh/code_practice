chicken = int(input())
cola, beer = map(int, input().split())

total_chicken = cola//2 + beer

print(min(total_chicken, chicken))
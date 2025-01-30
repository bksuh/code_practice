N, W, H, X = map(int, input().split())

print(min(N, (W//X)*(H//X)))
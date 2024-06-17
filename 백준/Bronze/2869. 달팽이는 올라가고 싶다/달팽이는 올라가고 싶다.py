import sys
import math
input = sys.stdin.readline

a, b, v = map(int, input().split())
ans = (v-b)/(a-b)
print(math.ceil(ans))

ans = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3
x = int(input())
y = int(input())
z = int(input())
ans = ans + (x +y*3 + z)
print('The 1-3-sum is', ans)
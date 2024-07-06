dic = [c for c in 'CAMBRIDGE']
tar = input()
for c in tar:
    if c in dic:
        tar = tar.replace(c, '')
print(tar)
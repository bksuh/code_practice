tar = input()

while '()' in tar:
    tar = tar.replace('()','')

print(len(tar))
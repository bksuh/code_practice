n = int(input())
tar = input()
a = tar.count('security')
b = tar.count('bigdata')

if a  > b :
    print("security!")
elif a == b:
    print("bigdata? security!")
else:
    print("bigdata?")
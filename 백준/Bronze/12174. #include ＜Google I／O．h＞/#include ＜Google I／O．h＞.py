n = int(input())

for i in range(n):
    b = int(input())
    string = input()
    ans = ''
    for j in range(0, len(string), 8):
        tmp_str = ''
        tmp = string[j:j+8]
        for c in tmp:
            if c == 'I':
                tmp_str += '1'
            else:
                tmp_str += '0'
        ans += chr(int(tmp_str, 2))
    print(f"Case #{i+1}: {ans}")

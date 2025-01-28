def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N, M = int(data[0]), int(data[1])
    s = data[2]
    
    vowels = set('AEIOU')
    ans = []
    
    # Step 1: Remove trailing vowels
    while s and s[-1] in vowels:
        s = s[:-1]
    if not s:
        print("NO")
        return
    
    # Step 2: Add the first non-vowel
    ans.append(s[-1])
    s = s[:-1]
    
    # Step 3: Find the first 'A'
    while s and s[-1] != 'A':
        s = s[:-1]
    if not s:
        print("NO")
        return
    ans.append(s[-1])
    s = s[:-1]
    
    # Step 4: Find the second 'A'
    while s and s[-1] != 'A':
        s = s[:-1]
    if not s:
        print("NO")
        return
    ans.append(s[-1])
    s = s[:-1]
    
    # Step 5: Validate length
    if len(s) + len(ans) < M:
        print("NO")
        return
    
    # Step 6: Construct the result
    print("YES")
    print(s[:M - 3] + ''.join(ans[::-1]))

if __name__ == "__main__":
    main()

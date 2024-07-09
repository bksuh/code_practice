n = int(input())
d={1:'Yakk', 2:'Doh', 3:'Seh', 4:'Ghar', 5:'Bang', 6:'Sheesh'}
for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(f"Case {_+1}: ", end='')
    if arr.count(1)==2:
        print("Habb Yakk")
    elif arr.count(2) == 2:
        print("Dobara")
    elif arr.count(3) == 2:
        print("Dousa")
    elif arr.count(4) ==2:
        print("Dorgy")
    elif arr.count(5) == 2:
        print("Dabash")
    elif arr.count(6) == 2:
        print("Dosh")
    elif arr[0] == 6 and arr[1] == 5:
        print("Sheesh Beesh")
    else:
        for elem in arr:
            print(d[elem], end =' ')
        print()
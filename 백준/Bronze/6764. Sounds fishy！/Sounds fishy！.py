arr = [int(input()) for _ in range(4)]
des_arr = sorted(arr)
ris_arr = sorted(arr, reverse=True)

if len(set(arr))== 4 and arr == des_arr :
    print("Fish Rising")
elif len(set(arr))== 4 and arr == ris_arr:
    print("Fish Diving")
elif arr.count(arr[0]) == 4:
    print("Fish At Constant Depth")
else:
    print("No Fish")
def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        return -1 if len(arr1) < len(arr2) else 1
    else:
        a = sum(arr1)
        b = sum(arr2)
        if a == b:
            return 0
        elif a > b:
            return 1
        else:
            return -1

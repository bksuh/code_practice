def solution(arr, idx):
    answer = 0
    tmp = arr[idx::]
    if 1 in tmp:
        answer = tmp.index(1) + idx
    else:
        answer= -1
    return answer
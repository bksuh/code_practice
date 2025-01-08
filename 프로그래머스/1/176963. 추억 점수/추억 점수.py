def solution(name, yearning, photo):
    answer = []
    for picture in photo:
        score = 0
        for i in range(len(name)):
            if name[i] in picture:
                score += yearning[i]
        answer.append(score)
    return answer
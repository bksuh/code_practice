def solution(babbling):
    answer = 0
    say = ["aya", "ye", "woo", "ma"]
    for _ in range(len(say)):
        for says in say:
            for i in range(len(babbling)):
                while babbling[i].startswith(says):
                    babbling[i] = babbling[i].replace(says, '')

    return babbling.count('')
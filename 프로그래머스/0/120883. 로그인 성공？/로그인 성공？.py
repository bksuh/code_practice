def solution(id_pw, db):
    ids = [a[0] for a in db]
    password = [a[1] for a in db]
    info_id, info_pw = id_pw
    if info_id in ids:
        if info_pw == password[ids.index(info_id)]:
            answer = 'login'
        else:
            answer = 'wrong pw'
    else:
        answer = 'fail'
    return answer
def solution(my_string):
    mos = ['a', 'e', 'i', 'o',  'u']
    for mo in mos:
        my_string = my_string.replace(mo, '')
    return my_string
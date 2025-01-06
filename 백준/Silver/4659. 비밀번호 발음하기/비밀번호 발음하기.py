while True:
    password = input()
    if password == 'end':
        break
    m = False
    pri = False
    cnt1, cnt2 = 0, 0
    m_list = ['a', 'e', 'i', 'o', 'u']
    for c in password:
        if c in m_list:
            m = True
            cnt1 +=1
            cnt2 = 0
        else:
            cnt2 += 1
            cnt1 = 0
        if cnt1 >=3 or cnt2 >=3:
            print(f"<{password}> is not acceptable.")
            pri = True
            break
    cur_indi = True
    current = password[0]
    for i in range(1, len(password)):
        if current == password[i] and current not in ['e', 'o']:
            cur_indi = False
            break
        else:
            current = password[i]
    if m and cnt1 <3 and cnt2 < 3:
        if cur_indi:
            print(f"<{password}> is acceptable.")
        elif not pri:
            print(f"<{password}> is not acceptable.")
    elif not pri:
        print(f"<{password}> is not acceptable.")
        

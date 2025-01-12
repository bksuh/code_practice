sy, sm, sd = map(int, input().split())
ey, em, ed = map(int, input().split())

sea_age = ey-sy+1
yun_age = ey-sy
man_age = 0

if sm < em:
    man_age = ey-sy
elif sm == em:
    if sd <= ed:
        man_age = ey-sy
    else:
        man_age = ey-sy-1
else:
    man_age = ey-sy-1

print(man_age)
print(sea_age)
print(yun_age)
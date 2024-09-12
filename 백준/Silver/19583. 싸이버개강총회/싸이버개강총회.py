import sys
input = sys.stdin.readline
st, mt, et = input().rstrip().split()
st = int(st.replace(':', ''))
mt = int(mt.replace(':', ''))
et = int(et.replace(':', ''))
check = {'check':[]}

cnt = 0
while True:
    try:
      time, name = input().rstrip().split()
      time = int(time.replace(':', ''))
      if time <= st:
         check[name] = 1
      elif name not in check.keys():
         continue
      if mt <= time <= et and check[name] == 1:
         cnt+=1
         check[name] +=1
    except:
        break
print(cnt)
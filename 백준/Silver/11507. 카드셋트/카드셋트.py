tar = input()
shape = {'P':0, 'K': 1, 'H': 2, 'T': 3}
cards = [[0]*13 for _ in range(4)]
indi = True
for i in range(0, len(tar),3):
    if cards[shape[tar[i]]][int(tar[i+1:i+3])-1] == 1:
        indi = False
        print("GRESKA")
        break
    else:
        cards[shape[tar[i]]][int(tar[i+1:i+3])-1] = 1

if indi:
    for i in range(len(cards)):
        print(cards[i].count(0), end =' ')
classroom = {'Algorithm': '204', 'DataAnalysis':'207',
'ArtificialIntelligence':'302','CyberSecurity':'B101','Network':'303',
'Startup':'501','TestStrategy':'105'}

t = int(input())

for _ in range(t):
    room = input()
    print(classroom[room])
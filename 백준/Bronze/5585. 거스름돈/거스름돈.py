coin = 0
cost = int(input())
cost = 1000 - cost  

coin += (cost//500)
cost -= 500*(cost//500)

coin += (cost//100)
cost -= 100*(cost//100)

coin += (cost//50)
cost -= 50*(cost//50)

coin += (cost//10)
cost -= 10*(cost//10)

coin += (cost//5)
cost -= 5*(cost//5)

coin += (cost//1)
cost -= (cost//1)

print(coin)

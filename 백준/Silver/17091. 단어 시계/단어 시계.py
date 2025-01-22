hour = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "one"]
min = ["o' clock", "one minute", "two minutes", "three minutes", "four minutes",
 "five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes", 
 "ten minutes", "eleven minutes", "twelve minutes", "thirteen minutes", "fourteen minutes", 
 "quarter", "sixteen minutes", "seventeen minutes", "eighteen minutes", "nineteen minutes", 
 "twenty minutes", "twenty one minutes", "twenty two minutes", "twenty three minutes", 
 "twenty four minutes", "twenty five minutes", "twenty six minutes", "twenty seven minutes", 
 "twenty eight minutes", "twenty nine minutes", 'half']
a = int(input())
b = int(input())
diff = 60 - b

if b == 0:
    print(f"{hour[a]} {min[b]}")
elif b <=30:
    print(f"{min[b]} past {hour[a]}")
else:
    print(f"{min[diff]} to {hour[a+1]}")
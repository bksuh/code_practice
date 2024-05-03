

def calculation_Checksum(message):
    calculation_checksum = len(message)
    return calculation_checksum

def check_Checksum(message):
    check_message = 0
    if (check_message):
        return 1
    else:
        return 0

n = int(input("How many times do you want to test"))
for i in range(n):
    message = input("Input your message : ")
    calculation_Checksum(message)
    if (check_Checksum(message)):
        print("No ERROR")
    else:
        print("Error")
    

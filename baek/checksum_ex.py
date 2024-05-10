

def calculation_Checksum(messages):
    sum = 0
    for message in messages:
        sum+=ord(message)
    carry = sum & 0xFFFF0000
    carry = carry>>16
    result = sum & 0x0000FFFF
    while(carry!=0):
        result +=carry
        carry = result &0xFFFF0000
        carry>>16
    result = result^0xFFFF
    return result

def check_Checksum(messages, checksum):
    sum = 0
    for message in messages:
        sum+=ord(message)
    carry = sum & 0xFFFF0000
    carry>>=16
    result = sum&0x0000FFFF
    while(carry!=0):
        result = result+carry
        carry = result & 0xFFFF0000
        carry = carry>>16
    
    errordetect = result +checksum
    errordetect ^=0xFFFF
    if errordetect==0 :
        return 1
    else:
        return 0

n = int(input("How many times do you want to test : "))
for i in range(n):
    message = input("Input your message : ")
    print("==========================")
    print("Sender message : {}\n".format(message))
    checksum= calculation_Checksum(message)
    print("Checksum value : {}".format(checksum))
    if check_Checksum(message, checksum):
        print("Recieved")
        print("No error detected")
        print("checksum used {}".format(checksum))
    else:
        print("Error Detected")
        print("checksum usde {}".format(checksum))
    print("==========================")
    
    

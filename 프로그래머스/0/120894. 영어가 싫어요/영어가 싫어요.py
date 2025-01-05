def solution(numbers):
    lookup = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, num in enumerate(lookup):
        while num in numbers:
            numbers = numbers.replace(num, str(i))
    return int(numbers)
import math
def solution(n, m):
    a = math.gcd(n, m)
    answer = [a, (n//a) * (m//a) * a]
    return answer
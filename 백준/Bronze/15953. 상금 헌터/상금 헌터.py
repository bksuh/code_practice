def prize_2017(rank):
    prize_table = [500, 300, 200, 50, 30, 10]
    rank_limit = [1, 2, 3, 4, 5, 6]
    
    if rank == 0 or rank > 21:
        return 0
    
    total_people = 0
    for i in range(len(prize_table)):
        total_people += rank_limit[i]
        if rank <= total_people:
            return prize_table[i] * 10000
    return 0

def prize_2018(rank):
    prize_table = [512, 256, 128, 64, 32]
    rank_limit = [1, 2, 4, 8, 16]
    
    if rank == 0 or rank > 31:
        return 0
    
    total_people = 0
    for i in range(len(prize_table)):
        total_people += rank_limit[i]
        if rank <= total_people:
            return prize_table[i] * 10000
    return 0

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        a, b = map(int, input().split())
        total_prize = prize_2017(a) + prize_2018(b)
        results.append(total_prize)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
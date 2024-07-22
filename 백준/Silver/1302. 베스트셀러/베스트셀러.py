n = int(input())
books = {}
for _ in range(n):
    book = input()
    if book in books:
        books[book] +=1
    else:
        books[book] = 1

books = list((k,v) for k,v in books.items())
books.sort(key = lambda x : (-x[1], x[0]))
print(books[0][0])
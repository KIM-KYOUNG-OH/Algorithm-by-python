n=int(input())
books={}
for _ in range(n):
    book=input()
    if book not in books:
        books[book]=1
    else:
        books[book]+=1
target = max(books.values())
array=[]
for book, num in books.items():
    if target==num:
        array.append(book)
array=sorted(array)
print(array[0])
# A List of Dictionaries

def main():
    books = []

    n = int(input("Enter the size: "))

    for i in range(n):
        book = dict()
        book["title"] = input("Title: ").strip().capitalize()
        book["author"] = input("Author: ").strip().capitalize()
        # print(book)
        books.append(book)

    print(books)

main()
import csv

def main():
    books = []

    with open("phonebook.csv") as file:
        file_reader = csv.DictReader(file)
        for book in file_reader:
            books.append(book)
    
    print(books)


main()
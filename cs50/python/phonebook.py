import csv

def main():
    file = open("phonebook.csv", "a")
    name = input("Name: ").strip().capitalize()
    number = input("Number: ")

    writer = csv.writer(file)
    writer.writerow([name,number])

    file.close()

main()
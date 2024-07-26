def main():
    n = int(input("Enter n: "))

    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(j, end = "")
            j += 1
        print()
        i += 1

main()
from sys import argv

def main():   
    if len(argv) == 2:
        print(f"Hello, {argv[1]}!")
    else:
        print("Hello, World!")

main()
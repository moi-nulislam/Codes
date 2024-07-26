# This code swaps two numbers without using any third variable
# Though python can do it easily by using "x , y = y , x"
def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    
    print(f"Originl: X = {x}     Y = {y}")

    x = x + y
    y = x - y
    x = x - y

    print(f"Swapped: X = {x}     Y = {y}")

main()
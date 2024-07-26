def main():
    scores = []
    n = int(input("Enter n: "))

    for i in range(n):
        score = int(input("Enter score: "))
        scores.append(score)
        # scores += [score]

    average = sum(scores) / len(scores)
    print(f"Average = {average}")


main()


if __name__ == '__main__':

    scores = set()
    nested_list = []
    second_lowest_names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        nested_list.append([name, score])
        scores.add(score)

    second_lowest = sorted(scores)[1]
    for name, score in nested_list:
        if score == second_lowest:
            second_lowest_names.append(name)

    # Sort alphabetically.
    second_lowest_names.sort()

    print("\n".join(second_lowest_names))
def pair_sum(array, k):
    if len(array) < 2:
        return print(f"Too small")

    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))
    print(seen)
    print(output)
    print("\n".join(map(str, list(output))))


pair_sum([1,2,3,2], 4)


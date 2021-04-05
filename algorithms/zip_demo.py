def demo():
    max_name = None
    names = ["Sambaran", "Debangana", "Chorki"]
    counts = [len(n) for n in names]
    max_count = 0
    for name, count in zip(names, counts):
        if count > max_count:
            max_count = count
            max_name = name
    return max_name


def no_walrus():
    fruits = {"apple": 4, "lemon": 2}
    count = fruits.get("lemon")
    if count:
        print(f"lemon={count}")
    else:
        print("out of lemons")


if __name__ == "__main__":
    no_walrus()
    print()

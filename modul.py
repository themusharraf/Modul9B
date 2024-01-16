s = ["ALi", "john", "Akbar"]

name: list = []


def topic(data: list) -> list:
    for x in data:
        if x[0] == "A":
            name.append(x)
    return name

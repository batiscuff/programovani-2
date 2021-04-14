def my_map(tokens, func):
    # return list(map(func, tokens))
    return [func(token) for token in tokens]


if __name__ == "__main__":
    print(my_map(["ahoj", "jak", "se", "vede"], len))
    print(my_map(["jaka", "je", "veda"], len))
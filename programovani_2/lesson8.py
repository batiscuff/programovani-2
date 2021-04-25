def up_to_ten(number):
    return number * 10

def my_big_map(word_list, func_list):
    func1 = func_list[0]
    func2 = func_list[1]
    return [func2(func1(word)) for word in word_list]


if __name__ == "__main__":
    word_list = ["ahoj", "jak", "se", "vede"]
    func_list = [len, up_to_ten]
    print(my_big_map(word_list, func_list))
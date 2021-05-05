from lesson7 import my_map


def up_to_ten(number):
    return number * 10

def my_big_map(word_list, func_list):
    for func in func_list:
        word_list = my_map(word_list, func)
    return word_list


if __name__ == "__main__":
    word_list = ["ahoj", "jak", "se", "vede"]
    func_list = [len, up_to_ten]
    print(my_big_map(word_list, func_list))

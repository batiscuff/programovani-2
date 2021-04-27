from lesson7 import my_map


def up_to_ten(number):
    return number * 10

def my_big_map(word_list, func_list):
    results = None
    for func in func_list:
        elements_list = word_list if results is None else results
        results = my_map(elements_list, func)
    return results


if __name__ == "__main__":
    word_list = ["ahoj", "jak", "se", "vede"]
    func_list = [len, up_to_ten]
    print(my_big_map(word_list, func_list))

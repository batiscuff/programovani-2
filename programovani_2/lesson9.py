from math import floor


data = [("pes", 1), ("pes", 2), ("pes", 3),
        ("pes", 4), ("pes", 5), ("jezevec", 1),
        ("jezevec", 2), ("jezevec", 3), ("jezevec", 4),
        ("kočka", 1), ("kočka", 2), ("kočka", 3)]


def find_smallest_value(dataset):
    categories = {item[0]: 0 for item in dataset}  # {'pes': 0, 'jezevec': 0, 'kočka': 0}
    for item in dataset:
        category = item[0]
        categories[category] += 1

    smallest_category_value = min(categories.values())
    return smallest_category_value


def make_test_train(dataset, ratio):
    smallest_category_value = find_smallest_value(dataset)

    train_floor = floor(ratio * smallest_category_value)
    test_floor = floor(smallest_category_value - train_floor)

    #test_dataset  = [*filter(lambda x: x[1] == test_floor, dataset)]
    test_dataset  = [*filter(lambda x: x[1] == train_floor + test_floor, dataset)]
    train_dataset = [*filter(lambda x: x[1] <= train_floor, dataset)]

    return {"test": test_dataset, "train": train_dataset}



if __name__ == "__main__":
    print(make_test_train(data, 2/3))
    print(make_test_train(data, 0.8))
    print(make_test_train(data, 0.5))

data = [("pes", 1), ("pes", 2), ("pes", 3),
        ("pes", 4), ("pes", 5), ("jezevec", 1),
        ("jezevec", 2), ("jezevec", 3), ("jezevec", 4),
        ("kočka", 1), ("kočka", 2), ("kočka", 3)]


def find_smallest(dataset: list) -> tuple:
    categories = {_tuple[0]: 0 for _tuple in dataset}  # {'pes': 0, 'jezevec': 0, 'kočka': 0}

    for _tuple in dataset:
        category = _tuple[0]
        categories[category] += 1

    smallest_category_name  = min(categories, key=categories.get)
    smallest_category_value = categories.get(smallest_category_name)
    return (smallest_category_name, smallest_category_value)


def make_test_train(dataset: list, ratio: float) -> dict:
    _, smallest_category_value = find_smallest(dataset)
    test_train_dataset = {
        "test":  [*filter(lambda x: x[1] == smallest_category_value, dataset)],
        "train": [*filter(lambda x: x[1] < smallest_category_value, dataset)]
    }
    return test_train_dataset


if __name__ == "__main__":
    print(make_test_train(data, 2/3))
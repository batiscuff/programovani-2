from icecream import ic
from utils import remove_punctuation


texts = [
    {"jmeno": "text1", "data": "ahoj, jeseter"},
    {"jmeno": "text2", "data": "jeseter? ne!"},
    {"jmeno": "text3", "data": "to ne"},
]


def string_preparation(string: str) -> set:
    """Čisti řetězec a vrátí množinu(set) ze slov"""
    cleaned_string = remove_punctuation(string)
    data_set = set(cleaned_string.lower().split())
    return data_set


def create_tokens_set(texts: list) -> set:
    """Vytvoří množinu tokenů na základě textu v slovniku["data"]"""
    tokens_set = set()
    for dictionary in texts:
        string = dictionary.get("data")
        data_set = string_preparation(string)
        tokens_set.update(data_set)
    return tokens_set


def vectorize(texts: list, global_vocabulary: set) -> list:
    """Vytvoří model Bag-of-Words založený na textu a globálním slovníku"""
    vectors = []
    for text_dict in texts:
        name = text_dict.get("jmeno")
        data = text_dict.get("data")
        sent_vec = []
        for token in global_vocabulary:
            if token in data:
                sent_vec.append(1)
            else:
                sent_vec.append(0)
        vectors.append({name: sent_vec})
    return vectors


def main() -> None:
    global_vocabulary = create_tokens_set(texts)
    vectorized = vectorize(texts, global_vocabulary)
    ic(global_vocabulary, vectorized)


if __name__ == "__main__":
    main()

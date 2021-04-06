from utils import remove_punctuation


texts = [
    {"jmeno": "text1", "data": "ahoj, jeseter"},
    {"jmeno": "text2", "data": "jeseter? ne!"},
    {"jmeno": "text3", "data": "to ne"},
]


def string_preparation(string):
    """Čisti řetězec a vrátí množinu(set) ze slov"""
    cleaned_string = remove_punctuation(string)
    words_set = set(cleaned_string.lower().split())
    return words_set


def create_tokens_set(texts):
    """Vytvoří množinu tokenů na základě textu v slovniku["data"]"""
    tokens_set = set()
    for dictionary in texts:
        string = dictionary.get("data")
        words_set = string_preparation(string)
        tokens_set.update(words_set)
    return tokens_set


def vectorize(texts, global_vocabulary):
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


global_vocabulary = create_tokens_set(texts)
vectorized = vectorize(texts, global_vocabulary)
print(global_vocabulary, vectorized, sep="\t")

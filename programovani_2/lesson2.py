from icecream import ic
from utils import load_file, remove_punctuation


fname = "files/muj_text_uloha2"


def get_tokens_freq(string: str) -> dict:
    string = remove_punctuation(string)
    string_list = string.lower().split()

    result = {}
    for key in set(string_list):  # filtruju pří pomoci set'a
        result.update({key: 0})

    for item in string_list:
        # Pokud je prvek ze seznamu stejný jako v klíči slovníku
        # hodnota(value) tohoto klíče se zvýší o 1 jednotku.
        if item in result.keys():
            result[item] += 1
    return result


def calc_ttr_from_dict(data: dict) -> float:
    """Vypočítá type-to-token ratio ze slovníku"""
    data_size = len(data)
    keys_lenght = 0
    for key in data.keys():
        keys_lenght += len(key)
    return data_size / keys_lenght


def main():
    string = load_file(f"{fname}.txt")
    frequence = get_tokens_freq(string)
    ic(frequence)
    ic(calc_ttr_from_dict(frequence))


if __name__ == "__main__":
    main()

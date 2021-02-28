from prettytable import PrettyTable
from utils import load_file, remove_punctuation, save_file


fname = "files/muj_text_uloha1"


def syllables(word: str) -> int:
    """Počítá samohlásky ve slově"""
    word = word.lower()
    vowels = "aeiouyáéíóúýěů"  # samohlasky
    count = 0
    if word[0] in vowels:
        count += 1
    for i in range(1, len(word)):
        if word[i] in vowels and word[i - 1] not in vowels:  # no, de, ba...
            count += 1
    if count == 0:  # pro slova bez samohlásek
        count += 1
    return count


def normalize_data(data: list) -> list:
    """Normalizuje data pro uložení do souboru"""
    results = []
    for elements in data:
        if len(elements[0]) > 3:  # větši než slovo "šel"
            string = "\t".join(str(element) for element in elements)
        else:
            string = "\t\t".join(str(element) for element in elements)
        results.append(f"{string}\n")
    return results


def create_table(data: list) -> str:
    """Vytvoří textovou tabulku na základě vstupních dat"""
    table = PrettyTable(["slovo", "počet písmen", "počet slabik"])
    for elements in data:
        table.add_row([element for element in elements])
    return str(table)


def main() -> None:
    line = load_file(f"{fname}.txt")
    line = remove_punctuation(line)

    string_list = line.lower().split()
    lenword_list = [len(word) for word in string_list]
    syllables_count_list = [syllables(word) for word in string_list]

    # slepí všechny seznamy do jednoho iterovaného objektu a promění jej v seznam
    data = list(zip(string_list, lenword_list, syllables_count_list))

    # save_file(f"{fname}_vertical.txt", normalize_data(data))  # první možnost uložení
    save_file(
        f"{fname}_vertical.txt", create_table(data)
    )  # druhá možnost uložení


if __name__ == "__main__":
    main()

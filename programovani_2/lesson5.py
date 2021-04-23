"""
Создайте функцию folder_to_bow которая загрузит все файлы.txt из
указаного адресса и сделает с них "мешок слов" модель.
"""
import json
from pathlib import Path
from utils import load_file, remove_punctuation, save_file


current_dir = Path.cwd()
fname = "bag_of_words_lesson5.json"
output_file = str(current_dir / fname)
files_dir = current_dir / "files_lesson5"  # programovani_2/files_lesson5


def load_all_txt_files(files: list) -> dict:
    texts = {}
    for _file in files:
        text = load_file(_file)
        texts.update({_file: text})
    return texts


def clean_text(text: str) -> list:
    text = remove_punctuation(text)
    clean_text = text.replace("\n", "")
    text_list = clean_text.lower().split()
    return text_list


def get_cleaned_texts(files: list) -> dict:
    loaded_txts = load_all_txt_files(files)

    cleaned_texts_dict = {}
    for tname, text in loaded_txts.items():
        cleaned_text = clean_text(text)
        cleaned_texts_dict.update({tname: cleaned_text})
    return cleaned_texts_dict


def create_tokens_list(cleaned_texts: dict) -> list:
    texts_list = [text for tname, text in cleaned_texts.items()]
    
    tokens = set()
    for text in texts_list:
        filtered_text = set(text)  # filtruju při pomoci setu
        tokens.update(filtered_text)
    return sorted(tokens)


def vectorize(cleaned_texts: dict, global_vocabulary: list) -> dict:
    vectors = {}
    for tname, text in cleaned_texts.items():
        sent_vec = []
        for token in global_vocabulary:
            sent_vec.append(1 if token in text else 0)
        vectors.update({tname: sent_vec})
    return vectors


def save_result(vectorized_dict: dict, global_vocabulary: list, texts: dict):
    result = [{
        "Vectors": vectorized_dict,
        "Global Vocabulary": global_vocabulary,
        "Texts": texts
    }]

    with open(output_file, "w+", encoding="utf-8") as of:
        json.dump(result, of, ensure_ascii=False)


def folder_to_bow(folder) -> tuple:
    files = [str(_file) for _file in files_dir.glob("*.txt")]
    cleaned_texts = get_cleaned_texts(files)
    global_vocabulary = create_tokens_list(cleaned_texts)
    vectorized = vectorize(cleaned_texts, global_vocabulary)
    return cleaned_texts, global_vocabulary, vectorized


def main():
    br = 20*"_"
    cleaned_texts, global_vocabulary, vectorized = folder_to_bow(files_dir)
    print(f"Počet nahraných souborů: {len(cleaned_texts)}",
          f"Texty jsou načtené a zpracované!", br, sep="\n")
    print(f"Globální slovník byl vytvořen!",
          f"Počet tokenů ve slovníku: {len(global_vocabulary)}", br, sep="\n")
    save_result(vectorized, global_vocabulary, cleaned_texts)
    print(f"Data byla uložena do souboru {fname}")


if __name__ == "__main__":
    main()

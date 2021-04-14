import json
from pprint import pprint
from pathlib import Path
from utils import load_file, remove_punctuation


current_dir = Path.cwd()
files_dir = current_dir / "files_lesson6"
files = list(files_dir.glob("*.txt"))
files = [str(_file) for _file in files]


def load_all_txt_files() -> dict:
    texts = {}
    for _file in files:
        text = load_file(_file)
        texts.update({_file: text})
    return texts


def load_bow() -> tuple:
    with open("bag_of_words_lesson5.json", encoding="utf-8") as f:
        data = json.load(f)

    vectors_list = data[0]["Vectors"]
    global_vocabulary = data[1]["Global Vocabulary"]
    return vectors_list, global_vocabulary


if __name__ == "__main__":
    texts = load_all_txt_files()
    vectors_list, global_vocabulary = load_bow()
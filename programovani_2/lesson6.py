"""
Создайте функцию most_similar которая найдет из нее 
наиболее похожий текст для указанного «мешка слов», 
полученного с помощью задачи (5) и указанного имени файла.
"""
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


def main():
    texts = load_all_txt_files()
    vectors_list, global_vocabulary = load_bow()


if __name__ == "__main__":
    main()

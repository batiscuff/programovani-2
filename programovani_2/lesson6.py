"""
Создайте функцию most_similar которая найдет из нее 
наиболее похожий текст для указанного «мешка слов», 
полученного с помощью задачи (5) и указанного имени файла.
"""
import json
from pprint import pprint
from pathlib import Path
from utils import load_file, remove_punctuation


def main():
    current_dir = Path.cwd()
    files_dir = current_dir / "files_lesson6"


if __name__ == "__main__":
    main()

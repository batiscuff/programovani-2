from pathlib import Path
from lesson4 import cosine_distance
from lesson5 import folder_to_bow


def most_similar(bow, target_file_name):
    bow_target_file = bow.get(target_file_name)
    
    fname_dist_dict = {}
    for file_name, vectors in bow.items():
        cos_dist_result = cosine_distance(bow_target_file, vectors)
        fname_dist_dict.update({file_name: cos_dist_result})

    return min(fname_dist_dict, key=fname_dist_dict.get)


def main():
    current_dir = Path.cwd()
    files_dir = current_dir / "files_lesson6"
    target_file_name = str(files_dir / "muj_text2.txt")

    *_, bow_with_filenames = folder_to_bow(files_dir)
    most_similar_text = most_similar(bow_with_filenames, target_file_name)
    
    print(most_similar_text)


if __name__ == "__main__":
    main()

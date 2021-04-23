from pathlib import Path
from lesson5 import folder_to_bow


def most_similar(vectors: dict) -> str:
    """Dostaneme součet vektorů(vsums), abychom jej
    mohli použít k nalezení nejpodobnějšího textu"""
    
    vsums = {}
    for fname, vecs in vectors.items():
        vsums.update({fname: sum(vecs)})

    max_vsum = max([vsum for vsum in vsums.values()])
    for fname, vsum in vsums.items():
        if vsum == max_vsum:
            return fname


def main():
    current_dir = Path.cwd()
    files_dir = current_dir / "files_lesson6"
    cleaned_texts, global_vocabulary, vectorized = folder_to_bow(files_dir)
    print(most_similar(vectorized))


if __name__ == "__main__":
    main()

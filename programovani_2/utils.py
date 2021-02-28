from collections.abc import Iterable
from string import punctuation
from typing import Union


def load_file(f: Union[bytes, str]) -> str:
    """Načtěte soubor podle názvu a funkce vrátí f.read (),
    nebo načtěte objekt podobný souboru funkce také vrátí
    objekt pro čtení souboru"""

    if hasattr(f, "read"):
        return f.read()
    elif isinstance(f, str):
        with open(f) as infile:
            return infile.read()
    else:
        raise ValueError(
            "Musí být voláno s názvem souboru nebo objektem podobným souboru"
        )


def save_file(fname: str, data: Union[Iterable, str]) -> None:
    """Uloží řetězec nebo jiný iterovatelný objekt (list, set, tuple, atd.)
    do souboru"""
    with open(fname, "w+") as f:
        if isinstance(data, str):
            f.write(data)
        elif isinstance(data, Iterable):
            f.writelines(data)
        else:
            raise ValueError(
                "Uložít můžete jenom řetězec nebo jiný iterovatelný objekt (list, set, tuple, atd.)"
            )


def remove_punctuation(line: str) -> str:
    for symb in punctuation:
        line = line.replace(symb, "")
    return line

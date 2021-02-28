from math import sqrt
from icecream import ic


A = [0, 1, 1, 0]
B = [0, 0, 1, 1]


def dot(vectors1: list, vectors2: list) -> int:
    result = []
    for a, b in zip(vectors1, vectors2):  # ((a, b), (a, b), ...)
        ab = a * b
        result.append(ab)
    return sum(result)


def cosine_distance(sdv1: list, sdv2: list, vdot: int) -> float:
    result = sdv1 * sdv2  # sdv - sqrt dot vectors
    distance = 1 - vdot / result
    return round(distance, 2)


def main() -> None:
    vectors_dot = dot(A, B)
    sqrt_dot_vectors1 = sqrt(dot(A, A))
    sqrt_dot_vectors2 = sqrt(dot(B, B))
    cos_dist = cosine_distance(
        sqrt_dot_vectors1, sqrt_dot_vectors2, vectors_dot
    )
    ic(cos_dist)


if __name__ == "__main__":
    main()

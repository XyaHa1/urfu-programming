from typing import List


def check_winners(scores: List[int], student_score: int) -> None:
    """
    scores: set of student scores
    student_score: score's Stas
    """
    scores.sort(reverse=True)
    if student_score in scores[:3]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


if __name__ == "__main__":
    scores = [10, 70, 30, 60, 50, 60, 40, 80, 100, 90]
    student_score = 80
    check_winners(scores, student_score)
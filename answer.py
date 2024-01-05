"""this finds maax sum in traingle problem"""
from solver import solver


def answer():
    """By starting at the top of the triangle below and moving to
    adjacent numbers on the row below, the maximum total from top to bottom is 23"""

    triangle_str = """3
                    7 4
                   2 4 6
                  8 5 9 3"""

    return solver(triangle_str)


if __name__ == "__main__":
    print(answer())

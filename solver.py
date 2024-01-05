"""this finds maax sum in traingle problem"""


def solver(s: str):
    """By starting at the top of the triangle below and moving to
    adjacent numbers on the row below, the maximum total from top to bottom is 23"""

    lines = s.split("\n")
    two_d_list = [[int(num) for num in line.split()] for line in lines]
    for i in reversed(range(len(two_d_list) - 1)):
        for j in range(len(two_d_list[i])):
            two_d_list[i][j] += max(two_d_list[i + 1][j], two_d_list[i + 1][j + 1])

    max_total = two_d_list[0][0]

    return max_total


if __name__ == "__main__":
    TRIANGLE_STR = """3
                    7 4
                   2 4 6
                  8 5 9 3"""
    print(solver(TRIANGLE_STR))

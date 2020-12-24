"""Test for mypy."""


def main() -> None:
    num3 = add_nums(5, 3)
    print(num3)


def add_nums(num1: int, num2: int) -> int:
    return num1 + num2


if __name__ == "__main__":
    main()

"""Day 3 https://adventofcode.com/2025/day/3"""

from pathlib import Path


class Day3:
    """Day3 class"""
    def __init__(self):
        self.result = 0

        
    def parse(self, path: str | Path) -> None:
        """Parse the file.

        Args:
            path (str | Path): Path of the input file.
        """
        if not isinstance(path, Path):
            path = Path(path)

        buffer: str = ""

        with path.open("r", encoding="utf-8") as f:
            buffer = f.read()

        banks: list[str] = buffer.split("\n")

        for bank in banks:
            if len(bank) > 0:
                self.get_highest_number(bank)

    def get_highest_number(self, string: str) -> None:
        """Find the two highest digits.

        Args:
            string (str): Bank String.
        """
        bank: list[int] = [int(c) for c in string]
        highest: int = max(bank)
        second: int = 0
        highest_index: int = bank.index(highest)

        if highest_index != (len(bank) - 1):
            second = max(bank[highest_index + 1:])
        else:
            second = highest
            highest = max(bank[:highest_index])


        self.result += int(str(highest) + str(second))

class Day3_2(Day3):
    """Day3.2 class"""
    def __init__(self):
        super().__init__()

    def get_highest_number(self, string: str, n: int = 12) -> None:
        """Find the n highest digits.

        Args:
            string (str): Bank String.
        """
        digits = [int(c) for c in string]

        to_remove = len(digits) - n
        stack: list[int] = []

        for d in digits:
            while to_remove > 0 and stack and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        result_digits = stack[:n]

        self.result += int("".join(str(x) for x in result_digits))


if __name__ == "__main__":
    day3 = Day3()
    day3.parse(Path("./day3/input.txt"))
    print(day3.result)
    day3_2 = Day3_2()
    day3_2.parse(Path("./day3/input.txt"))
    print(day3_2.result)

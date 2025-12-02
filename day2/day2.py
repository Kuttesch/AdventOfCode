"""Day 2 https://adventofcode.com/2025/day/2"""

from pathlib import Path

class Day2:
    """Day2 class."""
    def __init__(self) -> None:
        """Day2 class."""
        self.result: int = 0

    def add(self, value: int) -> None:
        """Add value to self.result. (makes code comprehensable)

        Args:
            value (int): value to add
        """
        self.result += value

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

        ranges: list[str] = buffer.split(",")
        for range in ranges:
            self.check_range(range)

    def check_range(self, string: str) -> None:
        """Check range.

        Args:
            string (str): string to check. 
        """
        ranges: list[str] = string.split("-")
        for i in range(int(ranges[0]), int(ranges[1]) + 1):
            self.check_value(str(i))

    def check_value(self, string: str) -> None:
        """Check if the given string is one twice repeated sequence.

        Args:
            string (str): string to check.
        """
        length: int = len(string)
        if string[(int(length/2)):] == string[:(int(length/2))]:
            self.add(int(string))

if __name__ == "__main__":
    day2 = Day2()
    day2.parse(Path("./day2/input.txt"))
    print(day2.result)

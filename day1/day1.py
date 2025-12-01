"""Day 1 https://adventofcode.com/2025/day/1"""

from pathlib import Path


class Calc:
    """Calc class."""

    def __init__(self) -> None:
        """Calc class"""
        self.state: int = 50
        self.counter: int = 0

    def calculate(self, number: int) -> None:
        """Calculate while respecting overflow and counting "0"'s.

        Args:
            number (int): number to add (pos/neg).
        """
        step = 1 if number > 0 else -1

        for _ in range(abs(number)):
            self.state = (self.state + step) % 100
            if self.state == 0:
                self.counter += 1

    def add(self, number: int) -> None:
        """Add number to the state.

        Args:
            number (int): number to add.
        """
        self.calculate(number)

    def subtract(self, number: int) -> None:
        """Subtract number from the state.

        Args:
            number (int): number to subtract.
        """
        self.calculate(number.__neg__())


class Parser:
    """Parser Class."""

    def __init__(self, calc: Calc) -> None:
        """Parser Class."""
        self.calc = calc

    def parse(self, path: str | Path) -> None:
        """Parse the file and calculate.

        Args:
            path (str | Path): Path of the input file.
        """
        if not isinstance(path, Path):
            path = Path(path)

        buffer: str = ""

        with path.open("r", encoding="utf-8") as f:
            buffer = f.read()

        instructions: list[str] = buffer.split("\n")

        for i in instructions:
            self.parseln(i)

    def parseln(self, string: str) -> None:
        """Parse line and call calc class.

        Args:
            string (str): line to parse.

        Raises:
            ValueError: If invalid input.
        """
        if string.startswith("L"):
            self.calc.subtract(int(string[1:]))
        elif string.startswith("R"):
            self.calc.add(int(string[1:]))
        elif string == "":
            pass
        else:
            raise ValueError("Invalid Input")


if __name__ == "__main__":
    calc = Calc()
    parser = Parser(calc)
    parser.parse(Path("./day1/input.txt"))
    print(calc.counter)

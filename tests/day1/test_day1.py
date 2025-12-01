"""Tests for day 1."""

from pathlib import Path
from tempfile import TemporaryDirectory

from day1.day1 import Calc, Parser  # adjust import


def test_forward_wrap_hits_zero_once():
    c = Calc()
    c.state = 98
    c.add(5)  # 98 → 99 → 0 → 1 → 2 → 3
    assert c.state == 3
    assert c.counter == 1


def test_backward_wrap_hits_zero_once():
    c = Calc()
    c.state = 2
    c.subtract(5)  # 2 → 1 → 0 → 99 → 98 → 97
    assert c.state == 97
    assert c.counter == 1


def test_large_rotation_counts_all_passes():
    c = Calc()
    c.state = 50
    c.add(1000)  # 1000/100 = 10 full cycles → hits zero 10 times
    assert c.state == 50
    assert c.counter == 10


def test_full_example():
    """
    From the problem statement:

    Start at 50
      L68 → hits 0 once
      L30
      R48 → ends on 0
      L5
      R60 → hits 0 once
      L55 → ends on 0
      L1
      L99 → ends on 0
      R14
      L82 → hits 0 once

    Total = 6
    """

    c = Calc()

    # The exact instruction list from the puzzle
    instructions = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    p = Parser(c)
    for line in instructions:
        p.parseln(line)

    assert c.counter == 6


def test_parser_reads_file_and_updates_calc():
    with TemporaryDirectory() as td:
        path = Path(td) / "input.txt"
        path.write_text("R1\nR1\nL2\n", encoding="utf-8")

        c = Calc()
        p = Parser(c)
        p.parse(path)

        # Sequence: start 50 → 51 → 52 → 50 → does not cross zero
        assert c.state == 50
        assert c.counter == 0

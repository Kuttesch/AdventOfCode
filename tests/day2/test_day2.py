# test_day2.py

from pathlib import Path

from day2.day2 import Day2


def test_check_value_adds_double_patterns():
    day = Day2()

    # All of these are "some digits repeated twice"
    valid_ids = ["11", "22", "99", "1010", "123123"]
    for s in valid_ids:
        day.check_value(s)

    assert day.result == sum(int(s) for s in valid_ids)


def test_check_value_ignores_non_double_patterns():
    day = Day2()

    # Not "X repeated twice"
    invalid_ids = [
        "1",       # single digit
        "12",      # two different digits
        "1234",    # not XX
        "111",     # odd length
        "121",     # odd length, not XX
        "1231231", # not exact double
    ]

    for s in invalid_ids:
        day.check_value(s)

    assert day.result == 0


def test_check_range_example_11_22():
    day = Day2()
    day.check_range("11-22")
    # From the puzzle: 11 and 22 are the only invalid IDs
    assert day.result == 11 + 22


def test_parse_full_example(tmp_path: Path):
    # Single-line version of the example from the puzzle text
    content = (
        "11-22,"
        "95-115,"
        "998-1012,"
        "1188511880-1188511890,"
        "222220-222224,"
        "1698522-1698528,"
        "446443-446449,"
        "38593856-38593862,"
        "565653-565659,"
        "824824821-824824827,"
        "2121212118-2121212124"
    )

    input_file = tmp_path / "input.txt"
    input_file.write_text(content, encoding="utf-8")

    day = Day2()
    day.parse(input_file)

    # From the example: sum of all invalid IDs is 1227775554
    assert day.result == 1227775554

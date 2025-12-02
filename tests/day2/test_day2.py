from pathlib import Path

from day2.day2 import Day2, Day2_2, CheckResult


# -------------------------
# Day2  (exactly twice)
# -------------------------

def test_day2_exact_twice_valid_invalid_detection():
    d = Day2()

    # invalid for Day2 (X + X)
    invalid = ["11", "22", "99", "1010", "123123"]
    for s in invalid:
        assert d.check_value(s) == CheckResult.INVALID

    assert d.result == sum(int(s) for s in invalid)


def test_day2_exact_twice_rejects_non_double():
    d = Day2()

    valid = [
        "1",        # length 1
        "12",       # two different digits
        "1234",     # not XX
        "111",      # odd length
        "121",      # odd, not XX
        "585858",   # 3× repeated -> NOT counted in Day2
    ]

    for s in valid:
        assert d.check_value(s) == CheckResult.VALID

    assert d.result == 0


def test_day2_range_parsing():
    d = Day2()
    d.check_range("11-22")
    # only 11 and 22
    assert d.result == 11 + 22


def test_day2_full_example_part1(tmp_path: Path):
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

    file = tmp_path / "input_part1.txt"
    file.write_text(content, encoding="utf-8")

    d = Day2()
    d.parse(file)

    # Official AoC example for "exactly twice"
    assert d.result == 1227775554


# -------------------------
# Day2_2 (any repeating pattern, >= 2 times)
# -------------------------

def test_day2_2_detects_any_periodic_pattern():
    d = Day2_2()

    # All periodic in some block, repeated >= 2 times
    invalid = [
        "11",        # 1 × 2
        "22",        # 2 × 2
        "99",        # 9 × 2
        "1010",      # 10 × 2
        "123123",    # 123 × 2
        "585858",    # 58 × 3
        "7777777",   # 7 × 7
    ]

    for s in invalid:
        assert d.check_value(s) == CheckResult.INVALID

    assert d.result == sum(int(s) for s in invalid)


def test_day2_2_ignores_non_periodic():
    d = Day2_2()

    valid = [
        "1",
        "12",
        "1234",
        "1112",
        "123124",  # not purely periodic
    ]

    for s in valid:
        assert d.check_value(s) == CheckResult.VALID

    assert d.result == 0


def test_day2_2_full_example_part2(tmp_path: Path):
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

    file = tmp_path / "input_part2.txt"
    file.write_text(content, encoding="utf-8")

    d = Day2_2()
    d.parse(file)

    # Broader rule (any repetitions >= 2) -> higher sum.
    # This matches the result observed from the current implementation:
    assert d.result == 4174379265

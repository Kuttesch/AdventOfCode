"""Tests for day 3."""

from day3.day3 import Day3, Day3_2


# ------------------------------
# Helpers
# ------------------------------
def run_day3_on_strings(strings):
    d = Day3()
    for s in strings:
        d.get_highest_number(s)
    return d.result


def run_day3_2_on_strings(strings, n=12):
    d = Day3_2()
    for s in strings:
        d.get_highest_number(s, n=n)
    return d.result


# ------------------------------
# Day 3 Part 1 Tests
# ------------------------------
def test_day3_part1_single():
    # Example:
    # In "987654321111111", highest two digits in order = 98
    d = Day3()
    d.get_highest_number("987654321111111")
    assert d.result == 98


def test_day3_part1_multiple():
    strings = ["12345", "9081726354"]
    # For "12345": highest digit is last → result = 45
    # For "9081726354": result = 98
    expected = 45 + 98
    assert run_day3_on_strings(strings) == expected


def test_day3_part1_edge_all_same():
    # All digits equal → highest = second = same digit
    assert run_day3_on_strings(["111111"]) == 11


# ------------------------------
# Day 3 Part 2 Tests (12-digit max subsequence)
# ------------------------------
def test_day3_part2_examples():
    """
    From the problem statement:

    987654321111111 -> 987654321111
    811111111111119 -> 811111111119
    234234234234278 -> 434234234278
    818181911112111 -> 888911112111

    Sum = 3121910778619
    """
    strings = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    expected = (
        987654321111
        + 811111111119
        + 434234234278
        + 888911112111
    )
    assert run_day3_2_on_strings(strings, n=12) == expected


def test_day3_part2_exact_length():
    # If the string is exactly length n → return the string unchanged
    assert run_day3_2_on_strings(["123456789012"], n=12) == 123456789012


def test_day3_part2_monotonic():
    # Increasing string → best is the last n digits
    s = "012345678901234"
    # n = 12 → take the lexicographically largest subsequence preserving order
    expected = int("".join(s[-12:]))  # keep last 12 characters
    assert run_day3_2_on_strings([s], n=12) == expected


def test_day3_part2_all_same():
    assert run_day3_2_on_strings(["111111111111111"], n=12) == int("1" * 12)

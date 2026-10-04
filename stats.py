# SPDX-License-Identifier: MIT
# Copyright (c) 2026 license-demo contributors
"""A small command-line tool for descriptive statistics."""

import argparse
import math
import statistics


def summarize(values):
    """Return count, minimum, maximum, mean, and median for finite numbers."""
    numbers = list(values)
    if not numbers or not all(math.isfinite(value) for value in numbers):
        raise ValueError("Please provide at least one finite number.")
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("numbers", nargs="+", type=float)
    args = parser.parse_args()
    try:
        result = summarize(args.numbers)
    except ValueError as error:
        parser.error(str(error))
    for name, value in result.items():
        print(f"{name}: {value:g}")


if __name__ == "__main__":
    main()

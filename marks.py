#!/usr/bin/env python3
import argparse
import sys

def parse_args():
    p = argparse.ArgumentParser(description="Calculate total and average for 3 subjects")
    p.add_argument("m1", type=float, help="Marks for subject 1")
    p.add_argument("m2", type=float, help="Marks for subject 2")
    p.add_argument("m3", type=float, help="Marks for subject 3")
    p.add_argument("-t", "--threshold", type=float, default=120.0, help="Pass threshold for total (default: 120)")
    p.add_argument("-p", "--precision", type=int, default=2, help="Decimal places for average (default: 2)")
    return p.parse_args()

def validate_mark(name, v):
    if v < 0:
        raise ValueError(f"{name} must be non-negative")
    return v

def main():
    args = parse_args()
    try:
        m1 = validate_mark("m1", args.m1)
        m2 = validate_mark("m2", args.m2)
        m3 = validate_mark("m3", args.m3)
    except ValueError as e:
        print("Input error:", e, file=sys.stderr)
        sys.exit(2)

    total = m1 + m2 + m3
    avg = total / 3.0

    # print results
    print(f"Marks: {m1}, {m2}, {m3}")
    # show total as integer if it's an integer
    if abs(total - round(total)) < 1e-12:
        print(f"Total: {int(round(total))}")
    else:
        print(f"Total: {total}")

    print(f"Average: {avg:.{args.precision}f}")

    if total > args.threshold:
        print("Result: Pass")
    else:
        print("Result: Fail")

if __name__ == "__main__":
    main()
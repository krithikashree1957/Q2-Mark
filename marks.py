#!/usr/bin/env python3
import sys

def usage():
    return "Usage: marks.py <mark1> <mark2> <mark3>\nEach mark must be a number between 0 and 100."

def parse_mark(s):
    try:
        m = float(s)
    except ValueError:
        print("Error: marks must be numbers", file=sys.stderr)
        sys.exit(2)
    if m < 0 or m > 100:
        print("Error: each mark must be between 0 and 100", file=sys.stderr)
        sys.exit(2)
    return m

def main():
    if len(sys.argv) != 4:
        print(usage(), file=sys.stderr)
        sys.exit(2)

    m1 = parse_mark(sys.argv[1])
    m2 = parse_mark(sys.argv[2])
    m3 = parse_mark(sys.argv[3])

    total = m1 + m2 + m3
    average = total / 3.0

    passed = all(m >= 40.0 for m in (m1, m2, m3))
    status = "PASS" if passed else "FAIL"

    print(f"Marks: {m1:.2f}, {m2:.2f}, {m3:.2f}")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
    print(status)

    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
#!/usr/bin/python3
"""
This Module contains a script that reads stdin line
by line and computes metrics
"""
from sys import stdin
from typing import Dict


def print_logs(total_size: int, status_codes: Dict[str, int]) -> None:
    """Print the log metrics"""
    print(f"File size: {total_size}")
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f"{key}: {status_codes[key]}")


status_codes_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
total_size = 0

try:
    for count, line in enumerate(stdin, 1):
        parts = line.split()
        try:
            total_size += int(parts[-1])
        except Exception:
            pass
        try:
            status_code = parts[-2]
            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1
        except Exception:
            pass
        if count % 10 == 0:
            print_logs(total_size, status_codes_dict)


except KeyboardInterrupt:
    print_logs(total_size, status_codes_dict)

finally:
    print_logs(total_size, status_codes_dict)

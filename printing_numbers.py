"""
Python asyncio example. A solution to the following problem:

Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Miss" instead of the number and for the multiples of five print "Kiss".
For numbers which are multiples of both three and five print "MissKiss".
Each print must be asynchronous call print() function with a 50ms delay.
"""

import asyncio
import sys
from typing import Any, List

if sys.version_info < (3, 5):
    print("Warning: Code is written for Python3.5+. You may run into issues using a different version of python.")


def is_multiple_of_3(val: int) -> bool:
    return val % 3 == 0


def is_multiple_of_5(val: int) -> bool:
    return val % 5 == 0


def is_multiple_of_3_and_5(val: int) -> bool:
    return is_multiple_of_3(val) and is_multiple_of_5(val)


def build_print_list() -> List[str]:
    def convert_number(val: int) -> str:
        if is_multiple_of_3_and_5(val):
            return "MissKiss"
        if is_multiple_of_3(val):
            return "Miss"
        if is_multiple_of_5(val):
            return "Kiss"
        return str(val)

    return [convert_number(val) for val in range(1, 101)]


async def print_async(val: Any) -> None:
    await asyncio.sleep(.05)
    print(val)


event_loop = asyncio.get_event_loop()
print_futures = [print_async(val) for val in build_print_list()]
event_loop.run_until_complete(asyncio.wait(print_futures))
event_loop.close()

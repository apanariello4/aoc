import json
import re
from typing import Union

from utils import advent

advent.setup(2015, 12)


def find_numbers(string: str) -> int:
    return sum(map(int, re.findall(r'-?\d+', string)))


def find_numbers_no_red(data: Union[dict, list, int, str]) -> int:
    if isinstance(data, dict):
        return 0 if 'red' in data.values() else sum(find_numbers_no_red(v) for v in data.values())
    elif isinstance(data, list):
        return sum(find_numbers_no_red(v) for v in data)
    elif isinstance(data, int):
        return data
    return 0


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    json_data = json.loads(data)
    advent.print_answer(1, find_numbers(data))
    advent.print_answer(2, find_numbers_no_red(json_data))

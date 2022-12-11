import re
from itertools import product
from utils import advent

advent.setup(2015, 15)


def get_ingredients(data: str) -> list[dict]:
    ingredients = {}
    pattern = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
    for line in data:
        name, capacity, durability, flavor, texture, calories = pattern.match(line).groups()
        ingredients[name] = {"capacity": int(capacity), "durability": int(durability), "flavor": int(flavor), "texture": int(texture), "calories": int(calories)}
    return ingredients


def get_all_combinations(repetitions: list[dict], total: int) -> list[tuple]:
    return set((c for c in product(range(total + 1), repeat=repetitions) if sum(c) == total))


def get_score(ingredients: list[dict], combination: tuple) -> int:
    score = 1
    for property in ("capacity", "durability", "flavor", "texture"):
        score *= max(0, sum(ingredients[ingredient][property] * amount for ingredient, amount in zip(ingredients, combination)))
    return score


def get_max_score(ingredients: list[dict], combinations: list[tuple]) -> int:
    return max(get_score(ingredients, combination) for combination in combinations)


def get_max_score_calories(ingredients: list[dict], combinations: list[tuple]) -> int:
    return max(get_score(ingredients, combination) for combination in combinations if sum(ingredients[ingredient]["calories"] * amount for ingredient, amount in zip(ingredients, combination)) == 500)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()
    ingredients = get_ingredients(data)

    combinations = get_all_combinations(len(ingredients), 100)

    advent.print_answer(1, get_max_score(ingredients, combinations))
    advent.print_answer(2, get_max_score_calories(ingredients, combinations))

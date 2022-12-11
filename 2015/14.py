import re

from utils import advent

advent.setup(2015, 14)


class Reindeer:
    def __init__(self, speed: int, rest_time: int, running_time: int):
        self.speed = speed
        self.rest_time = rest_time
        self.running_time = running_time
        self.resting = False
        self.distance = 0
        self.remaining_rest = 0

    def tick(self) -> None:
        if self.resting:
            self.remaining_rest -= 1
            if self.remaining_rest == 0:
                self.resting = False
        else:
            self.distance += self.speed
            if (self.distance / self.speed) % self.running_time == 0:
                self.resting = True
                self.remaining_rest = self.rest_time


def get_reindeers(data: str) -> list[Reindeer]:
    reindeers = []
    pattern = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    for line in data:
        name, speed, running_time, rest_time = pattern.match(line).groups()
        reindeers.append(Reindeer(int(speed), int(rest_time), int(running_time)))
    return reindeers


def let_them_run(reindeers: list, time: int) -> tuple[int, int]:
    points = {reindeer: 0 for reindeer in reindeers}
    max_distance = 0
    for _ in range(time):
        for reindeer in reindeers:
            points[reindeer] += reindeer.distance == max_distance != 0
            reindeer.tick()
        max_distance = max(reindeer.distance for reindeer in reindeers)
    return max_distance, max(points.values())


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()
    reindeers = get_reindeers(data)

    p1, p2 = let_them_run(reindeers, 2503)
    advent.print_answer(1, p1)
    advent.print_answer(2, p2)

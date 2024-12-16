from typing import Optional


def neighbors4(displacement=1):
    deltas = [(0, displacement), (0, -displacement), (displacement, 0), (-displacement, 0)]
    yield from deltas

def neighbors8(displacement=1):
    deltas = [(0, displacement), (0, -displacement), (displacement, 0), (-displacement, 0), (displacement, displacement), (-displacement, -displacement), (displacement, -displacement), (-displacement, displacement)]
    yield from deltas

def neighbors4_coords(r, c, displacement=1):
    for dr, dc in neighbors4(displacement):
        yield r + dr, c + dc

def neighbors8_coords(r, c, displacement=1):
    for dr, dc in neighbors8(displacement):
        yield r + dr, c + dc

def in_bounds(r, c, H, W):
    return 0 <= r < H and 0 <= c < W

def find_in_grid(grid, target) -> Optional[tuple[int, int]]:
    for r, row in enumerate(grid):
        if target in row:
            return r, row.index(target)
    return None

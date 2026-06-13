from __future__ import annotations

import random

from PIL import Image, ImageDraw

from CaptchaGenerator.core import CaptchaConfig, ChallengeResult, Color, VisualChallenge
from CaptchaGenerator.exceptions import InvalidArgumentError

Cell = tuple[int, int]


class MazeCaptcha(VisualChallenge):
    """Generate a perfect maze and return its solution path."""

    def generate(
        self,
        *,
        name_export: str,
        path_export: str,
        columns: int = 10,
        rows: int = 7,
        answer_mode: str = "directions",
        config: CaptchaConfig | None = None,
    ) -> ChallengeResult:
        if columns < 3 or rows < 3:
            raise InvalidArgumentError("Maze must be at least 3x3.")
        if answer_mode not in {"directions", "path", "exit"}:
            raise InvalidArgumentError("answer_mode must be directions, path, or exit.")
        resolved = self._config(config)
        connections = carve_maze(columns, rows)
        start, end = (0, 0), (columns - 1, rows - 1)
        path = solve_maze(connections, start, end)
        directions = path_to_directions(path)
        image = Image.new("RGB", resolved.size, resolved.background_color)
        draw = ImageDraw.Draw(image)
        cell_width = (resolved.width - resolved.padding * 2) / columns
        cell_height = (resolved.height - resolved.padding * 2) / rows
        for row in range(rows):
            for column in range(columns):
                x1 = resolved.padding + column * cell_width
                y1 = resolved.padding + row * cell_height
                x2, y2 = x1 + cell_width, y1 + cell_height
                neighbors = connections[(column, row)]
                if (column, row - 1) not in neighbors:
                    draw.line((x1, y1, x2, y1), fill=resolved.foreground_color,
                              width=resolved.line_width)
                if (column - 1, row) not in neighbors:
                    draw.line((x1, y1, x1, y2), fill=resolved.foreground_color,
                              width=resolved.line_width)
                if (column, row + 1) not in neighbors:
                    draw.line((x1, y2, x2, y2), fill=resolved.foreground_color,
                              width=resolved.line_width)
                if (column + 1, row) not in neighbors:
                    draw.line((x2, y1, x2, y2), fill=resolved.foreground_color,
                              width=resolved.line_width)
        self._marker(draw, start, cell_width, cell_height, resolved, "S",
                     resolved.accent_colors[2])
        self._marker(draw, end, cell_width, cell_height, resolved, "E",
                     resolved.accent_colors[0])
        answer = {"directions": directions, "path": path, "exit": end}[answer_mode]
        return self._save(
            image, path_export=path_export, name_export=name_export,
            answer=answer, prompt="Find the path from S to E.",
            metadata={"columns": columns, "rows": rows,
                      "answer_mode": answer_mode, "path_length": len(path),
                      "start": start, "end": end},
            config=resolved,
        )

    @staticmethod
    def _marker(draw: ImageDraw.ImageDraw, cell: Cell, cell_width: float,
                cell_height: float, config: CaptchaConfig, label: str,
                color: Color) -> None:
        x = config.padding + (cell[0] + 0.5) * cell_width
        y = config.padding + (cell[1] + 0.5) * cell_height
        radius = min(cell_width, cell_height) * 0.25
        draw.ellipse((x - radius, y - radius, x + radius, y + radius),
                     fill=color)
        draw.text((x - 4, y - 7), label, fill="white")


def carve_maze(columns: int, rows: int) -> dict[Cell, set[Cell]]:
    graph: dict[Cell, set[Cell]] = {
        (x, y): set() for y in range(rows) for x in range(columns)
    }
    visited = {(0, 0)}
    stack = [(0, 0)]
    while stack:
        current = stack[-1]
        x, y = current
        candidates = [
            neighbor for neighbor in ((x + 1, y), (x - 1, y),
                                      (x, y + 1), (x, y - 1))
            if neighbor in graph and neighbor not in visited
        ]
        if not candidates:
            stack.pop()
            continue
        target = random.choice(candidates)
        graph[current].add(target)
        graph[target].add(current)
        visited.add(target)
        stack.append(target)
    return graph


def solve_maze(graph: dict[Cell, set[Cell]], start: Cell, end: Cell) -> list[Cell]:
    queue = [start]
    parent: dict[Cell, Cell | None] = {start: None}
    for node in queue:
        if node == end:
            break
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    path: list[Cell] = []
    cursor: Cell | None = end
    while cursor is not None:
        path.append(cursor)
        cursor = parent[cursor]
    return list(reversed(path))


def path_to_directions(path: list[Cell]) -> list[str]:
    names = {(1, 0): "right", (-1, 0): "left",
             (0, 1): "down", (0, -1): "up"}
    return [
        names[(next_cell[0] - cell[0], next_cell[1] - cell[1])]
        for cell, next_cell in zip(path, path[1:])
    ]

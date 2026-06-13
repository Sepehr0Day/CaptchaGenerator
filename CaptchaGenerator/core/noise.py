from __future__ import annotations

import random
from typing import TYPE_CHECKING

from CaptchaGenerator.core.colors import random_color

if TYPE_CHECKING:
    from PIL.ImageDraw import ImageDraw

NOISE_LINE_COUNT: int = 50
NOISE_SHAPE_COUNT: int = 29


def draw_circle(draw: ImageDraw, width: int, height: int) -> None:
    """Draw a random circle on the image.

    Args:
        draw: The PIL ImageDraw object.
        width: The width of the image.
        height: The height of the image.
    """
    circle_color = random_color()
    draw.ellipse([(0, 0), (width, height)], outline=circle_color)


def draw_rectangle(draw: ImageDraw, width: int, height: int) -> None:
    """Draw a random rectangle on the image.

    Args:
        draw: The PIL ImageDraw object.
        width: The width of the image.
        height: The height of the image.
    """
    rectangle_color = random_color()
    rectangle_width = random.randint(50, width)
    rectangle_height = random.randint(50, height)
    rectangle_left = (width - rectangle_width) // 2
    rectangle_top = (height - rectangle_height) // 2
    rectangle_right = rectangle_left + rectangle_width
    rectangle_bottom = rectangle_top + rectangle_height
    draw.rectangle(
        (rectangle_left, rectangle_top, rectangle_right, rectangle_bottom),
        outline=rectangle_color,
    )


def draw_square(draw: ImageDraw, width: int, height: int) -> None:
    """Draw a random square on the image.

    Args:
        draw: The PIL ImageDraw object.
        width: The width of the image.
        height: The height of the image.
    """
    square_color = random_color()
    square_size = random.randint(2, min(width, height))
    square_left = (width - square_size) // 2
    square_top = (height - square_size) // 2
    square_right = square_left + square_size
    square_bottom = square_top + square_size
    draw.rectangle(
        (square_left, square_top, square_right, square_bottom), outline=square_color
    )


def draw_triangle(draw: ImageDraw, width: int, height: int) -> None:
    """Draw a random triangle on the image.

    Args:
        draw: The PIL ImageDraw object.
        width: The width of the image.
        height: The height of the image.
    """
    triangle_color = random_color()
    triangle_size = random.randint(5, min(width, height))
    triangle_top = (height - triangle_size) // 2
    triangle_bottom = triangle_top + triangle_size
    triangle_left = (width - triangle_size) // 2
    triangle_right = triangle_left + triangle_size
    triangle_points = [
        (triangle_left, triangle_bottom),
        ((triangle_left + triangle_right) // 2, triangle_top),
        (triangle_right, triangle_bottom),
    ]
    draw.polygon(triangle_points, outline=triangle_color)


def draw_noise_lines(
    draw: ImageDraw, width: int, height: int, count: int = NOISE_LINE_COUNT
) -> None:
    """Draw random noise lines on the image.

    Args:
        draw: The PIL ImageDraw object.
        width: The width of the image.
        height: The height of the image.
        count: The number of lines to draw.
    """
    for _ in range(count):
        line_color = random_color()
        line_width = random.randint(15, 35)
        start_point = (random.randint(0, width), random.randint(0, height))
        end_point = (random.randint(0, width), random.randint(0, height))
        draw.line([start_point, end_point], fill=line_color, width=line_width)


def draw_noise_shapes(
    draw: ImageDraw, width: int, height: int, count: int = NOISE_SHAPE_COUNT
) -> None:
    """Draw random noise rectangles (scratches) on the image.

    Args:
        draw: The PIL ImageDraw object.
        width: The width of the image.
        height: The height of the image.
        count: The number of shapes to draw.
    """
    for _ in range(count):
        scratch_color = random_color()
        scratch_width = random.randint(15, 50)
        scratch_height = random.randint(50, 70)
        scratch_left = random.randint(0, width - scratch_width)
        scratch_top = random.randint(0, height - scratch_height)
        scratch_right = scratch_left + scratch_width
        scratch_bottom = scratch_top + scratch_height
        draw.rectangle(
            (scratch_left, scratch_top, scratch_right, scratch_bottom),
            outline=scratch_color,
        )


def draw_random_shape(draw: ImageDraw, width: int, height: int) -> None:
    """Draw one of each random shape (circle, rectangle, square, triangle).

    Args:
        draw: The PIL ImageDraw object.
        width: The width of the image.
        height: The height of the image.
    """
    draw_circle(draw, width, height)
    draw_rectangle(draw, width, height)
    draw_square(draw, width, height)
    draw_triangle(draw, width, height)

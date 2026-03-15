#!/usr/bin/env python3

"""Module for technical_assessments.hrt."""

import bisect

import unittest


def hollow_square(size):
    """Return a hollow square made of ``*`` characters."""
    if size <= 0:
        return None

    if size == 1:
        return ["*"]

    border = "*" * size
    middle = "*" + " " * (size - 2) + "*"

    return [border] + [middle for _ in range(size - 2)] + [border]


def bus_commute_round_trips(outbound, inbound, outbound_time, inbound_time, round_trips):
    """Return the earliest finish time after completing ``round_trips`` commutes."""
    current_time = 0

    while round_trips > 0:
        next_outbound_idx = bisect.bisect_left(outbound, current_time)
        if next_outbound_idx == len(outbound):
            return -1

        current_time = outbound[next_outbound_idx] + outbound_time

        next_inbound_idx = bisect.bisect_left(inbound, current_time)
        if next_inbound_idx == len(inbound):
            return -1

        current_time = inbound[next_inbound_idx] + inbound_time
        round_trips -= 1

    return current_time


def board_layout_validation(board_size, pieces):
    """Validate that piece placements and covered paths do not overlap."""
    occupied = set()

    def is_in_bounds(row, col):
        return 0 <= row < board_size and 0 <= col < board_size

    def mark_path(start, end, step):
        row, col = start
        row_step, col_step = step

        while True:
            if (row, col) in occupied:
                return False
            occupied.add((row, col))

            if (row, col) == end:
                break

            row += row_step
            col += col_step

        return True

    def validate_segment(start, end, expected_piece):
        row1, col1 = start
        row2, col2 = end

        if not (is_in_bounds(row1, col1) and is_in_bounds(row2, col2)):
            raise ValueError(f"{expected_piece} coordinates out of bounds")

        if expected_piece == "R":
            if row1 != row2 and col1 != col2:
                raise ValueError("Invalid rook segment")
            step = (
                0 if row1 == row2 else (1 if row2 > row1 else -1),
                0 if col1 == col2 else (1 if col2 > col1 else -1),
            )
        else:
            if abs(row1 - row2) != abs(col1 - col2):
                raise ValueError("Invalid bishop segment")
            step = (
                1 if row2 > row1 else -1,
                1 if col2 > col1 else -1,
            )

        return mark_path(start, end, step)

    def validate_rook(piece):
        if len(piece) != 5:
            raise ValueError("Invalid rook definition")

        _, row1, col1, row2, col2 = piece
        return validate_segment((row1, col1), (row2, col2), "R")

    def validate_bishop(piece):
        if len(piece) != 5:
            raise ValueError("Invalid bishop definition")

        _, row1, col1, row2, col2 = piece
        return validate_segment((row1, col1), (row2, col2), "B")

    def validate_knight(piece):
        if len(piece) != 3:
            raise ValueError("Invalid knight definition")

        _, row, col = piece

        if not is_in_bounds(row, col):
            raise ValueError("Knight coordinates out of bounds")

        if (row, col) in occupied:
            return False

        occupied.add((row, col))
        return True

    validators = {
        "R": validate_rook,
        "B": validate_bishop,
        "K": validate_knight,
    }

    for piece in pieces:
        kind = piece[0]

        validator = validators.get(kind)
        if validator is None:
            raise ValueError("Unknown piece type")

        if not validator(piece):
            return False

    return True


class TestSolution(unittest.TestCase):
    def test_hollow_square_returns_none_for_non_positive_size(self):
        self.assertIsNone(hollow_square(0))
        self.assertIsNone(hollow_square(-1))

    def test_hollow_square_with_size_one(self):
        self.assertListEqual(hollow_square(1), ["*"])

    def test_hollow_square_with_size_two(self):
        self.assertListEqual(hollow_square(2), ["**", "**"])

    def test_hollow_square_with_larger_size(self):
        self.assertListEqual(
            hollow_square(4),
            ["****", "*  *", "*  *", "****"],
        )

    def test_bus_commute_round_trips_returns_finish_time(self):
        self.assertEqual(
            bus_commute_round_trips([0, 10, 20], [5, 15, 25, 35], 5, 5, 2),
            20,
        )

    def test_bus_commute_round_trips_returns_negative_one_when_outbound_fails(self):
        self.assertEqual(
            bus_commute_round_trips([], [5, 15, 25], 5, 5, 1),
            -1,
        )

    def test_bus_commute_round_trips_returns_negative_one_when_inbound_fails(self):
        self.assertEqual(
            bus_commute_round_trips([3], [0, 1, 2], 10, 10, 1),
            -1,
        )

    def test_board_layout_validation_returns_true_for_non_overlapping_pieces(self):
        self.assertTrue(
            board_layout_validation(
                8,
                pieces=[
                    ("R", 0, 0, 0, 7),
                    ("B", 1, 1, 3, 3),
                    ("K", 7, 7),
                ],
            )
        )

    def test_board_layout_validation_returns_false_for_overlapping_paths(self):
        self.assertFalse(
            board_layout_validation(
                8,
                pieces=[
                    ("R", 0, 0, 0, 7),
                    ("B", 0, 7, 3, 4),
                ],
            )
        )

    def test_board_layout_validation_raises_for_invalid_rook_segment(self):
        with self.assertRaises(ValueError):
            board_layout_validation(8, [("R", 0, 0, 1, 2)])

    def test_board_layout_validation_raises_for_unknown_piece_type(self):
        with self.assertRaises(ValueError):
            board_layout_validation(8, [("Q", 0, 0)])

if __name__ == '__main__':
    unittest.main()

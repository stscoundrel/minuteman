from unittest import TestCase

from src.minuteman.parser import parse


class TestMinutemanCore(TestCase):
    def test_parses_time_transforms(self):
        test_cases = [
            (
                "5 minutes a day in 1 year in days",
                "1.2673611111111112 days",
            ),
            (
                "1 hour a week in a year in days",
                "2.1666666666666665 days",
            ),
            (
                "2 hours a week in 2 years in days",
                "8.666666666666666 days",
            ),
            (
                "8 hours a day in a year in months",
                "4.055555555555555 months",
            ),
            (
                "5 days a week in a decade in years",
                "7.123287671232877 years",
            ),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(parse(expression), expected)

    def test_parses_time_transforms_with_rounding(self):
        test_cases = [
            (
                "5 minutes a day in 1 year in days",
                2,
                "1.27 days",
            ),
            (
                "1 hour a week in a year in days",
                3,
                "2.167 days",
            ),
            (
                "2 hours a week in 2 years in days",
                1,
                "8.7 days",
            ),
            (
                "8 hours a day in a year in months",
                0,
                "4 months",
            ),
            (
                "5 days a week in a decade in years",
                666,
                "7.123287671232877 years",
            ),
        ]

        for expression, rounding_decimals, expected in test_cases:
            with self.subTest(
                expression=expression,
                rounding_decimals=rounding_decimals,
                expected=expected,
            ):
                self.assertEqual(parse(expression, rounding_decimals), expected)

from unittest import TestCase

from src.minuteman.core import (
    TimeExpression,
    TimeExpressionRequst,
    UnitOfTime,
    transform,
)


class TestMinutemanCore(TestCase):
    def test_parses_time_transforms(self):
        test_cases = [
            # 5 minutes a day in 1 year in days
            (
                (
                    TimeExpressionRequst(
                        original=TimeExpression(
                            amount=5,
                            unit=UnitOfTime.MINUTES,
                        ),
                        in_time=TimeExpression(amount=1, unit=UnitOfTime.DAYS),
                        comparison=TimeExpression(amount=1, unit=UnitOfTime.YEARS),
                    ),
                    UnitOfTime.DAYS,
                ),
                TimeExpression(amount=1.2673611111111112, unit=UnitOfTime.DAYS),
            ),
            # 1 hour a week in a year
            (
                (
                    TimeExpressionRequst(
                        original=TimeExpression(
                            amount=1,
                            unit=UnitOfTime.HOURS,
                        ),
                        in_time=TimeExpression(amount=1, unit=UnitOfTime.WEEKS),
                        comparison=TimeExpression(amount=1, unit=UnitOfTime.YEARS),
                    ),
                    UnitOfTime.DAYS,
                ),
                TimeExpression(amount=2.1666666666666665, unit=UnitOfTime.DAYS),
            ),
            # 2 hours a week in 2 years
            (
                (
                    TimeExpressionRequst(
                        original=TimeExpression(
                            amount=2,
                            unit=UnitOfTime.HOURS,
                        ),
                        in_time=TimeExpression(amount=1, unit=UnitOfTime.WEEKS),
                        comparison=TimeExpression(amount=2, unit=UnitOfTime.YEARS),
                    ),
                    UnitOfTime.DAYS,
                ),
                TimeExpression(amount=8.666666666666666, unit=UnitOfTime.DAYS),
            ),
            # 8 hours a day in a year in months
            (
                (
                    TimeExpressionRequst(
                        original=TimeExpression(
                            amount=8,
                            unit=UnitOfTime.HOURS,
                        ),
                        in_time=TimeExpression(amount=1, unit=UnitOfTime.DAYS),
                        comparison=TimeExpression(amount=1, unit=UnitOfTime.YEARS),
                    ),
                    UnitOfTime.MONTHS,
                ),
                TimeExpression(amount=4.055555555555555, unit=UnitOfTime.MONTHS),
            ),
            # 5 days a week in a decade in years
            (
                (
                    TimeExpressionRequst(
                        original=TimeExpression(
                            amount=5,
                            unit=UnitOfTime.DAYS,
                        ),
                        in_time=TimeExpression(amount=1, unit=UnitOfTime.WEEKS),
                        comparison=TimeExpression(amount=1, unit=UnitOfTime.DECADES),
                    ),
                    UnitOfTime.YEARS,
                ),
                TimeExpression(amount=7.123287671232877, unit=UnitOfTime.YEARS),
            ),
            # 3 months a year in 8 decades in years
            (
                (
                    TimeExpressionRequst(
                        original=TimeExpression(
                            amount=3,
                            unit=UnitOfTime.MONTHS,
                        ),
                        in_time=TimeExpression(amount=1, unit=UnitOfTime.YEARS),
                        comparison=TimeExpression(amount=8, unit=UnitOfTime.DECADES),
                    ),
                    UnitOfTime.YEARS,
                ),
                TimeExpression(amount=20.0, unit=UnitOfTime.YEARS),
            ),
        ]

        for args, expected in test_cases:
            with self.subTest(args=args, expected=expected):
                self.assertEqual(transform(*args), expected)

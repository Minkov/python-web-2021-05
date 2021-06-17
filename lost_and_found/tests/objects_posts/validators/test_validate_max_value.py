from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.validators import validate_max_value


class ValidateMaxValueTests(TestCase):
    def test_whenValueIsGreaterThanMax_expectToRaise(self):
        value = 5
        validate_func = validate_max_value(value - 1)
        with self.assertRaises(ValidationError) as context:
            validate_func(value)

        self.assertIsNotNone(context.exception)

    def test_whenValueIsLesserThanMax_expectToDoNothing(self):
        value = 5
        validate_func = validate_max_value(value + 1)
        validate_func(value)

    def test_whenValueIsEqualToMax_expectToDoNothing(self):
        value = 5
        validate_func = validate_max_value(value)
        validate_func(value)

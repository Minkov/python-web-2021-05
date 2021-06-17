from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.models import Object


class ObjectTests(TestCase):
    valid_name = 'Object 1'
    valid_image = 'http://image.com'
    valid_width = 500
    valid_height = 1
    valid_weight = 1.2

    def test_whenWidthIsLessThan3_expectToRaise(self):
        width = 2

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        with self.assertRaises(ValidationError) as context:
            obj.full_clean()
            obj.save()

        self.assertIsNotNone(context.exception)

    def test_whenWidthIsEqualTo3_expectSuccess(self):
        width = 3

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        obj.full_clean()
        obj.save()

    def test_whenWidthIsGreaterThan600_expectToRaise(self):
        width = 601

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        with self.assertRaises(ValidationError) as context:
            obj.full_clean()
            obj.save()

        self.assertIsNotNone(context.exception)

    def test_whenWidthIsEqualTo600_expectSuccess(self):
        width = 600

        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        obj.full_clean()
        obj.save()

    def test_whenWidthBetween3And600_expectSuccess(self):
        obj = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=self.valid_width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        obj.full_clean()
        obj.save()

from django.test import TestCase
from django.utils import timezone


from .models import Course ,Step

class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description = "Learn to write regular expression in Python"
        )
        now = timezone.now()

        self.assertLess(course.created_at , now)

class StepModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title = 'Python Testing',
            description = 'Learn to write tests in python'
        )

    def test_step_creation(self):
        step = Step.objects.create(
            title='Introduction to Docsets',
            description = 'Learn How to write tests in your docstrings',
            course = self.course
        )
        self.assertIn(step , self.course.step_set.all())

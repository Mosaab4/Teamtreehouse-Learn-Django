from django.core.urlresolvers import reverse
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

class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title = 'Python Testing',
            description = 'Learn to write tests in python'
        )
        self.course2 = Course.objects.create(
            title = 'New Course',
            description ='A new Course'
        )
        self.step = Step.objects.create(
            title = "introduction to doctests",
            description = "Learn to write tests in your docstrings.",
            course = self.course

        )
    def test_course_list_views(self):
        resp = self.client.get(reverse('courses:list'))
        
        self.assertEqual(resp.status_code , 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])

        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)

    def test_course_detail_views(self):
        resp = self.client.get(reverse(
            'courses:detail',
            kwargs = {
                'pk':self.course.pk
            }
        ))
        
        self.assertEqual(resp.status_code , 200)
        self.assertEqual(self.course , resp.context['course'])

    def test_step_detail_view(self):
        resp = self.client.get(reverse(
            'courses:step',
            kwargs = {
                'course_pk' : self.course.pk,
                'step_pk': self.step.pk
            }
        ))
        self.assertEqual(resp.status_code , 200)
        self.assertEqual(self.step , resp.context['step'])

        




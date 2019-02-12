from django.test import TestCase
from django.shortcuts import resolve_url as r
from emcomum.core.forms import IntroduceForm


class HomeTest(TestCase):
    def setUp(self):
        self.res = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.res, 'index.html')

    def test_form(self):
        """Html must contains input tags"""
        tags = (('<form', 1),
                ('<input', 7),
                ('<button', 1),
                ('<textarea', 1),
                ('type="text"', 3),
                ('type="email"', 3))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.res, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.res, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have contact form"""
        form = self.res.context['form']
        self.assertIsInstance(form, IntroduceForm)

    def test_form_has_fields(self):
        """Form must have fields"""
        form = self.res.context['form']
        self.assertSequenceEqual(['from_name', 'from_email',
                                  'person1_name', 'person1_email',
                                  'person2_name', 'person2_email',
                                  'message'], list(form.fields))

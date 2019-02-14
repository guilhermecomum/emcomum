from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from emcomum.core.forms import MeetingForm
from emcomum.core.models import Meeting


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
        self.assertIsInstance(form, MeetingForm)

    def test_form_has_fields(self):
        """Form must have fields"""
        form = self.res.context['form']
        self.assertSequenceEqual(['host_name', 'host_email',
                                  'guest1_name', 'guest1_email',
                                  'guest2_name', 'guest2_email',
                                  'message'], list(form.fields))


class MeetingFormPostTest(TestCase):
    def setUp(self):
        data = dict(host_name="Tom Jobim", host_email="tom.jobim@mpb.br",
                    guest1_name="Baden Powell", guest1_email='baden.powell@mpb.br',
                    guest2_name="Vincius de Moraes", guest2_email='vinicius.moraes@mpb.br',
                    message='Olá, tudo bom?')

        self.res = self.client.post('/', data)

    def test_post(self):
        """Valid POST should redirect to /obrigado"""
        self.assertEqual(302, self.res.status_code)

    def test_send_introduce_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_introduce_email_subject(self):
        email = mail.outbox[0]
        expect = 'Em Comum | Tom Jobim, te enviou uma mensagem'

        self.assertEqual(expect, email.subject)

    def test_introduce_email_from(self):
        email = mail.outbox[0]
        expect = 'em@comum.org'

        self.assertEqual(expect, email.from_email)

    def test_introduce_email_to(self):
        email = mail.outbox[0]
        expect = ['tom.jobim@mpb.br', 'baden.powell@mpb.br', 'vinicius.moraes@mpb.br']

        self.assertEqual(expect, email.to)

    def test_save_meeting(self):
        self.assertTrue(Meeting.objects.exists())


class MeetingFormInvalidPost(TestCase):
    def setUp(self):
        self.res = self.client.post('/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.res, 'index.html')

    def test_has_form(self):
        form = self.res.context['form']
        self.assertIsInstance(form, MeetingForm)

    def test_form_has_erros(self):
        form = self.res.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_meeting(self):
        self.assertFalse(Meeting.objects.exists())


class ThanksTest(TestCase):
    def setUp(self):
        self.res = self.client.get(r('thanks'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.res, 'thanks.html')


class AboutPageTest(TestCase):
    def setUp(self):
        self.res = self.client.get(r('about'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.res, 'about.html')

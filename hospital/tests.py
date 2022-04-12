from django.test import TestCase
from hospital.models import models.Model
from ..forms import SignUpForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['Firstname','username', 'Lastname', 'password',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
class DoctorSignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['Firstname','username', 'Lastname', 'department','password',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

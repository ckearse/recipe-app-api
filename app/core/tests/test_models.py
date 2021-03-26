from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test Creating a new user with an email is successfull"""
        email = 'test@test.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email of a new user is normalized"""

        email = 'test@Test1.Com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that creating a user with no email provided, raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new super user"""

        email = 'super@test.com'
        password = 'test123'
        user = get_user_model().objects.create_super_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.password, password)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

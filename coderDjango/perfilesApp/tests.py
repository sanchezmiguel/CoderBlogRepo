from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, CreatorProfile


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración de objetos de prueba una vez para el conjunto de pruebas
        user = User.objects.create(username='testuser')
        UserProfile.objects.create(user=user, first_name='John', last_name='Doe', email='john@example.com')

    def test_str_representation(self):
        user_profile = UserProfile.objects.get(id=1)
        expected_str = user_profile.user.username
        self.assertEqual(str(user_profile), expected_str)


class CreatorProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración de objetos de prueba una vez para el conjunto de pruebas
        CreatorProfile.objects.create(name='Test Creator', position='Developer', bio='Bio text',
                                      email='creator@example.com')

    def test_str_representation(self):
        creator_profile = CreatorProfile.objects.get(name='Test Creator')
        expected_str = creator_profile.name
        self.assertEqual(str(creator_profile), expected_str)

    def test_name_uniqueness(self):
        try:
            CreatorProfile.objects.create(name='Test Creator', position='Designer', bio='Another bio',
                                          email='another@example.com')
        except Exception as e:
            self.assertEqual(type(e),IntegrityError)

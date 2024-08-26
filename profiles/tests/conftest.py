# profiles/tests/conftest.py
import pytest
from django.contrib.auth.models import User
from profiles.models import Profile
from django.conf import settings


@pytest.fixture(autouse=True)
def override_settings_for_tests():
    settings.STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


@pytest.fixture
def new_user(db):
    """Fixture to create a new user."""
    return User.objects.create_user("testuser", "test@example.com", "testpass123")


@pytest.fixture
def new_profile(db, new_user):
    """Fixture to create a new profile linked to a user."""
    return Profile.objects.create(user=new_user, favorite_city="New York")


@pytest.fixture
def populate_profiles(db):
    """Fixture to create multiple user profiles for testing list views or multiple interactions."""
    users = [
        User.objects.create_user(
            username=f"user{i}", email=f"user{i}@example.com", password="testpass123"
        )
        for i in range(1, 4)
    ]
    return [
        Profile.objects.create(user=user, favorite_city=f"City {i}")
        for i, user in enumerate(users, start=1)
    ]

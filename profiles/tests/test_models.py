# profiles/tests/test_models.py
import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str():
    user = User.objects.create(username="testuser", password="12345")
    profile = Profile.objects.create(user=user, favorite_city="New York")
    assert str(profile) == "testuser"

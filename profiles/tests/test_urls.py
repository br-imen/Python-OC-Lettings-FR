# profiles/tests/test_urls.py
from django.urls import reverse, resolve
from profiles import views


def test_profiles_index_url():
    url = reverse("profiles:profiles_index")
    assert resolve(url).func == views.index


def test_profile_url():
    url = reverse("profiles:profile", kwargs={"username": "user1"})
    assert resolve(url).func == views.profile

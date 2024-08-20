# profiles/tests/test_views.py
import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profile_view(client, new_profile):
    response = client.get(
        reverse("profiles:profile", kwargs={"username": new_profile.user.username})
    )
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
    assert response.context["profile"] == new_profile


@pytest.mark.django_db
def test_profiles_index_view(client, populate_profiles):
    response = client.get(reverse("profiles:profiles_index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")
    assert len(response.context["profiles_list"]) == 3


@pytest.mark.django_db
def test_profile_view_not_found(client):
    response = client.get(reverse("profiles:profile", kwargs={"username": "nonexistent"}))
    assert response.status_code == 404

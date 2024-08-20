import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Letting


@pytest.mark.django_db
def test_index_view(client, create_address):
    # Use the create_address fixture to create addresses for Lettings
    addresses = [create_address() for _ in range(3)]
    _ = [
        Letting.objects.create(title=f"Sample Letting {i+1}", address=addr)
        for i, addr in enumerate(addresses)
    ]

    response = client.get(reverse("lettings:lettings_index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
    assert len(response.context["lettings_list"]) == 3


@pytest.mark.django_db
def test_letting_view(client, create_address):
    # Use the create_address fixture to create an address for the Letting
    address = create_address()
    letting = Letting.objects.create(title="Unique Letting", address=address)

    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
    assert response.context["title"] == letting.title


@pytest.mark.django_db
def test_letting_view_not_found(client):
    response = client.get(
        reverse("lettings:letting", args=[99999])
    )  # Assume ID 99999 does not exist
    assert response.status_code == 404

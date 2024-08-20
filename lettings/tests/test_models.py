import pytest
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_string_representation(address):
    assert str(address) == "123 Elm Street"


@pytest.mark.django_db
def test_letting_string_representation(address):
    letting = Letting.objects.create(title="Charming House", address=address)
    assert str(letting) == "Charming House"


@pytest.mark.django_db
def test_address_max_values():
    with pytest.raises(ValidationError):
        Address(
            number=10000,
            street="Baker Street",
            city="London",
            state="LN",
            zip_code=100000,
            country_iso_code="GBR",
        ).full_clean()


@pytest.mark.django_db
def test_address_min_length_validators():
    with pytest.raises(ValidationError):
        Address(
            number=123,
            street="Elm Street",
            city="Springwood",
            state="O",
            zip_code=45321,
            country_iso_code="US",
        ).full_clean()

import pytest
from lettings.models import Address


@pytest.fixture
def address():
    return Address.objects.create(
        number=123,
        street="Elm Street",
        city="Springwood",
        state="OH",
        zip_code=45321,
        country_iso_code="USA",
    )


@pytest.fixture
def create_address(db, address):
    def make_address():
        return Address.objects.create(
            number=123,
            street="Main Street",
            city="Anytown",
            state="CA",
            zip_code=12345,
            country_iso_code="USA",
        )

    return make_address

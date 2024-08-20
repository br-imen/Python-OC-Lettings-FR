import pytest
from django.urls import reverse, resolve
from lettings.views import index, letting


@pytest.mark.parametrize(
    "url_name, view_func",
    [
        ("lettings_index", index),
        ("letting", letting),
    ],
)
def test_url_resolves_to_correct_view(url_name, view_func):
    url = reverse(
        f"lettings:{url_name}", kwargs={"letting_id": 1} if url_name == "letting" else {}
    )
    assert resolve(url).func == view_func

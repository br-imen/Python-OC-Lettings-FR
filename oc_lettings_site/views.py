from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non
# id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra
# purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Renders the index.html template.
    Parameters:
    - request: The HTTP request object.
    Returns:
    - The rendered index.html template.
    """
    return render(request, "index.html")


def custom_404_view(request, exception):
    """
    Custom view for handling 404 errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered 404_error.html template with a 404 status code.
    """
    return render(request, "404_error.html", status=404)


def custom_500_view(request):
    """
    Custom view for handling 500 server errors.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 500_error.html template with a status code of 500.
    """
    return render(request, "500_error.html", status=500)

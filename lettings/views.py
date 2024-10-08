from django.shortcuts import get_object_or_404, render
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum,
# consectetur quis velit. Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et
# ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Renders the index page with a list of all lettings.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response containing the index page with the lettings list.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim,
# odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. Mauris condimentum auctor elementum.
# Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    View function for displaying a single letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to be displayed.

    Returns:
        HttpResponse: The HTTP response object containing the rendered letting template.
    """
    # Use get_object_or_404 to handle the DoesNotExist exception
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)

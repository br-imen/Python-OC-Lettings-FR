from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
]

# Custom error handlers
handler404 = "oc_lettings_site.views.custom_404_view"
handler500 = "oc_lettings_site.views.custom_500_view"

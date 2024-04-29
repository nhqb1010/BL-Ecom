from django.urls import path

from app.api.views import health_check

urlpatterns = [
    path("api/heath-check/", health_check, name="health_check")
]
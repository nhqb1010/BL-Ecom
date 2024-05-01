from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


# *** Health Check Tests ***
def test_health_check():
    client = APIClient()
    response = client.get(reverse("health_check"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"status": "ok"}
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .api.views import login_view, verify_token_view


urlpatterns = [
    path("api/auth/token/", login_view, name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/token/verify/", verify_token_view, name="token_verify"),
]

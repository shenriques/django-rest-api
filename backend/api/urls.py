from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token # endpoint to generate auth tokens
from . views import api_home

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', api_home),
    # obtain the token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # how you refresh tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # verify the access token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
from django.urls import path
from rest_framework import routers

from accounts.views import ResetPassword

router = routers.DefaultRouter()

urlpatterns = [
    path('reset-password/', ResetPassword.as_view(), name='resetpassword'),
]

urlpatterns += router.urls

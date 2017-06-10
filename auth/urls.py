
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from auth import views

urlpatterns = [
    url(r'^$', views.UserRegistrationView.as_view()),
    url(r'^auth-token/', obtain_jwt_token),
]
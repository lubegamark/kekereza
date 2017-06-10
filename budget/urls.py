from django.conf.urls import url

from budget import views

urlpatterns = [
    url(r'^(?P<id>[^/]+)/income/', views.UserIncomeListView.as_view()),
    url(r'^(?P<id>[^/]+)/expense/', views.UserExpenseListView.as_view()),
]

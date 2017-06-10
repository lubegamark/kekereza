from django.conf.urls import url

from budget import views

urlpatterns = [
    url(r'^income/', views.UserIncomeListView.as_view()),
    url(r'^expense/', views.UserExpenseListView.as_view()),
]

from rest_framework import generics

from budget.models import Income, Expense
from budget.serializers import IncomeSerializer, ExpenseSerializer


class UserIncomeListView(generics.ListCreateAPIView):
    serializer_class = IncomeSerializer

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)


class UserExpenseListView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)

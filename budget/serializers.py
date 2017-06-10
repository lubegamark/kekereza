from rest_framework import serializers

from budget.models import Income, Expense


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense

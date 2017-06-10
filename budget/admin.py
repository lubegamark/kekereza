from django.contrib import admin

# Register your models here.
from budget.models import Income, Expense

admin.site.register(Income)
admin.site.register(Expense)

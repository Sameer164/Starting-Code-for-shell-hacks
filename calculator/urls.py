from django.urls import path
from .views import home, BudgetCreate, BudgetUpdate, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name = "home"),
    path('create_budget', BudgetCreate.as_view(), name='budget-create'),
    path("update_budget/<int:pk>", BudgetUpdate.as_view(), name = 'budget-update'),
]

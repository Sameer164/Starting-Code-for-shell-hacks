from django.shortcuts import render
from .models import Budget
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView



from django.urls import reverse_lazy
from . import urls
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'calculator/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')



def home(request, *args, **kwargs):
    
    budgets = Budget.objects.all()[:5]
    context = {"budgets": budgets}
    return render(request, 'calculator/index.html', context)

class BudgetCreate(CreateView):
    model = Budget
    fields = ['user', 'total_income', 'student_debt', 'secondary_incomes', 'your_subscriptions']
    success_url = reverse_lazy('home')

class BudgetUpdate(UpdateView):
    model = Budget
    fields = ['user', 'total_income', 'student_debt', 'secondary_incomes', 'your_subscriptions']
    success_url = reverse_lazy('home')

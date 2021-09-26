from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    total_income = models.PositiveIntegerField(verbose_name="After Tax Total Income", help_text="Fixed Primary Income", default=0, validators=[MinValueValidator(0)])
    student_debt = models.PositiveIntegerField(verbose_name="Your student debt amount", default=0, validators=[MinValueValidator(0)])
    secondary_incomes = models.PositiveIntegerField(verbose_name="Secondary Incomes", default=0, validators=[MinValueValidator(0)], null = True, blank = True)
    your_subscriptions = models.PositiveIntegerField(verbose_name="Expenses on Subscriptions", default=0, validators=[MinValueValidator(0)], null = True, blank = True)
    budget = models.IntegerField(default = 0, null = True, blank = True)


    def save(self, *args, **kwargs):
        self.budget = self.total_income + self.secondary_incomes - (self.student_debt+self.your_subscriptions)
        super(Budget, self).save(*args, **kwargs)

    def __str__(self):
        return "Budget: " + str(self.budget)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = true)
    monthly_budget = models.IntegerField(default = 0, null = True, blank = True)
    product_price = modles.PositiveIntegerField(verbose_name = "Price of your Purchase", default = 0, validators = [MinValueValidator(0)])
    need_or_not = models.BooleanField(verbose_name = "Necessity or not?")
    
    def calculate(self):
        self.monthly_budget = self.budget / 30
        if self.need_or_not = True:
            self.monthly_budget = (self.budget / 30) * 0.5
            return self.monthly_bidget
        else:
            self.monthly_budget =(self.budget / 30) * 0.3
            return self.monthly_budget
    
    def __str__(self):
        return "Price: " + str(self.product_price) + " vs. Budget: " + str(self.monthly_budget)
        

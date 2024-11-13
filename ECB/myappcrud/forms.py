from django import forms
from .models import Customer, Consumption, Bill

# -------------------- Customer Form --------------------

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstName', 'lastName', 'address', 'email', 'phoneNumber']

# -------------------- Consumption Form --------------------

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        fields = ['readingDateFrom', 'readingDateTo', 'customerID']

# -------------------- Bill Form --------------------

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['billDate', 'totalAmount', 'dueDate', 'customerID', 'tariffID']

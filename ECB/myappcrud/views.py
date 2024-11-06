from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Consumption, Bill
from .forms import CustomerForm, ConsumptionForm, BillForm

# -------------------- Customer Views --------------------

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'myappcrud/customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'myappcrud/customer_form.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'myappcrud/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'myappcrud/customer_confirm_delete.html', {'customer': customer})

# -------------------- Consumption Views --------------------

def consumption_list(request):
    consumptions = Consumption.objects.all()
    return render(request, 'myappcrud/consumption_list.html', {'consumptions': consumptions})

def consumption_create(request):
    if request.method == 'POST':
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consumption_list')
    else:
        form = ConsumptionForm()
    return render(request, 'myappcrud/consumption_form.html', {'form': form})

def consumption_update(request, pk):
    consumption = get_object_or_404(Consumption, pk=pk)
    if request.method == 'POST':
        form = ConsumptionForm(request.POST, instance=consumption)
        if form.is_valid():
            form.save()
            return redirect('consumption_list')
    else:
        form = ConsumptionForm(instance=consumption)
    return render(request, 'myappcrud/consumption_form.html', {'form': form})

def consumption_delete(request, pk):
    consumption = get_object_or_404(Consumption, pk=pk)
    if request.method == 'POST':
        consumption.delete()
        return redirect('consumption_list')
    return render(request, 'myappcrud/consumption_confirm_delete.html', {'consumption': consumption})

# -------------------- Bill Views --------------------

def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'myappcrud/bill_list.html', {'bills': bills})

def bill_create(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'myappcrud/bill_form.html', {'form': form})

def bill_update(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm(instance=bill)
    return render(request, 'myappcrud/bill_form.html', {'form': form})

def bill_delete(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill_list')
    return render(request, 'myappcrud/bill_confirm_delete.html', {'bill': bill})

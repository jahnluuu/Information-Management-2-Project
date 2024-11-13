from django.urls import path
from . import views

urlpatterns = [
    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/update/<int:pk>/', views.customer_update, name='customer_update'),
    path('customers/delete/<int:pk>/', views.customer_delete, name='customer_delete'),

    # Consumption URLs
    path('consumptions/', views.consumption_list, name='consumption_list'),
    path('consumptions/create/', views.consumption_create, name='consumption_create'),
    path('consumptions/update/<int:pk>/', views.consumption_update, name='consumption_update'),
    path('consumptions/delete/<int:pk>/', views.consumption_delete, name='consumption_delete'),

    # Bill URLs
    path('bills/', views.bill_list, name='bill_list'),
    path('bills/create/', views.bill_create, name='bill_create'),
    path('bills/update/<int:pk>/', views.bill_update, name='bill_update'),
    path('bills/delete/<int:pk>/', views.bill_delete, name='bill_delete'),
]

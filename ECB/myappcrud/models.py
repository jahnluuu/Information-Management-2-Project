from django.db import models

class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Consumption(models.Model):
    consumptionID = models.AutoField(primary_key=True)
    readingDateFrom = models.DateField()
    readingDateTo = models.DateField()
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consumption {self.consumptionID} for {self.customerID}"

class Bill(models.Model):
    billID = models.AutoField(primary_key=True)
    billDate = models.DateField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    dueDate = models.DateField()
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Assuming there's a Tariff model you will link to later
    tariffID = models.IntegerField()  

    def __str__(self):
        return f"Bill {self.billID} for {self.customerID}"

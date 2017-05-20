from django.db import models

from  django.contrib.auth.models import User

from apps.tools.models import Folder

from apps.tools.models import Busines


# Create your models here.

# Model Table accounts
class Account(models.Model):
    id_acn = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    accounts_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    primary = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)


class Customer(models.Model):
    id_cut = models.AutoField(primary_key=True)
    business = models.ForeignKey(Busines, on_delete=models.CASCADE)  # Field name made lowercase.
    users = models.ForeignKey(User,  on_delete=models.CASCADE)  # Field name made lowercase.
    folders = models.ForeignKey(Folder,  on_delete=models.CASCADE)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    no_social = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    deactivated = models.BooleanField(default=False)
    date_deactivated = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Employee(models.Model):
    id_emp = models.AutoField(primary_key=True)
    business = models.ForeignKey(Busines,  on_delete=models.CASCADE)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    comercial_name = models.CharField(max_length=45, blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    social_no = models.CharField(max_length=20, blank=True, null=True)
    date_admis = models.DateField(blank=True, null=True)
    phone = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    type_salary = models.CharField(max_length=20, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    deactivated = models.BooleanField(default=False)
    date_deactivated = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Invoice(models.Model):
    id_inv = models.AutoField(primary_key=True)
    customers = models.ForeignKey(Customer,  on_delete=models.CASCADE)  # Field name made lowercase.
    business = models.ForeignKey(Busines,  on_delete=models.CASCADE)  # Field name made lowercase.
    users = models.ForeignKey(User,  on_delete=models.CASCADE)  # Field name made lowercase.
    serial = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    waytopay = models.CharField(max_length=20, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paid = models.BooleanField(default=True)
    prefix = models.CharField(max_length=4, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.serial)


class Item(models.Model):
    id_ite = models.AutoField(primary_key=True)
    accounts = models.ForeignKey(Account,  on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Receipt(models.Model):
    id_rec = models.AutoField(primary_key=True)
    accounts = models.ForeignKey(Account,  on_delete=models.CASCADE)  # Field name made lowercase.
    business = models.ForeignKey(Busines,  on_delete=models.CASCADE)  # Field name made lowercase.
    users = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    serial = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=45)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    weytopay = models.CharField(max_length=20)
    paid = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)

class Payment(models.Model):
    id_sal = models.AutoField(primary_key=True)
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE)  # Field name made lowercase.
    users = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    employees = models.ForeignKey(Employee,  on_delete=models.CASCADE)  # Field name made lowercase.
    start_date_sal = models.DateField(blank=True, null=True)
    end_date_sal = models.DateField(blank=True, null=True)
    serial_sal = models.CharField(max_length=20, blank=True, null=True)
    discount_sal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    value_sal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Fee(models.Model):
    id_fee = models.AutoField(primary_key=True)
    accounts = models.ForeignKey(Account,  on_delete=models.CASCADE)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.description)


class InvoicesHasItem(models.Model):
    id_ind = models.AutoField(primary_key=True)
    invoices = models.ForeignKey(Invoice, on_delete=models.CASCADE)  # Field name made lowercase.
    items = models.ForeignKey(Item, on_delete=models.CASCADE)  # Field name made lowercase.
    quantity_ind = models.IntegerField(blank=True, null=True)
    value_ind = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class AccountDescrip(models.Model):
    id_acd = models.AutoField(primary_key=True)
    document = models.ForeignKey(InvoicesHasItem, on_delete=models.CASCADE)
    users = models.ForeignKey(User,  on_delete=models.CASCADE)  # Field name made lowercase.
    accounts = models.ForeignKey(Account,  on_delete=models.CASCADE)  # Field name made lowercase.
    date = models.DateField(auto_now_add=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)



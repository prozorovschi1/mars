from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Device(models.Model):
    """Model for the device"""

    class Meta:
        db_table = 'device'
        verbose_name = 'Disponible device'
        verbose_name_plural = 'Disponible devices'

    manufacturer = models.CharField(max_length=100, verbose_name='Producator')
    model = models.CharField(max_length=100, verbose_name='Model')

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Customer(models.Model):
    """Utilizatorul care a facut comanda"""

    class Meta:
        db_table = 'customers'
        verbose_name = 'Client'
        verbose_name_plural = 'Clienti'

    customer_name = models.CharField(max_length=255, verbose_name='Nume')
    customer_address = models.CharField(max_length=255, verbose_name='Adresa')
    customer_city = models.CharField(max_length=100, verbose_name='Oras')

    def __str__(self):
        return self.customer_name


class DeviceInField(models.Model):
    """Asociere între un dispozitiv și un client"""

    class Meta:
        db_table = 'device_in_field'
        verbose_name = 'Device in field'
        verbose_name_plural = 'Devices in field'

    serial_number = models.CharField(max_length=100, verbose_name='Serial number', unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Customer', related_name="devices")
    device = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name='Device', related_name="instances")
    owner = models.CharField(max_length=255, verbose_name='Owner')

    def __str__(self):
        return f"{self.serial_number} - {self.device.manufacturer} {self.device.model}"


class Order(models.Model):
    """Descrierea comenzii"""

    class Meta:
        db_table = 'orders'
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comenzi'

    STATUS_CHOICES = [
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
        ('Need info', 'Need info'),
        ('Open', 'Open'),
    ]

    device = models.ForeignKey(DeviceInField, verbose_name='Device', on_delete=models.RESTRICT, related_name="orders")
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.RESTRICT, related_name="orders")
    order_description = models.TextField(verbose_name='Order description')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Created at')
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name='Completed at')
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Order status')

    def save(self, *args, **kwargs):
        if self.order_status == 'Completed' and not self.completed_at:
            self.completed_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.order_status}"

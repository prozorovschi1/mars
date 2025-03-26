import os
import django
import random
from faker import Faker

# ✅ Setează manual fișierul de configurare Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mars_service.settings')  # Schimbă 'mars_service' cu numele proiectului tău

# ✅ Inițializează Django
django.setup()

# Acum putem importa modelele după configurarea Django
from orders_app.models import Device, Customer, DeviceInField, Order  # Asigură-te că numele aplicației este corect

fake = Faker()

# Funcție pentru crearea dispozitivelor
def create_devices(n=5):
    devices = []
    for _ in range(n):
        device = Device(
            manufacturer=fake.company(),
            model=fake.word()
        )
        device.save()
        devices.append(device)
    return devices

# Funcție pentru crearea clienților
def create_customers(n=5):
    customers = []
    for _ in range(n):
        customer = Customer(
            customer_name=fake.name(),
            customer_address=fake.address(),
            customer_city=fake.city()
        )
        customer.save()
        customers.append(customer)
    return customers

# Funcția principală care populează baza de date
def populate():
    print("Populare bazei de date...")
    devices = create_devices(10)
    customers = create_customers(10)
    print("✅ Populare completă!")

# Execută scriptul
if __name__ == "__main__":
    populate()

############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """
# Clear any existing data to avoid duplicate entries
Product.objects.all().delete()

# Insert sample products into the database
Product.objects.create(upc="1234", name="Red Apple", price=0.99)
Product.objects.create(upc="5678", name="Banana", price=0.79)
Product.objects.create(upc="4321", name="Orange Juice", price=3.49)
Product.objects.create(upc="8765", name="Milk", price=2.29)
Product.objects.create(upc="1937", name="Loaf of Bread", price=2.99)

# Print confirmation and product list
print("Product database populated successfully!\n")
for p in Product.objects.all():
    print(f"UPC: {p.upc}\tName: {p.name}\tPrice: ${p.price}")
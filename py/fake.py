import json
from faker import Faker
import _mysql_connector

# Initialize Faker
faker = Faker()

# Specify the number of data sets
num_sets = 500

# Generate the data
data = []
for _ in range(num_sets):
    record = {
        "business_id": faker.uuid4(),
        "business_name": faker.company(),
        "business_type": faker.random_element(["Retail", "Restaurant", "Service", "Tech"]),
        "location": faker.city(),
        "owner_name": faker.name(),
        "transaction_id": faker.uuid4(),
        "transaction_date": faker.date_this_year(),
        "transaction_amount": round(faker.random_number(digits=4) / 100, 2),
        "category": faker.random_element(["Rent", "Utilities", "Inventory", "Marketing", "Payroll"]),
        "payment_method": faker.random_element(["Credit Card", "Cash", "Bank Transfer"]),
        "vendor_name": faker.company(),
        "vendor_location": faker.city()
    }
    data.append(record)

# Print the data
print(data)




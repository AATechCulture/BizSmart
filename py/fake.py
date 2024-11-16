import os
import json;
from faker import Faker;
import teradatasql
from dotenv import load_dotenv

load_dotenv()


# Initialize Faker
faker = Faker()

# Specify the number of data sets
num_sets = 500


HOST =  os.getenv("HOST")
USER =  os.getenv("USER")
PASS =  os.getenv("PASS")

db = teradatasql.connect(host=HOST,user = USER, password = PASS)          # Connects python code to teradata database

curse = db.cursor()                                                       # Create cursor object from the database connection

curse.execute(f"""
              CREATE TABLE {USER}.BusinessData1(
              business_id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
              business_name VARCHAR(255), 
              business_type VARCHAR(255), 
              location VARCHAR(255), 
              owner_name VARCHAR(255), 
              transaction_date TIMESTAMP, 
              transaction_amount FLOAT(4), 
              category VARCHAR(255), 
              paymentDesc VARCHAR(255), 
              vendor_name VARCHAR(255)


              ) PRIMARY INDEX (business_id)
              
              """
              )



# Generate the data
data = [4]
for _ in range(num_sets):
    business_name = faker.company()
    business_type = faker.random_element(["Retail", "Restaurant", "Service", "Tech"])
    location = faker.city()
    paymentDesc = ""
    owner_name = faker.name()
    transaction_date = faker.date_this_year()
    transaction_amount = round(faker.random_number(digits=4) / 100, 2)
    category = faker.random_element(["Rent", "Utilities", "Inventory", "Marketing", "Payroll"])
    payment_method = faker.random_element(["Credit Card", "Cash", "Bank Transfer"])
    vendor_name = faker.company()
    query = f"INSERT INTO {USER}.BusinessData1 (business_name, business_type, location, owner_name, transaction_date, transaction_amount, category, paymentDesc, vendor_name) VALUES (?,?,?,?,?,?,?,?,?)"
    values = (business_name, business_type, location, owner_name, transaction_date, transaction_amount, category, paymentDesc, vendor_name)
    curse.execute(query, values)

# Print the data
print(data)

db.commit()
db.close()









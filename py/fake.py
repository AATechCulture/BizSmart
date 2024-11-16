import json;
from faker import Faker;
import teradatasql

# Initialize Faker
faker = Faker()

# Specify the number of data sets
num_sets = 500


HOST = "hackathonfakerfile-mwc2k52q3qz68tzk.env.clearscape.teradata.com"  # URL where database is hosted  
USER = "demo_user"                                                        # User on the database we're using
PASS = "HackathonTSU2024#"                                                # Password for database

db = teradatasql.connect(host=HOST,user = USER, password = PASS)          # Connects python code to teradata database

<<<<<<< HEAD
curse = db.cursor()
 
=======
curse = db.cursor()                                                       # Create cursor object from the database connection
>>>>>>> e2bf9b3191d35056e122bafbc2e61429c2f887f8

curse.execute(f"""
              CREATE TABLE {USER}.TSikk(
              business_id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
              business_name VARCHAR(255), 
              business_type VARCHAR(255), 
              location VARCHAR(255), 
              owner_name VARCHAR(255), 
              transaction_date TIMESTAMP, 
              transaction_amount FLOAT(4), 
              category VARCHAR(255), 
              payment_method VARCHAR(255), 
              vendor_name VARCHAR(255), 
              vendor_location VARCHAR(255)

              ) PRIMARY INDEX (business_id)
              
              """
              )



# Generate the data
data = [4]
for _ in range(num_sets):
    business_name = faker.company()
    business_type = faker.random_element(["Retail", "Restaurant", "Service", "Tech"])
    location = faker.city()
    owner_name = faker.name()
    transaction_date = faker.date_this_year()
    transaction_amount = round(faker.random_number(digits=4) / 100, 2)
    category = faker.random_element(["Rent", "Utilities", "Inventory", "Marketing", "Payroll"])
    payment_method = faker.random_element(["Credit Card", "Cash", "Bank Transfer"])
    vendor_name = faker.company()
    vendor_location = faker.city()
    query = f"INSERT INTO {USER}.TSikk (business_name, business_type, location, owner_name, transaction_date, transaction_amount, category, payment_method, vendor_name, vendor_location) VALUES (?,?,?,?,?,?,?,?,?,?)"
    values = (business_name, business_type, location, owner_name, transaction_date, transaction_amount, category, payment_method, vendor_name, vendor_location)
    curse.execute(query, values)

# Print the data
print(data)

db.commit()
db.close()









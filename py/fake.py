import json;
from faker import Faker;
import teradatasql

# Initialize Faker
faker = Faker()

# Specify the number of data sets
num_sets = 500


HOST = "hackathonfakerfile-mwc2k52q3qz68tzk.env.clearscape.teradata.com"
USER = "demo_user"
PASS = "HackathonTSU2024#"

db = teradatasql.connect(host=HOST,user = USER, password = PASS)

curse = db.cursor()


curse.execute("""
              CREATE SET TABLE {USER}.Transactionals(
              business_id INTEGER,
              business_name VARCHAR(255), business_type VARCHAR(255), 
              location VARCHAR(255), owner_name VARCHAR(255), 
              transaction_date TIMESTAMP, 
              transaction_amount FLOAT(4), 
              category VARCHAR(255), 
              payment_method VARCHAR(255), 
              vendor_name VARCHAR(255), 
              vendor_location VARCHAR(255),
              UNIQUE PRIMARY INDEX(business_id)

              )
              
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
        query = "INSERT INTO {USER}.Transactionals (business_name, business_type, location, owner_name, transaction_date, transaction_amount, category, payment_method, vendor_name, vendor_location) VALUES (?,?,?,?,?,?,?,?,?,?)"
        values = (business_name, business_type, location, owner_name, transaction_date, transaction_amount, category, payment_method, vendor_name, vendor_location)
        curse.executemany(query, values)

# Print the data
print(data)

db.commit()
db.close()
curse.close()








import teradatasql

DB_URL = ""                                 #Add Host
USER = ""                                   #Add Username
PASS = ""                                   #Add Password

try:
    # Establish a connection to the Teradata database
    with teradatasql.connect(host=DB_URL, user=USER, password=PASS) as con:
        # Create a cursor to execute queries
        with con.cursor() as cur:
            try:
                # Creating the table SampleEmployee
           
                
                print(f"Sample table {USER}.SampleEmployee created.")

                # Adding sample data into SampleEmployee table
                cur.execute (f"INSERT INTO {USER}.SampleEmployee VALUES (1, 'Richard Hendricks','CEO')")
                cur.execute (f"INSERT INTO {USER}.SampleEmployee VALUES (2, 'Jared Dunn','CFO')")
                cur.execute (f"INSERT INTO {USER}.SampleEmployee VALUES (3, 'Jian Yang','Intern')")

                print(f"Sample data added to table {USER}.SampleEmployee.")

                # Execute the SELECT query to get the results from SampleEmployee table 
                cur.execute(f"SELECT * FROM {USER}.SampleEmployee")

                # Extract data from the result set and print it
                for row in cur:
                    print(f"Associate ID: {row[0]}, Associate_Name: {row[1]}, Job_Title:{row[2]}")

                

            except teradatasql.DatabaseError as db_err:
                # Handle any errors that occur during query execution
                print("Error while executing the query:", db_err)

except teradatasql.DatabaseError as db_err:
    # Handle any errors that occur during the database connection
    print("Error while connecting to the Teradata database:", db_err)

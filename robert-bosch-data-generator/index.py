from faker import Faker
import pandas as pd
import random

# Initialize Faker and seed for reproducibility
fake = Faker()
Faker.seed(0)

# Generate 120k records for each of the 10 companies
num_records = 120000
num_companies = 10

data = []
for _ in range(num_records * num_companies):
    company_name = 'Robert Bosch Ghana Limited'
    name = fake.name()
    address = [ 'Greater Accra Region', 'Ashanti Region', 'Western Region', 'Eastern Region', 'Central Region' , 'Volta Region',
    'Northern Region', 'Upper East Region', 'Upper West Region', 'Bono Region', 'Ahafo Region', 'Bono East Region', 'Savannah Region',
    'North East Region', 'Oti Region', 'Western North Region']
    transaction_activity = ['auto parts & accessories', 'eBike systems', 'motor vehicle technology', 'household appliances',
    'security systems', 'solar inverters', 'packaging technology', 'industry solutions', 'business process management solutions']
    customer_preference = ['website', 'facebook', 'linkedin', 'youtube', 'x', 'instagram']
    communication_method = ['email', 'phone']

    data.append({
        'Company': company_name,
        'Name': name,
        'Address': random.choice(address),
        'Transaction Activity': random.choice(transaction_activity),
        'Customer Preference': random.choice(customer_preference),
        'Communication Method': random.choice(communication_method)
    })

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('robert_bosch_company_data.csv', index=False)



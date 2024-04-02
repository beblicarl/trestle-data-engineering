from faker import Faker
import pandas as pd
import random

fake = Faker()

# Generate 120k records
num_records = 120000

data = []
for _ in range(num_records):
    company_name = 'Robert Bosch Ghana Limited'
    name = fake.name()
    phone = fake.phone_number()
    email = fake.email()
    address = ['Greater Accra Region', 'Ashanti Region', 'Western Region', 'Eastern Region', 'Central Region', 'Volta Region',
               'Northern Region', 'Upper East Region', 'Upper West Region', 'Bono Region', 'Ahafo Region', 'Bono East Region',
               'Savannah Region', 'North East Region', 'Oti Region', 'Western North Region']
    branch = 'Airport Residential Area'
    service_product = ['auto parts & accessories', 'eBike systems', 'motor vehicle technology', 'household appliances',
                            'security systems', 'solar inverters', 'packaging technology', 'industry solutions',
                            'business process management solutions']
    transaction_activity = fake.random_int(min=1, max=9999)
    customer_preference = ['website', 'facebook', 'linkedin', 'youtube', 'x', 'instagram']
    communication_method = ['email', 'phone']

    data.append({
        'Company': company_name,
        'Name': name,
        'Phone Number': phone,
        'Email Address' : email,
        'Address': random.choice(address),
        'Branch' : branch,
        'Services / Products': random.choice(service_product),
        'Transaction Activity': transaction_activity,
        'Customer Preference': random.choice(customer_preference),
        'Communication Method': random.choice(communication_method),
        
    })

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('robert_bosch_company_data.csv', index=False, header=True)

import pandas as pd
import random
import datetime

# Create sample data for 50 e-commerce customers
data = {
    'Customer ID': [f'CUST{str(i).zfill(4)}' for i in range(1, 51)],
    'Customer Name': [f'Customer_{i}' for i in range(1, 51)],
    'Email': [f'customer{i}@example.com' for i in range(1, 51)],
    'Phone': [f'+1-800-{random.randint(100,999)}-{random.randint(1000,9999)}' for _ in range(50)],
    'Country': [random.choice(['USA', 'Canada', 'UK', 'Germany', 'Australia']) for _ in range(50)],
    'City': [random.choice(['New York', 'Toronto', 'London', 'Berlin', 'Sydney']) for _ in range(50)],
    'Sign-up Date': [datetime.date(2020, 1, 1) + datetime.timedelta(days=random.randint(0, 1000)) for _ in range(50)],
    'Total Orders': [random.randint(1, 20) for _ in range(50)],
    'Total Spend ($)': [round(random.uniform(100.0, 5000.0), 2) for _ in range(50)],
    'Last Order Date': [datetime.date(2023, 1, 1) + datetime.timedelta(days=random.randint(0, 365)) for _ in range(50)],
    'Last Order Amount ($)': [round(random.uniform(10.0, 500.0), 2) for _ in range(50)],
    'Loyalty Tier': [random.choice(['Bronze', 'Silver', 'Gold', 'Platinum']) for _ in range(50)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file with corrected file path
file_path = r'C:\Users\rushi\Documents\Yuga\ecommerce_customers.xlsx'
df.to_excel(file_path, index=False)

file_path

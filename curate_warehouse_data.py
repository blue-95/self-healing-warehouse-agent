import pandas as pd
from faker import Faker
import random

# Initialize Faker and load your downloaded data
fake = Faker()
df = pd.read_csv("warehouse_messy_data.csv")

def curate_and_contaminate(df, num_synthetic_rows=150):
    # 1. Anonymize Supplier Names using Faker
    df['Supplier'] = [fake.company() for _ in range(len(df))]
    
    # 2. Add Synthetic "New" Rows to show scalability
    new_rows = []
    for i in range(num_synthetic_rows):
        new_rows.append({
            "Product ID": fake.unique.random_int(min=5000, max=9999),
            "Product Name": f"synthetic {fake.word()}",
            "Category": random.choice(['ELECTRONICS', 'CLOTHING', 'TOYS']),
            "Warehouse": f"Warehouse {random.randint(1, 5)}",
            "Location": f"Aisle {random.randint(1, 10)}",
            "Quantity": random.randint(10, 500),
            "Price": round(random.uniform(5.0, 500.0), 2),
            "Supplier": fake.company(),
            "Status": random.choice(['In Stock', 'Out of Stock']),
            "Last Restocked": fake.date_this_year().strftime("%d/%m/%Y")
        })
    
    # Combine original and synthetic data
    combined_df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)

    # 3. Contaminate for the "Self-Healing" Agent (Logic Check)
    # Example: Create an outlier where Quantity is negative (Impossible)
    for _ in range(10):
        idx = random.randint(0, len(combined_df) - 1)
        combined_df.at[idx, 'Quantity'] = -99 
        
    return combined_df

# Run curation
print("Starting curation...")
final_df = curate_and_contaminate(df, num_synthetic_rows=150)

# FORCE A NEW FILE NAME to verify it worked
output_file = "warehouse_FINAL_WITH_ERRORS.csv"
final_df.to_csv(output_file, index=False)

print(f"✅ SUCCESS! Total rows: {len(final_df)}")
print(f"✅ File saved as: {output_file}")
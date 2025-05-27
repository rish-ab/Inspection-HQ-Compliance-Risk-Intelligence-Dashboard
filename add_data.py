import os
import pandas as pd
import random
from faker import Faker

# Create folder if it doesn't exist
os.makedirs("Data", exist_ok=True)

fake = Faker()
regs = ['GDPR', 'NIST', 'CMMC']
severity = ['Low', 'Medium', 'High']
types = ['Access Violation', 'Data Leak', 'Policy Breach', 'Login Failure', 'Unauthorized Device']

data = [{
    'log_id': i,
    'system_name': f"System_{random.randint(1,5)}",
    'regulation': random.choice(regs),
    'severity': random.choice(severity),
    'event_type': random.choice(types),
    'timestamp': fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
    'resolved': random.choice(['Yes', 'No'])
} for i in range(1, 5001)]

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("Data/mock_compliance_logs.csv", index=False)

print("✅ Mock compliance logs saved successfully!")

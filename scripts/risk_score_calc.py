import pandas as pd

# Load your data
df = pd.read_csv("Data/mock_compliance_logs.csv")

# Map severity to numeric scores
severity_map = {'Low': 1, 'Medium': 2, 'High': 3}
df['risk_value'] = df['severity'].map(severity_map)

# Group by system and regulation
risk_summary = df.groupby(['system_name', 'regulation']).agg(
    total_logs=('log_id', 'count'),
    unresolved_issues=('resolved', lambda x: (x == 'No').sum()),
    total_risk_score=('risk_value', 'sum')
).reset_index()

# Save to new CSV
risk_summary.to_csv("Data/compliance_risk_summary.csv", index=False)
print("✅ Compliance risk summary created!")

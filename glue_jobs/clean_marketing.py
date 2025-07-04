import pandas as pd
import os
from datetime import datetime, timedelta
import random

# Paths
input_path = os.path.join('..', 'data', 'marketing', 'marketing.csv')
output_path = os.path.join('..', 'data', 'marketing', 'marketing_cleaned.csv')

# Load dataset
df = pd.read_csv('../data/marketing/marketing.csv', sep='\t')
df.columns = df.columns.str.strip()
df.head()


# Keep only relevant columns
campaign_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
df = df[['ID'] + campaign_cols]

# Melt into long format
df_long = df.melt(id_vars='ID', value_vars=campaign_cols,
                  var_name='campaign_id', value_name='click')

# Rename columns
df_long = df_long.rename(columns={
    'ID': 'customer_id'
})

# Set channel (we'll assume "email" for now)
df_long['channel'] = 'email'

# Generate random timestamps
def random_timestamp():
    base = datetime(2024, 12, 1)
    offset = timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    return (base + offset).isoformat()

df_long['timestamp'] = df_long['customer_id'].apply(lambda x: random_timestamp())

# Reorder columns
df_long = df_long[['campaign_id', 'customer_id', 'channel', 'click', 'timestamp']]

# Save
df_long.to_csv(output_path, index=False)

print("marketing_cleaned.csv saved at:", output_path)

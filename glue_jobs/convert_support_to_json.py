import pandas as pd
import json
import random
import os

# Define input and output paths
input_path = os.path.join('..', 'data', 'support', 'support.csv')
output_path = os.path.join('..', 'data', 'support', 'support_tickets.json')

# Load the support dataset
df = pd.read_csv(input_path)

# Filter only inbound tweets (customer messages)
df = df[df['inbound'] == True]

# Create a list of support ticket dictionaries
tickets = []
for _, row in df.iterrows():
    ticket = {
        "ticket_id": str(row['tweet_id']),
        "customer_id": str(row['author_id']),
        "issue": row['text'],
        "status": random.choice(["open", "resolved"]),
        "created_at": row['created_at']
    }
    tickets.append(ticket)

# Save the list as a JSON file
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(tickets, f, indent=2)

print("support_tickets.json saved at:", output_path)

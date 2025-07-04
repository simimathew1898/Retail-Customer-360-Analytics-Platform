import pandas as pd
import os

# Define paths
input_path = os.path.join('..', 'data', 'orders', 'orders.csv')
output_path = os.path.join('..', 'data', 'orders', 'orders_cleaned.csv')

# Load raw orders CSV
df = pd.read_csv(input_path, encoding='ISO-8859-1')

# Drop rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Filter out negative or zero quantity/price
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Create total_amount column
df['total_amount'] = df['Quantity'] * df['UnitPrice']

# Rename and select required columns
df_cleaned = df.rename(columns={
    'InvoiceNo': 'order_id',
    'CustomerID': 'customer_id',
    'InvoiceDate': 'order_date',
    'StockCode': 'product_id',
    'Quantity': 'quantity'
})[['order_id', 'customer_id', 'order_date', 'total_amount', 'product_id', 'quantity']]

# Convert customer_id to string
df_cleaned['customer_id'] = df_cleaned['customer_id'].astype(str)

# Save cleaned file
df_cleaned.to_csv(output_path, index=False)

print("Cleaned orders file saved to:", output_path)

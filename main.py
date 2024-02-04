import pandas as pd
from datetime import datetime

def read_orders_csv(file_path):
    try:
        orders_df = pd.read_csv(file_path)
        return orders_df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def compute_total_revenue_by_month(orders_df):
    orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
    orders_df['month'] = orders_df['order_date'].dt.to_period('M')
    revenue_by_month = orders_df.groupby('month')['product_price'].sum()
    return revenue_by_month

def compute_total_revenue_by_product(orders_df):
    revenue_by_product = orders_df.groupby('product_name')['product_price'].sum()
    return revenue_by_product

def compute_total_revenue_by_customer(orders_df):
    revenue_by_customer = orders_df.groupby('customer_id')['product_price'].sum()
    return revenue_by_customer

def identify_top_customers(orders_df, n=10):
    top_customers = orders_df.groupby('customer_id')['product_price'].sum().nlargest(n)
    return top_customers

if __name__ == "__main__":
    file_path = "orders.csv"
    
    orders_df = read_orders_csv(file_path)
    
    if orders_df is not None:
        # Task 1: Compute total revenue by month
        total_revenue_by_month = compute_total_revenue_by_month(orders_df)
        print("Total Revenue by Month:")
        print(total_revenue_by_month)
        
        # Task 2: Compute total revenue by product
        total_revenue_by_product = compute_total_revenue_by_product(orders_df)
        print("\nTotal Revenue by Product:")
        print(total_revenue_by_product)
        
        # Task 3: Compute total revenue by customer
        total_revenue_by_customer = compute_total_revenue_by_customer(orders_df)
        print("\nTotal Revenue by Customer:")
        print(total_revenue_by_customer)
        
        # Task 4: Identify top 10 customers by revenue
        top_customers = identify_top_customers(orders_df)
        print("\nTop 10 Customers by Revenue:")
        print(top_customers)

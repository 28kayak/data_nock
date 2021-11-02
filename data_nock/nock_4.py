"""[Join Master Data]
Make one big table based on all data from customer_master and item_master

1. what is the common data we can use to join -> customer_id and item_id 
2. what data we want to add -> all fields from customer_master.csv and item_master.csv
"""
import pandas as pd
# read data from CSV files
item_master = pd.read_csv("./data/item_master.csv")
customer_master = pd.read_csv("./data/customer_master.csv")
transaction_1 = pd.read_csv("./data/transaction_1.csv")
transaction_detail_1 = pd.read_csv("./data/transaction_detail_1.csv")

# join data same as the nock_3.py
join_data = pd.merge(
    transaction_detail_1, 
    transaction_1[["transaction_id", "payment_date", "customer_id"]],
    on="transaction_id", 
    how="left")

join_data = pd.merge(join_data, customer_master, on="customer_id", how="left")

join_data = pd.merge(join_data, item_master, on="item_id", how="left")

df = pd.DataFrame(join_data)
# show all top 5 data
print(join_data.head())

# show 3 columns with top 5 data 
print(join_data[["customer_name", "customer_id", "birth"]].head())

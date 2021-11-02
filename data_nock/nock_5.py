"""[pick necessary columns]
create a revenue data based on the csvs
revenue = quantity * item_price 
"""


import pandas as pd 
# read data from csv
item_master = pd.read_csv("./data/item_master.csv")
customer_master = pd.read_csv("./data/customer_master.csv")
transaction_1 = pd.read_csv("./data/transaction_1.csv")
transaction_detail_1 = pd.read_csv("./data/transaction_detail_1.csv")


join_data = pd.merge(
    transaction_detail_1,
    transaction_1[["transaction_id", "payment_date", "customer_id"]],
    on="transaction_id",
    how="left"
)

join_data = pd.merge(join_data, customer_master, on="customer_id", how="left")
join_data = pd.merge(join_data, item_master, on="item_id", how="left")

# create price column and insert results of multiplication 
join_data["price"] = join_data["quantity"] * join_data["item_price"]

print(join_data[["price", "quantity", "item_price"]].head())

# nock_6
print("Sum of data : " + str(join_data["price"].sum()))

print("transaction price sum : " + str( join_data["price"].sum()))
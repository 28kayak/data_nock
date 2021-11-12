"""[各種統計量を把握する]
"""
import pandas as pd

# read data from csv files 
item_master = pd.read_csv("./data/item_master.csv")
customer_master = pd.read_csv("./data/customer_master.csv")
transaction_1 = pd.read_csv("./data/transaction_1.csv")
transaction_2 = pd.read_csv("./data/transaction_2.csv")
transaction_detail_1 = pd.read_csv("./data/transaction_detail_1.csv")
transaction_detail_2 = pd.read_csv("./data/transaction_detail_2.csv")

#Union transaction
transaction = pd.concat([transaction_1, transaction_2],ignore_index=True)
#Union transaction_detail
transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)

# join data 
join_data = pd.merge(
    transaction_detail,
    transaction[["transaction_id", "payment_date", "customer_id"]],
    on="transaction_id",
    how="left"
)

join_data = pd.merge(join_data, customer_master, on="customer_id", how="left")
join_data = pd.merge(join_data, item_master, on="item_id", how="left")

# calculate revenue 
join_data["price"] = join_data["quantity"] * join_data["item_price"]

print(join_data.isnull().sum())

"""
isnull() returns missing value with boolean. 
isnull().sum() returns total number of missing (True) for specific columns
"""
print(join_data.describe())

"""[Result of decribe function]
        detail_id     quantity          age     item_price          price
count  7144.000000  7144.000000  7144.000000    7144.000000    7144.000000
mean   3571.500000     1.199888    50.265677  121698.628219  135937.150056
std    2062.439494     0.513647    17.190314   64571.311830   68511.453297
min       0.000000     1.000000    20.000000   50000.000000   50000.000000
25%    1785.750000     1.000000    36.000000   50000.000000   85000.000000
50%    3571.500000     1.000000    50.000000  102500.000000  120000.000000
75%    5357.250000     1.000000    65.000000  187500.000000  210000.000000
max    7143.000000     4.000000    80.000000  210000.000000  420000.000000
"""


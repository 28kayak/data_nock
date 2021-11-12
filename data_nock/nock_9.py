"""[Monthly Data]
"""
import pandas as pd
import matplotlib.pyplot as plt

# read data from csv files 
item_master = pd.read_csv("./data/item_master.csv")
customer_master = pd.read_csv("./data/customer_master.csv")
transaction_1 = pd.read_csv("./data/transaction_1.csv")
transaction_2 = pd.read_csv("./data/transaction_2.csv")
transaction_detail_1 = pd.read_csv("./data/transaction_detail_1.csv")
transaction_detail_2 = pd.read_csv("./data/transaction_detail_2.csv")

# union transaction data
transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
# union transaction detail
transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)

# join data
join_data = pd.merge(
    transaction_detail,
    transaction[["transaction_id", "payment_date", "customer_id"]],
    on="transaction_id",
    how="left"
)
join_data = pd.merge(
    join_data, 
    customer_master,
    on="customer_id",
    how="left"
)
join_data = pd.merge(
    join_data,
    item_master,
    on="item_id",
    how="left"
)
# create price data
join_data["price"] = join_data["quantity"] * join_data["item_price"]

# nock_8 change date type of payment_date
join_data["payment_date"] = pd.to_datetime(join_data["payment_date"])
join_data["payment_month"] = join_data["payment_date"].dt.strftime("%Y%m")

print(join_data[["payment_date", "payment_month", "customer_name"]].head())
#print(join_data.dtypes)
print(join_data.head())

#月別・商品別でデータを集計する。
grouped = join_data.groupby(["payment_month", "item_name"]).sum()[["price","quantity"]]
print(grouped)

join_data1 =pd.pivot_table(
    join_data, 
    index="item_name", 
    columns="payment_month", 
    values=["price", "quantity"], 
    aggfunc="sum"
)
print(join_data1)
graph_data = pd.pivot_table(
    join_data,
    index="payment_month",
    columns="item_name",
    values="price",
    aggfunc="sum" 
)

#可視化する
"""[summary]
in order to visualize, we need to import mathplotlib
"""
plt.plot(list(graph_data.index), graph_data['PC-A'], label="PC-A")
plt.plot(list(graph_data.index), graph_data["PC-B"], label="PC-B")
plt.plot(list(graph_data.index), graph_data["PC-C"], label="PC-C")
plt.plot(list(graph_data.index), graph_data["PC-D"], label="PC-D")
plt.plot(list(graph_data.index), graph_data["PC-E"], label="PC-E")
plt.legend()
#plt.show()
plt.savefig('../generated/1-14.png')
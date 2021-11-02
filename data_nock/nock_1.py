# Let's read data 
import pandas as pd
# Read customer_master.csv file
customer_master = pd.read_csv('./data/customer_master.csv')
# read the first 5 lines of csv
print(customer_master.head()) 

# Read item_master.csv file
item_master = pd.read_csv('./data/item_master.csv')
print(item_master.head())

# Read transaction_1.csv file
transaction_1 = pd.read_csv('./data/transaction_1.csv')
print(transaction_1.head())

# Read trasaction_detail_1.csv file
transaction_detail_1 = pd.read_csv('./data/transaction_detail_1.csv')
print(transaction_detail_1.head())
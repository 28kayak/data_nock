# join data 
"""[JOIN Data]
when join two sets of data, need to consider about 
main data and key to be used for join.

main data in this case will be: data_nock/data/transaction_detail_1.csv 
because this file contains the most details 

next to think about is: 
1. what is the common data we can use to join -> transaction_id 
2. what data we want to add -> payment_date, customer_id
"""
import pandas as pd
   

# read transaction_1.csv file
transaction_1 = pd.read_csv('./data/transaction_1.csv')
# read transaction_detail_1.csv file
transaction_detail_1 = pd.read_csv('./data/transaction_detail_1.csv')

join_data = pd.merge(
    transaction_detail_1, 
    transaction_1[["transaction_id", "payment_date", "customer_id"]], 
    on="transaction_id", 
    how="left")

data = join_data.head()
print(data)

"""[result]
detail_id transaction_id item_id  quantity         payment_date customer_id
0          0    T0000000113    S005         1  2019-02-01 01:36:57    PL563502
1          1    T0000000114    S001         1  2019-02-01 01:37:23    HD678019
2          2    T0000000115    S003         1  2019-02-01 02:34:19    HD298120
3          3    T0000000116    S005         1  2019-02-01 02:47:23    IK452215
4          4    T0000000117    S002         2  2019-02-01 04:33:46    PL542865
"""

print(len(transaction_detail_1))
print(len(transaction_1))
print(len(join_data))
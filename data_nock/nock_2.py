# Union on Data 
import pandas as pd
import nock_1

transaction_2 = pd.read_csv('./data/transaction_2.csv')
transaction = pd.concat([nock_1.transaction_1, transaction_2], ignore_index=True)
print(len(nock_1.transaction_1))
print(len(transaction_2))
print(len(transaction)) #print number of rows in transaction
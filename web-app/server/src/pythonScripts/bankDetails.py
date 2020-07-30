#!/usr/bin/env python
# coding: utf-8

# In[ ]:
print("File generated")
import sys
import json
import csv
import pandas as pd
import numpy as np


# In[ ]:


def json2csv(json_name, csv_name, key):
    with open(json_name) as json_file:
        data = json.load(json_file)
    transaction_data = data[key]
    data_file = open(csv_name, 'w') 
    csv_writer = csv.writer(data_file)
    count = 0
    for tran in transaction_data:
        if count == 0: 
            # Writing headers of CSV file 
            header = tran.keys()
            csv_writer.writerow(header) 
            count += 1
        # Writing data of CSV file 
        csv_writer.writerow(tran.values())
    data_file.close() 


# In[ ]:


json2csv('allfidata_fish.json', 'bank_details.csv', 'data')


# In[ ]:


df = pd.read_csv('bank_details.csv')


# In[ ]:


df


# In[ ]:


df["Summary"]


# In[ ]:


type(df.at[0,"Summary"])


# In[ ]:


df.at[1,"Summary"]


# In[ ]:


# li = df["Summary"][0].split(',')
# li


# In[ ]:


# stri = df.at[0,"Summary"].replace("{","")
# stri = stri.replace("'",'')


# In[ ]:


#stri


# In[ ]:


#li = stri.split(',')
#li


# In[ ]:


#balance = li[0].split(':')


# In[ ]:


# current_balance = balance[1].strip()
# bank_name = df.at[0,"bank"]
# bank_name


# In[ ]:


df.shape


# In[ ]:


bank_name, account_type, account_no, balances = [], [], [], []
for i in range(df.shape[0]):
    type_ac = ''
    li = ''
    sti1 = ''
    type_account1 = ''
    stri1 = df.at[i,"Summary"].replace("{","")
    stri1 = stri1.replace("}","")
    stri1 = stri1.replace("'",'')
    #print(stri1)
    li = stri1.split(',')
    #print(li)
    type_ac = li[4].split(':')
    #print(type_ac)
    type_account1 = type_ac[1].strip() 
    #print(type_account1)
    if type_account1 == "SAVINGS":
        #print("in")
        bank_name1 = df.at[i,"bank"] #Bank name
        balance = li[0].split(':')
        current_balance1 = balance[1].strip() #Current balance
        account_no1 = df.at[i,"maskedAccountNumber"] #Account no
        bank_name.append(bank_name1)
        account_type.append(type_account1)
        account_no.append(account_no1)
        balances.append(current_balance1)
        
        #Account Type
        #print (bank_name1, current_balance1, account_no1, type_account1)


# In[ ]:


balances


# In[ ]:


df_out = pd.DataFrame({"bankName": bank_name, "currentBalance": balances, "accountNo": account_no, "typeAccount": account_type})
df_out


# In[ ]:


df_out.to_json("../bankDetails.json", orient = 'records')
print("File generated")
#sys.stdout.flush()

# In[ ]:





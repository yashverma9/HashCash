print("File generated")
import sys
import json
import csv
import pandas as pd
import numpy as np



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


json2csv('shreya_allfidata.json', 'bank_details.csv', 'accounts')

df = pd.read_csv('bank_details.csv')

#df["Summary"]

#type(df.at[0,"Summary"])

#df.at[1,"Summary"]
#df.shape


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

#balances
    
df_out = pd.DataFrame({"bankName": bank_name, "currentBalance": balances, "accountNo": account_no, "typeAccount": account_type})
#df_out



df_out.to_json("src/bankDetails.json", orient = 'records')
print("File generated")
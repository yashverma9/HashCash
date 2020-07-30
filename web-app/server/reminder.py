#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import numpy as np
import csv
import json
import datetime as dt
from datetime import datetime


# In[3]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# In[4]:


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


# In[5]:


json2csv('fish102.json', 'fish102.csv', 'fiData')


# In[6]:


df = pd.read_csv('fish102.csv')


# In[7]:


df


# In[8]:


new_df = df.drop(["transactionTimestamp","balance","reference"],axis = 1)


# In[9]:


new_df


# In[10]:


#Checking is narration string type or not
isinstance(new_df["narration"][0],str)


# In[11]:


#To find the number of forward slashes in each narration
new_df["narration"][0].count('/')


# In[12]:


#To find the first occurance index of a substr (works same as .index(), but find() is better because it returns -1 when not found) 
new_df["narration"][0].find('I/')


# In[13]:


#To split a string into tuple of 3 parts, part before specified substr, substr and part after substr
tup1 = new_df["narration"][0].partition('/')
print(tup1)


# In[14]:


tup1[0]=="UPI"
type(new_df.shape[0])==int
new_df["narration"].nunique()
type(new_df["narration"].isna().sum())


# In[15]:


#GOOD USEFUL METHOD
#To split the string into many parts based on the separator and return list, it returns original string in list if the separator is not present
li = new_df["narration"][0].split('/')
print(li)


# In[16]:


def gen_narrations(df):
    nan = df["narration"].isna().sum()
    if nan!=0:
        return ("The narration is empty for nan no. of transactions!")
    n = df.shape[0]
    narrations = []
    for i in range(0,n):
        li = [df["txnId"][i]]
        li+=(df["narration"][i].split('/'))
        narrations.append(li)
    return pd.DataFrame(narrations, columns =['txnId','f1','f2','f3','f4','f5','f6'], dtype = str)
    


# In[17]:


narrations = gen_narrations(new_df)


# In[18]:


narrations


# In[19]:


#Making separate dataframes for specific merchants: These 7 are unique ones
upi_df = narrations[narrations["f1"]=="UPI"]
gib_df = narrations[narrations["f1"]=="GIB"]
vps_df = narrations[narrations["f1"]=="VPS"]
atm_df = narrations[narrations["f1"]=="ATM"]
ach_df = narrations[narrations["f1"]=="ACH"]
mmt_df = narrations[narrations["f1"]=="MMT"]
iin_df = narrations[narrations["f1"]=="IIN"]


# In[20]:


upi_df


# In[21]:


gib_df


# In[22]:


vps_df


# In[23]:


atm_df


# In[24]:


ach_df


# In[25]:


mmt_df


# In[26]:


iin_df


# In[27]:


#Making separate dataframes for specific merchants: These are for the others
ips_df = narrations[narrations["f1"]=="IPS"]
vin_df = narrations[narrations["f1"]=="VIN"]
cms_df = narrations[narrations["f1"]=="CMS"]
bil_df = narrations[narrations["f1"]=="BIL"]
nfs_df = narrations[narrations["f1"]=="NFS"]
other_df = narrations[narrations["f1"]!="UPI"]
other_df = other_df[other_df["f1"]!="GIB"]
other_df = other_df[other_df["f1"]!="VPS"]
other_df = other_df[other_df["f1"]!="ATM"]
other_df = other_df[other_df["f1"]!="ACH"]
other_df = other_df[other_df["f1"]!="MMT"]
other_df = other_df[other_df["f1"]!="IIN"]
other_df = other_df[other_df["f1"]!="IPS"]
other_df = other_df[other_df["f1"]!="VIN"]
other_df = other_df[other_df["f1"]!="CMS"]
other_df = other_df[other_df["f1"]!="BIL"]
other_df = other_df[other_df["f1"]!="NFS"]


# In[28]:


ips_df


# In[29]:


vin_df


# In[30]:


cms_df


# In[31]:


bil_df


# In[32]:


nfs_df


# In[33]:


other_df


# In[34]:


#This dictionary indicates the column name which gives us the insights about the brand/company/reciever of money/transaction etc (CMS: there is no description)
merchants_list = ["UPI","GIB","VPS","ATM","ACH","MMT","IIN","IPS","VIN","CMS","BIL","NFS","OTHER"]
merchants_df_dict = {"UPI":upi_df, "GIB":gib_df, "VPS":vps_df, "ATM":atm_df, "ACH":ach_df, "MMT":mmt_df, "IIN":iin_df, "IPS":ips_df, "VIN":vin_df, "CMS":cms_df, "BIL":bil_df, "NFS":nfs_df, "OTHER":other_df}
selector_dict = {"UPI":["f3", "f4"], "GIB":["f3"], "VPS":["f2"], "ATM":["f3"], "ACH":["f2"], "MMT":["f4"], "IIN":["f3"], "IPS":["f2"], "VIN":["f2"], "CMS":["f3"], "BIL":["f3","f4"], "NFS":["f3"], "OTHER":["f1"]}


# In[35]:


print(merchants_list)
print(merchants_df_dict)
print(selector_dict)


# In[36]:


brand_df = pd.read_csv("Brand.csv")
brand_df


# In[37]:


#Function to remove whitespace (called by simply_string)
def remove(string): 
    return string.replace(" ", "") 
#Function to bring entire string to lower case and remove any spaces
def simplify_string(string):
    string = remove(string)
    string = string.casefold()
    return string
#Function to parse UPI id
import re
def parse_upi(string):
    alphanumeric = ""
    pattern = '[0-9.]'
    string = re.sub(pattern,'',string)
    tup = string.partition('@')
    return tup[0]
    
def parse_cms(string):
    pattern = '[0-9_]'
    return re.sub(pattern,'',string)


# In[38]:


#Function to find which transaction indicates which brand
'''
def detect_brands(merchant, merchant_df, brands):
    f = selector_dict[merchant]
    if merchant=="UPI":
        trans_data1= merchant_df[f[0]].apply(simplify_string)
        trans_data2= merchant_df[f[1]].apply(simplify_string)
        trans_data2=trans_data2.apply(parse_upi)
        trans_data =trans_data1.str.cat(trans_data2, sep =",")
    elif merchant=="CMS":
        trans_data= merchant_df[f[0]].apply(simplify_string)
        trans_data=trans_data.apply(parse_cms)
    elif merchant=="BIL":
        trans_data1= merchant_df[f[0]].apply(simplify_string)
        trans_data2= merchant_df[f[1]].apply(simplify_string)
        trans_data = trans_data1.str.cat(trans_data2, sep ="")
        
    else:
        trans_data= merchant_df[f[0]].apply(simplify_string)
    brands = brands.apply(simplify_string)
    #print("brands: \n", brands)
    #print("trans_summaries: \n", trans_data)
    print("The total transactions under ",merchant,": ",len(trans_data))
    matching_count = 0
    matched = 0
    if merchant!="UPI":
        for t in trans_data:
            matched = 0
            for b in brands:
                index1 = t.find(b)
                index2 = b.find(t)
            
                if index1!=-1: #and index2!=-1:
                    #print(t)
                    matched = 1
                    matching_count+=1
                    continue
                elif index2!=-1:
                    #print(t)
                    matched = 1
                    matching_count+=1
                    continue
            if matched == 0:
                print(t)
    
    if merchant=="UPI":
        print("Trying with UPI ID")
        for t in trans_data:
            tup1= t.partition(',')
            t1 = tup1[0]
            t2 = tup1[2]
            matched = 0
            for b in brands:
                index1 = t1.find(b)
                index2 = b.find(t1)
            
                if index1!=-1: #and index2!=-1:
                    #print(t)
                    matched = 1
                    matching_count+=1
                    continue
                elif index2!=-1:
                    #print(t)
                    matched = 1
                    matching_count+=1
                    continue
            if matched == 0:
                print ("Matching no. 2")
                #print("t2: ",t2)
                for b in brands:
                    index1 = t2.find(b)
                    index2 = b.find(t2)
            
                    if index1!=-1: #and index2!=-1:
                        #print(t)
                        matched = 1
                        matching_count+=1
                        continue
                    elif index2!=-1:
                        #print(t)
                        matched = 1
                        matching_count+=1
                        continue
            if matched == 0:
                print("Not found: ",tup1)
                                 
    print("Matched brands: ",matching_count)
    '''


# In[39]:


#detect_brands(merchants_list[0],merchants_df_dict[merchants_list[0]], brands)
#print (merchants_list[9]) #,merchants_df_dict[merchants_list[0]]


# In[40]:


type(df[df["narration"]=="SAL FINTECH PRODUCTS and SOLUTIONS DEC 2019"]["txnId"])


# In[41]:


df.loc[df['txnId']=='M3258741','mode'].values[0]


# In[42]:


type(df["txnId"][0])


# In[43]:


output_df = df.copy()


# In[44]:


output_df.drop(["transactionTimestamp", "narration", "reference"],axis = 1, inplace = True)


# In[45]:


output_df


# In[46]:


#output_df.at[df["txnId"]=="M3258741"]["brand"] = "yash"


# In[47]:


#To find the row index where the some condtion is met
#index = output_df.index[output_df['txnId']=="M6221730"].tolist()


# In[48]:


#To assign value to new cell of dataframe using row index and column name
#output_df.at[index[0], "brand"] = "Nike"


# In[49]:


output_df["brand"] = ""


# In[50]:


output_df["category"] = ""


# In[51]:


output_df


# In[52]:


def detect_brands(merchant, merchant_df, brand_df,output_df):
    output_df = output_df.copy()
    brand_df = brand_df.copy()
    merchant_df = merchant_df.copy()
    f = selector_dict[merchant]
    
    if merchant=="UPI":
        merchant_df[f[0]] = merchant_df[f[0]].apply(simplify_string)
        merchant_df[f[1]] = merchant_df[f[1]].apply(simplify_string)
        merchant_df[f[1]] = merchant_df[f[1]].apply(parse_upi)
        merchant_df[f[0]] = merchant_df[f[0]].str.cat(merchant_df[f[1]], sep =",")
        #print(merchant_df.head())
    elif merchant=="CMS":
        merchant_df[f[0]] = merchant_df[f[0]].apply(simplify_string)
        merchant_df[f[0]] = merchant_df[f[0]].apply(parse_cms)
        
    elif merchant=="BIL":
        merchant_df[f[0]] = merchant_df[f[0]].apply(simplify_string)
        merchant_df[f[1]] = merchant_df[f[1]].apply(simplify_string)
        merchant_df[f[0]] = merchant_df[f[0]] .str.cat(merchant_df[f[1]], sep ="")
        
    else:
        merchant_df[f[0]] = merchant_df[f[0]].apply(simplify_string)
        
    brand_df['parsed'] = brand_df['Brand_name'].apply(simplify_string)
    
    #print("brands: \n", brands)
    #print("trans_summaries: \n", trans_data)
   # print("The total transactions under ",merchant,": ",len(merchant_df[f[0]]))
    matching_count = 0
    matched = 0
    if merchant!="UPI":
       # print("Doing for: ",merchant)
        for index_t, row_t in merchant_df.iterrows():
            txnId = row_t['txnId']
            t = row_t[f[0]]
            matched = 0
            for index_b, row_b in brand_df.iterrows():
                b = row_b["parsed"]
                index1 = t.find(b)
                index2 = b.find(t)
            
                if index1!=-1: #and index2!=-1:
                    #print(t)
                    matched = 1
                    matched_brand = row_b["Brand_name"]
                    matched_category = row_b["Category"]
                    matching_count+=1
                    continue
                elif index2!=-1:
                    #print(t)
                    matched = 1
                    matched_brand = row_b["Brand_name"]
                    matched_category = row_b["Category"]
                    matching_count+=1
                    continue
            if matched == 0:
              #  print("Not found: ",t)
                matched_brand, matched_category = "Unknown", "Other"
            #else:
                #print("TxnId: ", txnId, "  Brand Name: ", matched_brand, "  Category: ",matched_category)
            
            index = output_df.index[output_df['txnId']==txnId].tolist()
            output_df.at[index[0], "brand"] = matched_brand
            output_df.at[index[0], "category"] = matched_category
    
    if merchant=="UPI":
       # print("Doing for: ",merchant)
        for index_t, row_t in merchant_df.iterrows():
            txnId = row_t['txnId']
            #print(txnId)
            tup1= row_t[f[0]].partition(',')
            t1 = tup1[0]
            t2 = tup1[2]
            matched = 0
            for index_b, row_b in brand_df.iterrows():
                b = row_b["parsed"]
                index1 = t1.find(b)
                index2 = b.find(t1)
            
                if index1!=-1: #and index2!=-1:
                    #print(t)
                    matched = 1
                    matched_brand = row_b["Brand_name"]
                    matched_category = row_b["Category"]
                    matching_count+=1
                    continue
                elif index2!=-1:
                    #print(t)
                    matched = 1
                    matched_brand = row_b["Brand_name"]
                    matched_category = row_b["Category"]
                    matching_count+=1
                    continue
            if matched == 0:
                #print ("Matching no. 2")
                #print("t2: ",t2)
                for index_b, row_b in brand_df.iterrows():
                    b = row_b["parsed"]
                    index1 = t2.find(b)
                    index2 = b.find(t2)
            
                    if index1!=-1: #and index2!=-1:
                        #print(t)
                        matched = 1
                        matched_brand = row_b["Brand_name"]
                        matched_category = row_b["Category"]
                        matching_count+=1
                        continue
                    elif index2!=-1:
                        #print(t)
                        matched = 1
                        matched_brand = row_b["Brand_name"]
                        matched_category = row_b["Category"]
                        matching_count+=1
                        continue
                
            if matched == 0:
              #  print("Not found: ",tup1)
                matched_brand, matched_category = t2, "Transfer"
           # else:
                #print("TxnId: ", txnId, "  Brand Name: ", matched_brand, "  Category: ",matched_category)
            index = output_df.index[output_df['txnId']==txnId].tolist()
            output_df.at[index[0], "brand"] = matched_brand
            output_df.at[index[0], "category"] = matched_category
    #print("Matched brands: ",matching_count)
    return output_df


# In[53]:


for i in range(len(merchants_list)):
    output_df = detect_brands(merchants_list[i],merchants_df_dict[merchants_list[i]], brand_df, output_df)


# In[54]:


output_df


# In[55]:


output_df['valueDate'] = pd.to_datetime(output_df['valueDate'], format='%Y-%m-%d')


# In[56]:


selected_df = (output_df[output_df["category"].isin(["Rent", "Insurance", "Loan (EMI)", "Credit Card" ])])
selected_df


# In[127]:


brand, short_brand, category, amount, date, color = [], [], [], [], [], []
today = datetime.now()
t_day = today.day
t_month = today.month
t_year = today.year
color1 = ""
print(t_year)


# In[128]:


# Rent reminder
rent_ind = selected_df.index[selected_df['brand']=="Rent"].tolist()
rent_date = str(selected_df.at[rent_ind[-1], "valueDate"])
rent_date= rent_date[:10]
rent_date = rent_date[8:]
if int(rent_date) >= t_day:
    if t_month>=10:
        rent_date = rent_date+"-"+str(t_month)+"-"+str(t_year)[:2]
    else: 
        rent_date = rent_date+"-0"+str(t_month)+"-"+str(t_year)[:2]
else:
    n_month = t_month+1
    if n_month>=10:
        rent_date = rent_date+"-"+str(n_month)+"-"+str(t_year)[:2]
    else: 
        rent_date = rent_date+"-0"+str(n_month)+"-"+str(t_year)[:2]
rent_month = int(rent_date[3:5])
rent_d_date = int(rent_date[0:2])
dif = rent_d_date - t_day
if rent_month != t_month:
    color1 = "Green"
else:
    if dif>7:
        color1 = "Yellow"
    else:
        color1 = "Red"
color.append(color1)
rent_amount = selected_df.at[rent_ind[-1], "amount"]
rent_amount = str(rent_amount)
brand.append("Rent")
short_brand.append("Rent")
category.append("Rent")
amount.append(rent_amount)
date.append(rent_date)


# In[129]:


color


# In[130]:


# Insurance reminder
#ins_ind = selected_df.index[selected_df['category']=="Insurance"].tolist()
#ins_ind
ins_df = selected_df[selected_df["category"]=="Insurance"]
ins_brands = ins_df["brand"].tolist()
ins_brands = set(ins_brands)
ins_brands


# In[131]:


#Insurance reminder
for ins in ins_brands:
    ins_ind = ins_df.index[ins_df['brand'] == ins].tolist()
    ins_date = str(ins_df.at[ins_ind[-1], "valueDate"])
    ins_amount = ins_df.at[ins_ind[-1], "amount"]
    ins_amount = str(ins_amount)
    ins_date= ins_date[:10]
    ins_date = ins_date[8:]
    if int(ins_date) >= t_day:
        if t_month>=10:
            ins_date = ins_date+"-"+str(t_month)+"-"+str(t_year)[:2]
        else: 
            ins_date = ins_date+"-0"+str(t_month)+"-"+str(t_year)[:2]
    else:
        n_month = t_month+1
        if n_month>=10:
            ins_date = ins_date+"-"+str(n_month)+"-"+str(t_year)[:2]
        else: 
            ins_date = ins_date+"-0"+str(n_month)+"-"+str(t_year)[:2]
    ins_month = int(ins_date[3:5])
    ins_d_date = int(ins_date[0:2])
    dif = ins_d_date - t_day
    if ins_month != t_month:
        color1 = "Green"
    else:
        if dif>7:
            color1 = "Yellow"
        else:
            color1 = "Red"
    color.append(color1)
    brand.append(ins)
    short_brand.append(ins.replace(" Insurance",""))
    category.append("Insurance")
    amount.append(ins_amount)
    date.append(ins_date)


# In[132]:


#Loan (EMI) reminder
loan_df = selected_df[selected_df["category"]=="Loan (EMI)"]
loan_brands = loan_df["brand"].tolist()
loan_brands = set(loan_brands)
loan_brands
loan_df


# In[133]:


# LOAN
for loan in loan_brands:
    loan_ind = loan_df.index[loan_df['brand'] == loan].tolist()
    loan_date = str(loan_df.at[loan_ind[-1], "valueDate"])
    loan_amount = loan_df.at[loan_ind[-1], "amount"]
    loan_amount = str(loan_amount)
    loan_date= loan_date[:10]
    loan_date = loan_date[8:]
    if int(loan_date) >= t_day:
        if t_month>=10:
            loan_date = loan_date+"-"+str(t_month)+"-"+str(t_year)[:2]
        else: 
            loan_date = loan_date+"-0"+str(t_month)+"-"+str(t_year)[:2]
    else:
        n_month = t_month+1
        if n_month>=10:
            loan_date = loan_date+"-"+str(n_month)+"-"+str(t_year)[:2]
        else: 
            loan_date = loan_date+"-0"+str(n_month)+"-"+str(t_year)[:2]
    loan_month = int(loan_date[3:5])
    loan_d_date = int(loan_date[0:2])
    dif = loan_d_date - t_day
    if loan_month != t_month:
        color1 = "Green"
    else:
        if dif>7:
            color1 = "Yellow"
        else:
            color1 = "Red"
    color.append(color1)
    brand.append(loan)
    short_brand.append(loan.replace(" Loan",""))
    category.append("Loan (EMI)")
    amount.append(loan_amount)
    date.append(loan_date)


# In[134]:


#Credit Card reminder
credit_df = selected_df[selected_df["category"]=="Credit Card"]
credit_brands = credit_df["brand"].tolist()
credit_brands = set(credit_brands)
credit_brands
credit_df


# In[135]:


# Credit Card
for credit in credit_brands:
    credit_ind = credit_df.index[credit_df['brand'] == credit].tolist()
    credit_date = str(credit_df.at[credit_ind[-1], "valueDate"])
    #credit_amount = credit_df.at[credit_ind[-1], "amount"]
    #credit_amount = str(loan_amount)
    credit_date= credit_date[:10]
    credit_date = credit_date[8:]
    if int(credit_date) >= t_day:
        if t_month>=10:
            credit_date = credit_date+"-"+str(t_month)+"-"+str(t_year)[:2]
        else: 
            credit_date = credit_date+"-0"+str(t_month)+"-"+str(t_year)[:2]
    else:
        n_month = t_month+1
        if n_month>=10:
            credit_date = credit_date+"-"+str(n_month)+"-"+str(t_year)[:2]
        else: 
            credit_date = credit_date+"-0"+str(n_month)+"-"+str(t_year)[:2]
    credit_month = int(credit_date[3:5])
    credit_d_date = int(credit_date[0:2])
    dif = credit_d_date - t_day
    if credit_month != t_month:
        color1 = "Green"
    else:
        if dif>7:
            color1 = "Yellow"
        else:
            color1 = "Red"
    color.append(color1)
    brand.append(credit)
    sht = credit.replace(" (HDFC Credit Card Payment)","")
    sht = sht.replace(" (ICICI Bank Credit Card Ca)","")
    sht = sht.replace(" CC PMT","")
    sht = sht.replace(" Card","")
    sht = sht.replace(" (SBICARD)","")
    short_brand.append(sht)
    category.append("Credit Card")
    amount.append("--")
    date.append(credit_date)


# In[136]:


(len(brand), len(short_brand), len(category), len(date), len(amount))
((brand), (short_brand), (category), (date), (amount), (color))


# In[138]:


df_out= pd.DataFrame({"brand": brand, "short_brand": short_brand, "category": category, "next_date": date, "amount": amount, "color": color})
df_out


# In[140]:


df_out.to_json("../reminderDetails.json", orient = 'records')


# In[ ]:





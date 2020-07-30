#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import json
import datetime as dt


# In[2]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# In[3]:


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


# In[4]:


json2csv('fish102.json', 'fish102.csv', 'fiData')


# In[5]:


df = pd.read_csv('fish102.csv')


# In[6]:


df


# In[7]:


new_df = df.drop(["transactionTimestamp","balance","reference"],axis = 1)


# In[8]:


new_df


# In[9]:


#Checking is narration string type or not
isinstance(new_df["narration"][0],str)


# In[10]:


#To find the number of forward slashes in each narration
new_df["narration"][0].count('/')


# In[11]:


#To find the first occurance index of a substr (works same as .index(), but find() is better because it returns -1 when not found) 
new_df["narration"][0].find('I/')


# In[12]:


#To split a string into tuple of 3 parts, part before specified substr, substr and part after substr
tup1 = new_df["narration"][0].partition('/')
#print(tup1)


# In[13]:


tup1[0]=="UPI"
type(new_df.shape[0])==int
new_df["narration"].nunique()
type(new_df["narration"].isna().sum())


# In[14]:


#GOOD USEFUL METHOD
#To split the string into many parts based on the separator and return list, it returns original string in list if the separator is not present
li = new_df["narration"][0].split('/')
#print(li)


# In[15]:


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
    


# In[16]:


narrations = gen_narrations(new_df)


# In[17]:


narrations


# In[18]:


#Making separate dataframes for specific merchants: These 7 are unique ones
upi_df = narrations[narrations["f1"]=="UPI"]
gib_df = narrations[narrations["f1"]=="GIB"]
vps_df = narrations[narrations["f1"]=="VPS"]
atm_df = narrations[narrations["f1"]=="ATM"]
ach_df = narrations[narrations["f1"]=="ACH"]
mmt_df = narrations[narrations["f1"]=="MMT"]
iin_df = narrations[narrations["f1"]=="IIN"]


# In[19]:


upi_df


# In[20]:


gib_df


# In[21]:


vps_df


# In[22]:


atm_df


# In[23]:


ach_df


# In[24]:


mmt_df


# In[25]:


iin_df


# In[26]:


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


# In[27]:


ips_df


# In[28]:


vin_df


# In[29]:


cms_df


# In[30]:


bil_df


# In[31]:


nfs_df


# In[32]:


other_df


# In[33]:


#This dictionary indicates the column name which gives us the insights about the brand/company/reciever of money/transaction etc (CMS: there is no description)
merchants_list = ["UPI","GIB","VPS","ATM","ACH","MMT","IIN","IPS","VIN","CMS","BIL","NFS","OTHER"]
merchants_df_dict = {"UPI":upi_df, "GIB":gib_df, "VPS":vps_df, "ATM":atm_df, "ACH":ach_df, "MMT":mmt_df, "IIN":iin_df, "IPS":ips_df, "VIN":vin_df, "CMS":cms_df, "BIL":bil_df, "NFS":nfs_df, "OTHER":other_df}
selector_dict = {"UPI":["f3", "f4"], "GIB":["f3"], "VPS":["f2"], "ATM":["f3"], "ACH":["f2"], "MMT":["f4"], "IIN":["f3"], "IPS":["f2"], "VIN":["f2"], "CMS":["f3"], "BIL":["f3","f4"], "NFS":["f3"], "OTHER":["f1"]}


# In[34]:


#print(merchants_list)
#print(merchants_df_dict)
#print(selector_dict)


# In[35]:


brand_df = pd.read_csv("Brand.csv")
brand_df


# In[36]:


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


# In[37]:


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


# In[38]:


#detect_brands(merchants_list[0],merchants_df_dict[merchants_list[0]], brands)
#print (merchants_list[9]) #,merchants_df_dict[merchants_list[0]]


# In[39]:


type(df[df["narration"]=="SAL FINTECH PRODUCTS and SOLUTIONS DEC 2019"]["txnId"])


# In[40]:


df.loc[df['txnId']=='M3258741','mode'].values[0]


# In[41]:


type(df["txnId"][0])


# In[42]:


output_df = df.copy()


# In[43]:


output_df.drop(["transactionTimestamp", "narration", "reference"],axis = 1, inplace = True)


# In[44]:


output_df


# In[45]:


#output_df.at[df["txnId"]=="M3258741"]["brand"] = "yash"


# In[46]:


#To find the row index where the some condtion is met
#index = output_df.index[output_df['txnId']=="M6221730"].tolist()


# In[47]:


#To assign value to new cell of dataframe using row index and column name
#output_df.at[index[0], "brand"] = "Nike"


# In[48]:


output_df["brand"] = ""


# In[49]:


output_df["category"] = ""


# In[50]:


output_df


# In[53]:


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
    #print("The total transactions under ",merchant,": ",len(merchant_df[f[0]]))
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
               # print("Not found: ",t)
                matched_brand, matched_category = "Unknown", "Other"
         #   else:
             #   print("TxnId: ", txnId, "  Brand Name: ", matched_brand, "  Category: ",matched_category)
            
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
              #  print ("Matching no. 2")
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
          #  else:
            #    print("TxnId: ", txnId, "  Brand Name: ", matched_brand, "  Category: ",matched_category)
            
            index = output_df.index[output_df['txnId']==txnId].tolist()
            output_df.at[index[0], "brand"] = matched_brand
            output_df.at[index[0], "category"] = matched_category
   # print("Matched brands: ",matching_count)
    return output_df


# In[54]:


for i in range(len(merchants_list)):
    output_df = detect_brands(merchants_list[i],merchants_df_dict[merchants_list[i]], brand_df, output_df)


# In[55]:


output_df


# In[56]:


output_df['valueDate'] = pd.to_datetime(output_df['valueDate'], format='%Y-%m-%d')


# In[57]:


#Defining dictionary for identifying days
days_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thurday", 4:"Friday", 5: "Saturday", 6: "Sunday"}
months_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5:"May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}


# In[58]:


months_dict[output_df.at[50,'valueDate'].month]


# In[59]:


month_wise_exp = pd.DataFrame({"Month":[months_dict[i] for i in months_dict.keys()],"Total_Expense":0, "Total_Income":0})


# In[60]:


month_wise_exp


# In[61]:


def get_monthly_exp(df, month_wise_exp):
    df = df.copy()
    month_wise_exp = month_wise_exp.copy()
    for index_1, row_1 in df.iterrows():
            date = row_1['valueDate']
            type_trans = row_1['type']
            amnt = row_1["amount"]
            m = date.month
            m = months_dict[m]
            for index_2, row_2 in month_wise_exp.iterrows():
                mon = row_2['Month']
                if mon == m:
                    ind = month_wise_exp.index[month_wise_exp['Month']==mon].tolist()
                    if type_trans == "DEBIT":
                        month_wise_exp.at[ind[0], "Total_Expense"] += amnt  
                    if type_trans == "CREDIT":
                        month_wise_exp.at[ind[0], "Total_Income"] += amnt  
                    continue
    return month_wise_exp
    


# In[62]:


month_wise_exp = get_monthly_exp(output_df, month_wise_exp)


# In[63]:


month_wise_exp


# In[64]:


month_wise_exp.to_json("../web-app/server/src/monthWiseEI.json", orient = 'records')


# In[65]:


opening_closing = pd.DataFrame({"Month":[months_dict[i] for i in months_dict.keys()], "Opening_Balance":0, "Closing_Balance":0})


# In[66]:


opening_closing


# In[67]:


def get_opening_closing(df, opening_closing):
    df = df.copy()
    opening_closing = opening_closing.copy()
    for index_1, row_1 in opening_closing.iterrows():
                mon = row_1['Month']
                for index_2, row_2 in df.iterrows():
                    date = row_2['valueDate']
                    type_trans = row_2['type']
                    bal = row_2["balance"]
                    amnt = row_2["amount"]
                    m = date.month
                    m = months_dict[m]
                    if m == mon:
                        ind = opening_closing.index[opening_closing['Month']==mon].tolist()
                        if type_trans == "DEBIT":
                            opening_closing.at[ind[0], "Opening_Balance"] = bal + amnt
                        else:
                            opening_closing.at[ind[0], "Opening_Balance"] = bal - amnt
                        break
    
    for index_1, row_1 in opening_closing.iterrows():
        mon = row_1['Month']
        opening = row_1['Opening_Balance']
        ind = opening_closing.index[opening_closing['Month']==mon].tolist()
        #print (ind)
        if ind[0] == 0:
                opening_closing.at[11, "Closing_Balance"] = opening
        else:
            opening_closing.at[ind[0]-1, "Closing_Balance"] = opening
    return opening_closing            


# In[68]:


opening_closing = get_opening_closing(output_df, opening_closing)
opening_closing


# In[69]:


opening_closing.to_json("../web-app/server/src/openingClosing.json", orient = 'records')


# In[97]:


category_list = brand_df["Category"].unique()
category_list.sort()
category_list


# In[71]:


category_wise_exp = pd.DataFrame({"Category": category_list, "Total_Expense":0})
category_wise_exp


# In[72]:


def get_category_exp(df, category_wise_exp):
    df = df.copy()
    category_wise_exp = category_wise_exp.copy()
    for index_1, row_1 in df.iterrows():
            cat = row_1['category']
            type_trans = row_1['type']
            amnt = row_1["amount"]
            for index_2, row_2 in category_wise_exp.iterrows():
                c = row_2['Category']
                if cat == c:
                    ind = category_wise_exp.index[category_wise_exp['Category']==cat].tolist()
                    if type_trans == "DEBIT":
                        category_wise_exp.at[ind[0], "Total_Expense"] += amnt 
                    break
    return category_wise_exp


# In[73]:


category_wise_exp = get_category_exp(output_df, category_wise_exp)
category_wise_exp


# In[74]:


category_wise_exp.to_json("../web-app/server/src/categoryWiseYearly.json", orient = 'records')


# In[75]:


def Convert(lst): 
    li = list(months_dict.values())
    res_dct = {"Month": li} 
    res_dct.update({lst[i]: [0]*12  for i in range(0, len(lst))})
    res_dct.update({'Total_Expense' : [0]*12})
    return res_dct
res_dict = Convert(category_list)
res_dict


# In[76]:


category_month_wise_exp = pd.DataFrame(res_dict)
category_month_wise_exp


# In[77]:


def get_month_wise_category(df, category_month_wise_exp):
    df = df.copy()
    category_month_wise_exp = category_month_wise_exp.copy()
    for index_1, row_1 in df.iterrows():
            date = row_1['valueDate']
            mon_no = date.month
            type_trans = row_1['type']
            mon = months_dict[mon_no]
            amnt = row_1["amount"]
            category = row_1["category"]
            for index_2, row_2 in category_month_wise_exp.iterrows():
                m = row_2['Month']
                if mon == m:
                    ind = category_month_wise_exp.index[category_month_wise_exp['Month']==mon].tolist()
                    if type_trans == "DEBIT":
                        category_month_wise_exp.at[ind[0],category ] += amnt 
    return category_month_wise_exp                
            


# In[78]:


category_month_wise_exp = get_month_wise_category(output_df, category_month_wise_exp)
category_month_wise_exp["Total_Expense"] = month_wise_exp["Total_Expense"]
category_month_wise_exp


# In[79]:


category_month_wise_exp.to_json("../web-app/server/src/categoryMonthWise.json", orient = 'records')


# In[84]:


def get_current_balance(df):
    df = df.copy()
    '''
    y = datetime.now().year
    m = datetime.now().month
    d = datetime.now().day
    '''
    y = 2020
    m = 6
    d = 22
    dif = 31
    act_date = d
    for index_1, row_1 in df.iterrows():
        date = row_1['valueDate']
        year = date.year
        mon = date.month
        day = date.day
        if year == y and mon == m:
            #print (day)
            dif_cur = abs(d - day)
            dif = min(dif, dif_cur)
    #print(dif)
    act_date = d - dif
    for index_1, row_1 in df.iterrows():
        bal = row_1['balance']
        date = row_1['valueDate']
        year = date.year
        mon = date.month
        day = date.day
        #print (d)
        if year == y and mon == m and act_date == day:
            #print (d)
            return (round(bal,0), str(y)+"-"+str(m)+"-"+str(d))


# In[87]:


current_balance, date = get_current_balance(output_df)
current_balance, date
cur_balance_df = pd.DataFrame({"date":[date], "balance":[current_balance]})
cur_balance_df


# In[88]:


cur_balance_df.to_json("../web-app/server/src/currentBalance.json", orient = 'records')


# In[90]:


def get_month_wise_transaction(df, month):
    df = df.copy()
    df["month"] = ""
    for index_1, row_1 in df.iterrows():
        date = row_1['valueDate']
        txnId = row_1['txnId']
        mon_no = date.month
        mon = months_dict[mon_no]
        ind = df.index[df['txnId']==txnId].tolist()
        df.at[ind[0],"month"] = mon 
    df = df[df['month'] == month] 
    return df
    


# In[93]:


month_wise_transactions = pd.DataFrame()
for mon in months_dict.values():
    month_wise_transac = get_month_wise_transaction(output_df, mon)
    month_wise_transactions = pd.concat([month_wise_transactions, month_wise_transac], axis = 0, ignore_index= True)


# In[95]:


month_wise_transactions.to_json("../web-app/server/src/monthWiseTransactions.json", orient = 'records')


# In[96]:


def get_category_wise_transaction(df, category):
    df = df.copy()
    df = df[df['category']==category]
    return df


# In[99]:


category_wise_transactions = pd.DataFrame()
for cat in category_list:
    cat_wise_transac = get_category_wise_transaction(output_df, cat)
    category_wise_transactions = pd.concat([category_wise_transactions, cat_wise_transac], axis = 0, ignore_index= True)
category_wise_transactions


# In[100]:


category_wise_transactions.to_json("../web-app/server/src/categoryWiseTransactions.json", orient = 'records')


# In[102]:


brands_list = output_df["brand"].unique().tolist()
brands_list


# In[125]:


brand, amount = [],[]
invalid_categories = ["Bills", "Cash Withdrawal", "Health", "Insurance", "Investment", "Loan (EMI)", "Other", "Rent", "Transfer", "Credit Card"]
def get_brand_wise(output_df):
    output_df = output_df.copy()
    for b in brands_list:
        ind = output_df.index[output_df['brand']==b].tolist()
        t_type = output_df.at[ind[0],"type"]
        cat = output_df.at[ind[0],"category"]
        b_amount = 0
        if t_type == "DEBIT" and cat not in invalid_categories:
            for i in ind:
                amnt = output_df.at[i, "amount"]
                b_amount += amnt
            brand.append(b)
            amount.append(b_amount)              


# In[126]:


get_brand_wise(output_df)
brand, amount


# In[127]:


amount, brand = zip(*sorted(zip(amount, brand), reverse =True))


# In[128]:


amount, brand


# In[131]:


brandWise = pd.DataFrame({"brand": brand, "amount": amount})
brandWise


# In[132]:


brandWise.to_json("../brandWise.json", orient = 'records')
print("Files generated")

# In[ ]:





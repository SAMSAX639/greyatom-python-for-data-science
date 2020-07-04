# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank = pd.read_csv(path)

#Code starts here

# Step 1
categorical_var = bank.select_dtypes(include = 'object')
numerical_var = bank.select_dtypes(include = 'number')

# Step 2
banks = bank.drop("Loan_ID",axis=1)
banks.head()
bank_mode = banks.mode()
pd.Series(banks.columns).apply(lambda x: banks[x].fillna(banks[x].mode()[0],inplace=True))

# Step 3
avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values="LoanAmount")

# Step 4
se = banks[banks["Self_Employed"]=="Yes"]
loan_approved_se = len(se[se["Loan_Status"] == "Y"])
nse = banks[banks["Self_Employed"]=="No"]
loan_approved_nse = len(nse[nse["Loan_Status"] == "Y"])
percentage_se = round(loan_approved_se*100/614,2)
percentage_nse = round(loan_approved_nse*100/614,2)

# Step 5
banks["loan_term"] = banks["Loan_Amount_Term"].apply(lambda x: int(x)/12)
big_loan_term = len(banks[banks["loan_term"] >= 25])

# Step 6
loan_groupby = banks.groupby("Loan_Status")
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.agg(np.mean)



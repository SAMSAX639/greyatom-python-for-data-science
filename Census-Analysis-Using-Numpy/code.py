# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

# Appending New Record
census = np.concatenate((data, np.asarray(new_record)), axis=0)

# Analysis of Age Distribution
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)

# Analysis of country race distribution
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

lenght = [len_0,len_1,len_2,len_3,len_4]
minority_race = lenght.index(min(lenght))
print(minority_race)

# Analysis of Govt. Policy
senior_citizens = census[census[:,0] > 60]
senior_citizens_len = len(senior_citizens)
working_hours_sum = senior_citizens[:,6].sum()
avg_working_hours = round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)

# Analysis of Higher Educated People
high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]
avg_pay_high = round(high[:,7].mean(),2)
avg_pay_low = round(low[:,7].mean(),2)
print(avg_pay_high,avg_pay_low)




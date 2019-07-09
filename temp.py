#Importing all the required libraries
import pandas as pd
import numpy as np
from sklearn.feature_selection import chi2
import scipy.stats

#creating a dataframe which will help us have 3x2 matrix
subscription = {'Age Group': ['21 and below','21-35 Age','35 and above','21 and below','21-35 Age','35 and above'],
        'Subscription':['Yes','Yes','Yes','No','No','No'],
        'Subscriber': [700,300,200,500,700,600]
        }

df = pd.DataFrame(subscription,columns= ['Age Group','Subscription', 'Subscriber'])

# steps to calculate chi-square

cnt=pd.crosstab(df['Age Group'], df['Subscription'], values=df['Subscriber'], aggfunc='sum').round(0)
stat, p, dof, expected = scipy.stats.chi2_contingency(cnt)
print(stat)
prob= 0.95  #confidence interval or probability
critical = scipy.stats.chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f \n' % (prob, critical, stat))
#critical value is calculated from chi sqaure distribution table

#H0 (Null Hypothesis): Netflix subscription is not dependent on the age group subsciber belongs to
#H1 (Alternate Hypothesis):  Netflix subscription is dependent on the age group subsciber belongs to   

#there are two methods to evaluate chi-square
#Method 1
if abs(stat) >= critical:
    print('Dependent (reject Null Hypothesis)')
else:
    print('Independent (fail to reject Null Hypothesis)')

#Method 2
#interpret p-value
alpha = 1.0 - prob
print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
    print('Dependent (reject Null Hypothesis)')
else:
    print('Independent (fail to reject Null Hypothesis)')



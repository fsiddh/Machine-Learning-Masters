# necessary Imports
import pandas as pd
import matplotlib.pyplot as plt
import pickle
% matpllotlib inline

df= pd.read_csv('Admission_Prediction.csv') # reading the CSV file

df.head() # cheking the first five rows from the dataset
df.info() # printing the summary of the dataframe

df['GRE Score'].fillna(df['GRE Score'].mode()[0],inplace=True)
#to replace the missing values in the 'GRE Score' column with the mode of the column
# Mode has been used here to replace the scores with the most occuring scores so that data follows the general trend

df['TOEFL Score'].fillna(df['TOEFL Score'].mode()[0],inplace=True)
#to replace the missing values in the 'GRE Score' column with the mode of the column
# Mode has been used here to replace the scores with the most occuring scores so that data follows the general trend

df['University Rating'].fillna(df['University Rating'].mean(),inplace=True)
#to replace the missing values in the 'University Rating' column with the mode of the column
# Mean has been used here to replace the scores with the average score

# dropping the 'Chance of Admit' and 'serial number' as they are not going to be used as features for prediction
x=df.drop(['Chance of Admit','Serial No.'],axis=1)
# 'Chance of Admit' is the target column which shows the probability of admission for a candidate
y=df['Chance of Admit']


plt.scatter(df['GRE Score'],y) # Relationship between GRE Score and Chance of Admission
plt.scatter(df['TOEFL Score'],y) # Relationship between TOEFL Score and Chance of Admission
plt.scatter(df['CGPA'],y) # Relationship between CGPA and Chance of Admission


# splitting the data into training and testing sets
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.33, random_state=100)

# fitting the date to the Linear regression model
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(train_x, train_y)

# calucltaing the accuracy of the model
from sklearn.metrics import r2_score
score= r2_score(reg.predict(test_x),test_y)

# saving the model to the local file system
filename = 'finalized_model.pickle'
pickle.dump(reg, open(filename, 'wb'))

# prediction using the saved model.
loaded_model = pickle.load(open(filename, 'rb'))
prediction=loaded_model.predict(([[320,120,5,5,5,10,1]]))
print(prediction[0])

import pandas as pd
import datetime
import numpy as np
   
# Create a datetime variable for today
base = datetime.datetime.today()

# Create a list variable that creates 365 days of rows of datetime values
date_list = [base - datetime.timedelta(days=x) for x in range(0, 365)]
# Create a list variable of 365 numeric values
score_list = list(np.random.randint(low=0, high=10, size=365))

# Create an empty dataframe
df = pd.DataFrame()

# Create a column from the datetime variable
df['datetime'] = date_list
# Convert that column into a datetime datatype
df['datetime'] = pd.to_datetime(df['datetime'])

# Set the datetime column as the index
df.index = df['datetime']
# Create a column from the numeric score variable
df['score'] = score_list

# Let's take a took at the data
df.head()
# Group the data by month, and take the mean for each group (i.e. each month)
df.resample('M').mean()
print(df.to_json(orient='values'))

# Group the data by month, and take the sum for each group (i.e. each month)
df.resample('M').sum()


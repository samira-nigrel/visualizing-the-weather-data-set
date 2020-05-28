# --------------
 
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
 
 
# Generate a line chart that visualizes the readings in the months
 
def line_chart(df,period,col):
   dict = {'year': 'A', 'month': 'M', 'day': 'D'}
   df1 = df.groupby(pd.Grouper(freq=dict[period]))[[col]].mean()
   plt.plot(pd.DatetimeIndex(df1.index).month_name(),df1)
  
 
   """ A line chart that visualizes the readings in the months
  
   This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
  
   Keyword arguments:
   df - Pandas dataframe which has the data.
   period - Period of time over which you want to aggregate the data
   col - Feature of the dataframe
  
   """
  
  
 
 
 
 
 
 
 
# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
   for col in df.columns:
       #print(col)
       plt.figure(figsize=(10,4))
       sns.distplot(df[col].value_counts())  
      
 
   """ Univariate analysis of categorical columns
  
   This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
  
   Keyword arguments:
   df - Pandas dataframe which has the data.
  
   """
  
 
# Function to plot continous plots
def plot_cont(df,plt_typ):
   if plt_typ== "Dist_Plot":
       for col in df.columns:
           plt.figure(figsize=(10,4))
           sns.distplot(df[col].value_counts())
   else:
       for col in df.columns:
           plt.figure(figsize=(10,4))
           df.plot.box(weather_df[col].value_counts())
 
   """ Univariate analysis of Numerical columns
  
   This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
  
   Keyword arguments:
   df - Pandas dataframe which has the data.
   plt_type - type of plot through which you want to visualize the data
  
   """
  
 
 
 
 
 
 
 
# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
   aggregate = {'mean':np.mean,'max':np.max,'min':np.min}
   w = df.groupby(col1)[col2].agg(aggregate[agg1]).plot(kind='bar')
   return(w)
   """ Agrregate values by grouping
  
   This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
 
   Keyword arguments:
   df - Pandas dataframe which has the data.
   col1 - Feature of the dataframe on which values will be aggregated.
   agg1 - Dictionary of aggregate functions with feature as the key and func as the value
   col2 - Feature of the dataframe to be plot against grouped data.
  
   Returns:
   grouping - Dataframe with all columns on which it is grouped on.
   """
  
  
 
 
 
 
# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df = pd.read_csv(path,parse_dates=True, index_col='Date/Time')
#print(weather_df.head())
 
weather_df_num = weather_df.select_dtypes(include = 'number')
#weather_df_num.head()
 
weather_df_cat = weather_df.select_dtypes(include = 'object')
#weather_df_cat.head()
 
# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
line_chart(weather_df,'month', 'Temp (C)')
plt.ylim(-7,25)
plt.xlabel("Months")
plt.ylabel("Temperature")
plt.xticks(rotation=90)
 
 
# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.
plot_categorical_columns(weather_df_cat)
 
 
# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot
plot_cont(weather_df_num,"Dist_Plot")
 
 
# Call the function "plot_cont()" with the appropriate parameters to plot boxplot
plot_cont(weather_df_num," ")
 
# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
g = group_values(weather_df,'Weather','mean','Visibility (km)')





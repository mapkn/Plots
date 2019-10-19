# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:24:33 2016

@author: Mitul
"""

#import numpy as np

import matplotlib.pyplot as plt
import os.path
import pandas as pd

# useful link
#https://swcarpentry.github.io/python-novice-gapminder/09-plotting/


# Plotting from Dfs implicitly uses matplotlib.pyplot

path='\\\\FS002\\patemi$\\Data'
file = 'gapminder_gdp_oceania.csv'


# Read the data from csv into a DF
data = pd.read_csv(os.path.join(path,file), index_col='country')


# Extract year from last 4 characters of each column name
years = data.columns.str.strip('gdpPercap_')
# Convert year values to integers, saving results back to dataframe
data.columns = years.astype(int)

data.loc['Australia'].plot()



# Transpose data to plot multiple series
data.T.plot()
plt.style.use('ggplot')

# Bar chart
data.T.plot(kind='bar')
plt.ylabel('GDP per capita')



# Plotting by calling matplotlib directly. Command is plt.plot(x,y)
years = data.columns
gdp_australia = data.loc['Australia']
plt.plot(years, gdp_australia, 'g--')
plt.show()


# Plotting many sets of data together


gdp_australia = data.loc['Australia']
gdp_nz = data.loc['New Zealand']

# Plot with differently-colored markers.
plt.plot(years, gdp_australia, 'b-', label='Australia')
plt.plot(years, gdp_nz, 'g-', label='New Zealand')

# Create legend.
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('GDP per capita ($)')
plt.show()
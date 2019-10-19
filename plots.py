# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:24:33 2016

@author: Mitul
"""

import numpy as np

import matplotlib.pyplot as plt
import os.path
import pandas as pd

# Generates 2 random normal samples
y = np.random.standard_normal((1000, 2))

# size x = 17, y=7 
fig=plt.figure(figsize=(17, 7))

#axplot=plt.axes([5,5,5,5])

""" stacked=True allows to stack the two data sets """
plt.hist(y, label=['1st', '2nd'], stacked =False,bins=25)


plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')

# size x = 12, y = 5
fig2=plt.figure(figsize=(12, 5))

plt.plot(y)
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:09:53 2016

@author: Mitul
"""

import numpy as np
import numpy.random as random
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_clipboard(header=None).values.flatten()
data.sort()
norm=random.normal(0,2,len(data))
norm.sort()
plt.figure(figsize=(12,8),facecolor='1.0') 

plt.plot(norm,data,"o")

#generate a trend line as in http://widu.tumblr.com/post/43624347354/matplotlib-trendline
z = np.polyfit(norm,data, 1)
p = np.poly1d(z)
plt.plot(norm,p(norm),"k--", linewidth=2)
plt.title("Normal Q-Q plot", size=28)
plt.xlabel("Theoretical quantiles", size=24)
plt.ylabel("Expreimental quantiles", size=24)
plt.tick_params(labelsize=16)
plt.show()
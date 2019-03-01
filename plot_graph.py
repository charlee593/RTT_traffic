import numpy as np
from scipy.integrate import cumtrapz
from scipy.stats import norm
from matplotlib import pyplot as plt
# !/usr/bin/env python


import csv
reader = csv.reader(open('data/canada_dict.csv', 'r'))
d = {}
for row in reader:
   k, v = row
   d[k] = v

print d.keys()

# n = 1000
# x = np.linspace(0,100, n)
# data = norm.rvs(size=n)
# data = data + abs(min(data))
# data = np.sort(data)
# print data
# cdf = cumtrapz(x=x, y=data )
# cdf = cdf / max(cdf)
#
# fig, ax = plt.subplots(ncols=1)
# ax1 = ax.twinx()
# ax.hist(data, density=True, histtype='stepfilled', alpha=0.2)
# ax1.plot(data[1:],cdf)
# plt.show()
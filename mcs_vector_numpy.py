# -*- coding: utf-8 -*-
print('Created on Thu Oct 05 15:49:55 2017 @author: ATrain')

import math 
import numpy as np
from time import time 

np.random.seed(20000)
t0 = time()

#Parameters
S0 = 100.; K = 7.; T = 5.0; r = 0.05; sigma = 0.2
M = 50; dt = T / M; I = 250000

#simulating I paths with M time steps 
S = np.zeros((M + 1, I))
S[0] = S0 
for t in range(1, M+1):
    z = np.random.standard_normal(I) #pseudo random numbers 
    S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * math .sqrt(dt) * z)
        #vectorized operation per time step over all paths 
# calculating the monte carlo estimator 
C0 = math.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / I

#results output 
tnp1 = time() - t0 
print( 'European Option value %7.3f' % C0)
print('Duraiton in seconds %7.3f' % tnp1 )

import matplotlib.pyplot as plt 
plt.plot(S[:, :10])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')
plt.show()

plt.hist(S[-1], bins=50)
plt.grid(True)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.show()

plt.hist(np.maximum(S[-1] - K, 0), bins=50)
plt.grid(True)
plt.xlabel('option inner value')
plt.ylabel('frequency')
plt.ylim(0, 50000)
plt.show()

euro_nil = sum(S[-1] , K)
print( 'the total expiring worthless:', euro_nil)























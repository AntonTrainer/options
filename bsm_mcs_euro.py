#Mote Carlo valuation of the European call option in Blach-Scholes-Merton model

import numpy as np
from numpy import * 

#paramaters (variables)
SO = 500 #initial index val
K = 105 #strike price
T = 1.0 #time to maturity 
r = 0.05 #riskless short rate
sigma = 0.2 #volatility

I = 100000 #number of simulations

#valuation Algorythm 
z = np.random.standard_normal(I) #pseudorandom numbers
ST = SO * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z) # idex values at maturity 
hT = np.maximum(ST - K, 0) # inner values at maturity 
CO = np.exp(-r * T) * np.sum(hT) / I # Monte Carlo estimator 

#result output
print("Value of the European Call Option %5.3f" % CO)
"""z = random.standard_normal(I)
ST = SO * exp((r - 0.5 * sigma ** 2) * T + sigma * sqrt(T) * z)
hT = maximum(ST - K, 0)
CO = exp(-r * T) * sum(hT) / I 
print 'the value of the European call option %5.3f' % CO """




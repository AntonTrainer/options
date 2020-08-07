#%%
print 'BSM_Functions.py -- Created on Sat Sep 30 11:17:25 2017  --  @author: ATrain'

#black-scholes-merton model ex 1 
#bsm_functions.py

#analytical BSM Formula 

def bsm_call_value(SO, K, T, r, sigma):
    ''' Valuation of Euro call option in bsm model. 
    Analytical formula 
    
    Paramerters: 
        =========
    SO : float 
        initial stock/index level
    K : float 
        strike price
    T : float
        maturity date in year fractions 
    r : float
        constant risk-free short rate 
    sigma : float
        volatility factor in diffusion term 
    
    Returns
    ========
    value : float 
        present value of the European call option 
    '''
    from math import log, sqrt, exp 
    from scipy import stats 
    
    SO = float(SO)
    d1 = (log(SO / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(SO / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value = (SO * stats.norm.cdf(d1, 0.0, 1,0) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.00))
            #Stats.norm.cdf ----> Cummulative distribution function for normal distribution 
    return value 

#Vega function 
    

    ''' Vaga of European call option in BSM model.
    
     Paramerters: 
        =========
    SO : float 
        initial stock/index level
    K : float 
        strike price
    T : float
        maturity date in year fractions 
    r : float
        constant risk-free short rate 
    sigma : float
        volatility factor in diffusion term 
        
    Returns
    =======
    vega : float 
        partial derivative of BSM formula with respect to sigma ie vega
        
        '''
def bsm_vega(S0,K,T,r,sigma):
    from math import log,sqrt
    from scipy import stats 
    S0 = float(S0)
    d1 = (log(S0 / K ) + (r + 0.5 * sigma ** 2) * T) /(sigma * sqrt(T))
    vega = S0 * stats.norm.cdf(d1,0.0,1.0) * sqrt(T)
   
# Implied Volatility Function
    '''
     Paramerters: 
        =========
    SO : float 
        initial stock/index level
    K : float 
        strike price
    T : float
        maturity date in year fractions 
    r : float
        constant risk-free short rate 
    sigma_est : float
        estimated implied volatility
    it : interger
    number of iterations
    '''
    
def bsm_implied_volatility(S0,K,T,r,C0,sigma_est, it= 100):
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0,K,T,r,sigma_est) - C0)
                     / bsm_vega(S0,K,T,r,sigma_est))
    return sigma_est

VO = 17.6639
r = 0.01
import pandas as pd 
h5 = pd.io.pytables.HDFStore('./source/vstoxx_data_31032014.h5' , 'r')
futures_data = h5['futures_data'] #VSTOXX Futures data
options_data = h5['options_data'] #VSTOXX options data 
h5.close()
futures_data

   
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
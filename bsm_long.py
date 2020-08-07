
from math import log, sqrt, exp
from scipy import stats

def bsm_call_value(SO, K, T, r, sigma):
    """SO = initial stiock level
    K = strike price
    T = maturity date (year fractions)
    r = constant risk free rate 
    sigma = volatility factor in difffusion term 
    returns present value of European call option 
    """
    SO = float(SO)
    d1 = (log(SO/k) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T)) #note the difference bet d1 and d2 is only a +/- on the second term 
    d2 = (log(SO/k) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value = (SO * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    #stats.norm.cdf is the cummulative normal distribution function 
    return value
#Vaga funtction 

def bsm_vega(SO, K, T, r, sigma):
    SO = float(SO) 
    d1 = (log(SO/k) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    vega = SO * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)
    return vega

#Implied Volatility function 
def bsm_call_imp_vol(SO, K, T, r, CO, sigma_est, it=100): #it = iterations 

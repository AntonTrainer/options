import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['figure.titlesize'] = 18
plt.rcParams['figure.titleweight'] = 'medium'
plt.rcParams['lines.linewidth'] = 2.5

# Make a function for each of the options that are possible (long/short, put/call)
# S = underlying price of stock, K = Strike, Price = price of the option, leave out the premium because that is todays value vs the value of the call at expiration

# ---------Option Functions--------------


def long_call(S, K, Price):
    P = list(map(lambda x: max(x - K, 0) - Price, S))
    return P


def short_call(S, K, Price):
    P = long_call(S, K, Price)
    return [-1.0 * p for p in P]


def long_put(S, K, Price):
    P = list(map(lambda x: max(K - x, 0) - Price, S))
    return P


def short_put(S, K, Price):
    P = long_put(S, K, Price)
    return [-1.0 * p for p in P]

# -----------Graphing of Standard Payouts (with arbitary numbers)----------


# Create a list of stock prices with an x value every 20 cents
S = [t/5 for t in range(0, 500)]

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True,
                       sharey=True, figsize=(20, 15))
fig.suptitle('Payoff Functions for Long and Short Calls and Puts',
             fontsize=20, fontweight='bold')
fig.text(0.5, 0.04, 'Underlying Price', ha='center',
         fontsize=14, fontweight='bold')
fig.text(0.08, .5, 'Options Payoff (USD)', va='center',
         rotation='vertical', fontsize=14, fontweight='bold')

#Define the options to graph 
#----------Long Call/ Long Put ---------
lc_pay = long_call(S, 50, 0)
lp_pay = long_put(S, 50, 0)
plt.subplot(221)
plt.plot(S, lc_pay, 'r')
plt.plot(S, lp_pay, 'b')
plt.legend(['Long Call', 'Long Put'])

#----------Short Call Short Put --------------
sc_Pay = short_call(S, 50, 0)
sp_Pay = short_put(S, 50, 0)
plt.subplot(222)
plt.plot(S, sc_Pay, 'r')
plt.plot(S, sp_Pay, 'b')
plt.legend(['Short Call', 'Short Put'])

#----------Long Call, Short Put --------- PUT CALL PARITY
plt.subplot(223)
plt.plot(S, lc_pay, 'r')
plt.plot(S, sp_Pay, 'b')
plt.legend(['Long Call', 'Short Put'])

plt.subplot(224)
plt.plot(S, sc_Pay, 'r')
plt.plot(S, lp_pay, 'b')
plt.legend(['Short Call','Long Put'])

plt.show()





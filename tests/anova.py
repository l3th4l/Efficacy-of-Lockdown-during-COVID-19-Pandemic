import numpy as np 
import pandas as pd
import scipy.stats

def __init__():
    pass

def two_way(dat):
    dat = np.array(dat)

    N = np.prod(dat.shape)
    
    CF = np.sum(dat)**2 / N

    TSS = np.sum(dat**2) - CF
    dft = N - 1

    SSR = 1/(dat.shape[1]) * (dat.sum(axis = 1)**2).sum() - CF
    dfr = dat.shape[0] - 1
    
    SSC = 1/(dat.shape[0]) * (dat.sum(axis = 0)**2).sum() - CF
    dfc = dat.shape[1] - 1

    SSE = TSS - SSC - SSR 
    dfe = dft - dfr - dfc  

    p_r = 1-scipy.stats.f.cdf(SSR/SSE, dfr, dfe)
    p_c = 1-scipy.stats.f.cdf(SSC/SSE, dfc, dfe)

    output = {"N" : {" ":N},

              "Degrees of Freedom":
              {"row" : dfr, 
              "column" : dfc, 
              "error" : dfe, 
              "total" : N-1}, 

              "Sum of Squares":
              {"total" : TSS, 
              "row" : SSR, 
              "column" : SSC, 
              "error" : SSE}, 

              "F Ratio" : 
              {"row" : SSR/SSE, 
              "column" : SSC/SSE},

              "p-value":              
              {"row" : p_r, 
              "column" : p_c}}

    out = pd.DataFrame(output).fillna("")
    print(out)
    return p_r, p_c, out
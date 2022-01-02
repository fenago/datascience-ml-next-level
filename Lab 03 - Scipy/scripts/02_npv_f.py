
import numpy as np

def npv_f(rate, values):
    cashFlows = np.asarray(values)
    return (cashFlows/ (1+rate)**np.arange(1,len(cashFlows)+1)).sum(axis=0)

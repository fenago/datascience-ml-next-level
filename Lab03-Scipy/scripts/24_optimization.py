

import scipy.optimize as optimize 
def my_f(x):
    return 3 + x**2
    
optimize.fmin(my_f,5)   # 5 is initial value


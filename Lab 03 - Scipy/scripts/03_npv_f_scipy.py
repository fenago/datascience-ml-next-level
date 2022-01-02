
import scipy as sp
cashflows=[50,40,20,10,50]
npv=sp.npv(0.1,cashflows) #estimate NPV 
print round(npv,2)


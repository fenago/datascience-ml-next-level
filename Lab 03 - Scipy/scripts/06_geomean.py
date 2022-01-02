
import scipy as sp
ret=sp.array([0.1,0.05,-0.02])
arithmetric_mean=sp.mean(ret)  # arithmetic mean   
print "arithmatic mean=", arithmetric_mean 

geomean=pow(sp.prod(ret+1),1./len(ret))-1 # geometric mean   
print 'gemetric mean=',geomean


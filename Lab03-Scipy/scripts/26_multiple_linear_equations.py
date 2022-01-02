
import scipy as sp
A=sp.mat('[1 2 5; 2 5 1; 2 3 8]')
b = sp.mat('[10;8;5]')

print 'A.I*b=', A.I*b      

print linalg.solve(A,b)  # offer the same solution

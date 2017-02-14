//Calculate the cubic root of a number

import numpy as np

def cubic(x0,tol,maxIter):
    numIter=0
    err=tol+1
    S=x0
    print('{:2}   {:.15f}'.format(numIter,x0))
    while numIter<maxIter and err>tol:
        x1=(1/3)*((2*x0)+(S/(x0**2)))
        err=(x0-x1)/x1        
        numIter+=1
        x0=x1
        print('{:2}   {:.15f}   {:.2e}'.format(numIter,x1,err))      
    return x1,numIter

//generic method

import numpy as np


def function(f,h,x0,tol,maxIter):
    numIter=0
    err=tol+1
    print('{:2}    {:.15f}'.format(numIter,x0))
    while numIter<maxIter and err>tol:
        den=f(x0+h)-f(x0-h)
        if den==0:
            print('null denominator')
            numIter=-1
            return x0,numIter
        fx0=f(x0)
        delta=(-2)*h*(f(x0)/den)
        x1=x0+delta
        err=abs(delta)/abs(x1)
        numIter+=1
        print('{:2}    {:.15f}   {:.2e}'.format(numIter,x1,err))
        x0=x1
        sol=x1
    return sol,numIter

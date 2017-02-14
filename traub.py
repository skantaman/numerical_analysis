//Traub method

import numpy as np

def traub(f,df,x0,tol,maxIter):
    numIter=0
    err=tol+1
    print('{:2}    {:.15f}'.format(numIter,x0))
    while err>tol and numIter<maxIter:
        den=df(x0)
        if den==0:
            print('null denominator')
            numIter=-1
            return x0,numIter
        fx0=f(x0)
        delta=-fx0/den
        y0=x0+delta
        fy0=f(y0)
        x1=y0-(fy0/den)
        err=abs(delta)/abs(x1)
        numIter+=1
        print('{:2}    {:.15f}    {:.2e}'.format(numIter,x1,err))
        x0=x1
    return x1,numIter

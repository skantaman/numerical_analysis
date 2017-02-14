//Secant method

import numpy as np

def secant(f,x0,x1,tol,nmax):
    nit=0
    err=tol+1
    print('{:2}    {:.15f}   {:.15f}'.format(nit,x0,x1))
    while err>tol and nit<nmax:
        den=f(x1)-f(x0)
        if den==0:
            print('null denominator')
            nit=-1
            return x0,x1,nit
        fx0=f(x0)
        fx1=f(x1)
        delta= (-fx1*(x1-x0))/den
        x2=x1+delta        
        err=abs(delta)
        nit+=1
        print('{:2}   {:.15f}   {:2e}'.format(nit,x2,err))
        x1=x2
    return x2,nit

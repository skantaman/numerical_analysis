//method of the subsequent bisections

import numpy as np

def bisections(f,a,b,tol,nmax):
    nit=0
    x=.5*(a+b)
    err=.5*(b-a)
    print('{:2}   {:.15f}   {:.2e}'.format(nit,x,err))
    fa=f(a)
    while err>tol and nit<nmax:
        fx=f(x)
        if fa*fx<0:
            b=x
        else:
            a=x
            fa=fx
        x=.5*(a+b)
        err=.5*err
        nit+=1
        print ('{:2}    {:.15f}   {:.2e}'.format(nit,x,err))
    return x,nit

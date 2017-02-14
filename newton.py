//Newton method

def newton(f,df,x0,tol,nmax):
    nit=0
    err=tol+1
    print('{:2}   {:.15f}'.format(nit,x0))
    while err>tol and nit<nmax:
        den=df(x0)
        if den==0:
            print('null denominator')
            nit=-1
            return x0,nit
        fx0=f(x0)
        delta=-fx0/den
        x1=x0+delta
        err=abs(delta)
        nit+=1
        print('{:2}   {:.15f}   {:.2e}'.format(nit,x1,err))
        x0=x1
    return x1,nit

def exponent(x:float) -> float:
    my_sum=0
    cnt=0
    while cnt < 100:
        if cnt==0:
            mone=1
            mehane=1
        else:
            mone *= x
            mehane*=cnt
        my_sum+=mone/mehane
        cnt+=1
    return my_sum

def Ln(x:float) -> float:
    if x<=0:
        return 0
    cnt=0
    while cnt < 100:
        if cnt==0:
            y_n=0
        else:
            y_n = y_n+2*(x-exponent(y_n))/(x+exponent(y_n))
        cnt+=1
    return y_n

def XtimesY(x:float,y:float) -> float:
    if x<=0:
        return 0
    my_pow=exponent(y*Ln(x))
    return my_pow

def sqrt(x:float,y:float) -> float:
    if x<=0:
        return 0
    my_sqrt=XtimesY(y,1/x)
    return my_sqrt

def calculate(x:float) -> float:
    my_calc = exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    return float('%0.6f' % my_calc)
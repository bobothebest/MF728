# author: DUAN LINKUO
# email address:lkduan@bu.edu
import numpy as np
from scipy.optimize import fsolve
def swap_to_forward_1Y(sw1):
    def swap_present_value(f1):
        PV = sw1 /(1+0.5*f1)  + sw1  / (1+0.5*f1)**2
        #PV=sum([C/(1+r/2)**i for i in range(1,2*t+1)])+1/(1+r/2)**(2*t)
        return PV-f1 /(1+0.5*f1)  - f1  / (1+0.5*f1)**2
    forward_rate = fsolve(swap_present_value, sw1)
    return forward_rate[0] 
f1=swap_to_forward_1Y( 2.8438/100)
D1=1  / (1+0.5*f1)**2

def swap_to_forward_2Y(sw2,f1):
    def swap_present_value(f2):
        PV=sw2/(1+0.5*f1) +sw2/(1+0.5*f1)**2+sw2/((1+0.5*f1)**2*(1+0.5*f2))+sw2/((1+0.5*f1)**2*(1+0.5*f2)**2)
        PV2=f1/(1+0.5*f1) +f1/(1+0.5*f1)**2+f2/((1+0.5*f1)**2*(1+0.5*f2))+f2/((1+0.5*f1)**2*(1+0.5*f2)**2)
        return PV- PV2
    forward_rate_2Y = fsolve(swap_present_value, sw2)
    return forward_rate_2Y[0]  
f2=swap_to_forward_2Y(3.060/100,f1)
D2=D1/((1+0.5*f2)**2)

def swap_to_forward_3Y(sw3,f1,f2):
    def swap_present_value(f3):
        PV=sw3/(1+0.5*f1)+sw3/(1+0.5*f1)**2+sw3/((1+0.5*f1)**2*(1+0.5*f2))+sw3/((1+0.5*f1)**2*(1+0.5*f2)**2)+sw3/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+f3*0.5))+sw3/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2)
        PV2=f1/(1+0.5*f1)+f1/(1+0.5*f1)**2+f2/((1+0.5*f1)**2*(1+0.5*f2))+f2/((1+0.5*f1)**2*(1+0.5*f2)**2)+f3/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+f3*0.5))+f3/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2)
        return PV- PV2
    forward_rate_3Y = fsolve(swap_present_value, sw3)
    return forward_rate_3Y[0]  
f3=swap_to_forward_3Y(0.03126, f1, f2)
D3=D2/(1+0.5*f3)**2

def swap_to_forward_4Y(sw4,f1,f2,f3):
    def swap_present_value(f4):
        PV=sw4/(1+0.5*f1)+sw4/(1+0.5*f1)**2+sw4/((1+0.5*f1)**2*(1+0.5*f2))+sw4/((1+0.5*f1)**2*(1+0.5*f2)**2)+sw4/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+f3*0.5))+sw4/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2)+sw4/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4))+sw4/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4)**2)
        PV2=f1/(1+0.5*f1)+f1/(1+0.5*f1)**2+f2/((1+0.5*f1)**2*(1+0.5*f2))+f2/((1+0.5*f1)**2*(1+0.5*f2)**2)+f3/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+f3*0.5))+f3/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2)+f4/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4))+f4/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4)**2)
        return PV- PV2
    forward_rate_4Y = fsolve(swap_present_value, sw4)
    return forward_rate_4Y[0]  
f4=swap_to_forward_4Y(0.03144, f1, f2,f3)
D4=D3/(1+0.5*f4)**2

def swap_to_forward_5Y(sw5,f1,f2,f3,f4):
    def swap_present_value(f5):
        PV=sw5*sum((1+0.5*f1)**-i for i in range(1,3))+sw5/((1+0.5*f1)**2*(1+0.5*f2))+sw5/((1+0.5*f1)**2*(1+0.5*f2)**2)+sw5/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+f3*0.5))+sw5/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2)+sw5/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4))+sw5/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4)**2)+sw5/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4)**2*(1+0.5*f5))+sw5/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4)**2*(1+0.5*f5)**2)
        PV2=f1/(1+0.5*f1)+f1/(1+0.5*f1)**2+f2/((1+0.5*f1)**2*(1+0.5*f2))+f2/((1+0.5*f1)**2*(1+0.5*f2)**2)+f3/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+f3*0.5))+f3/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2)+f4/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4))+f4/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4)**2)+f5/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4)**2*(1+0.5*f5))+f5/((1+0.5*f1)**2*(1+0.5*f2)**2*(1+0.5*f3)**2*(1+0.5*f4)**2*(1+0.5*f5)**2)
        return PV- PV2
    forward_rate_5Y = fsolve(swap_present_value, sw5)
    return forward_rate_5Y[0]  
f5=swap_to_forward_5Y(0.0315, f1, f2,f3,f4)
D5=D4/(1+0.5*f5)**2
def swap_to_forward_7Y(sw7,f1,f2,f3,f4,f5):
    def swap_present_value(f7):
        PV=sw7*sum((1+0.5*f1)**-i for i in range(1,3))+sw7*D1*sum((1+0.5*f2)**-i for i in range(1,3))+sw7*D2*sum((1+0.5*f3)**-i for i in range(1,3))+sw7*D3*sum((1+0.5*f4)**-i for i in range(1,3))+sw7*D4*sum((1+0.5*f5)**-i for i in range(1,3))+sw7*D5*sum((1+0.5*f7)**-i for i in range(1,5))
        PV2=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))+f5*D4*sum((1+0.5*f5)**-i for i in range(1,3))+f7*D5*sum((1+0.5*f7)**-i for i in range(1,5))
        return PV- PV2
    forward_rate_7Y = fsolve(swap_present_value, sw7)
    return forward_rate_7Y[0]  
f7=swap_to_forward_7Y(0.03169, f1, f2,f3,f4,f5)
D7=D5/(1+f7*0.5)**4

def swap_to_forward_10Y(sw10,f1,f2,f3,f4,f5,f7):
    def swap_present_value(f10):
        PV=sw10*sum((1+0.5*f1)**-i for i in range(1,3))+sw10*D1*sum((1+0.5*f2)**-i for i in range(1,3))+sw10*D2*sum((1+0.5*f3)**-i for i in range(1,3))+sw10*D3*sum((1+0.5*f4)**-i for i in range(1,3))+sw10*D4*sum((1+0.5*f5)**-i for i in range(1,3))+sw10*D5*sum((1+0.5*f7)**-i for i in range(1,5))+sw10*D7*sum((1+0.5*f10)**-i for i in range(1,7))
        PV2=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))+f5*D4*sum((1+0.5*f5)**-i for i in range(1,3))+f7*D5*sum((1+0.5*f7)**-i for i in range(1,5))+f10*D7*sum((1+0.5*f10)**-i for i in range(1,7))
        return PV- PV2
    forward_rate_10Y = fsolve(swap_present_value, sw10)
    return forward_rate_10Y[0]  
f10=swap_to_forward_10Y(0.0321, f1, f2,f3,f4,f5,f7)
D10=D7/(1+f10*0.5)**6

def swap_to_forward_30Y(sw30,f1,f2,f3,f4,f5,f7,f30):
    def swap_present_value(f30):
        PV=sw30*sum((1+0.5*f1)**-i for i in range(1,3))+sw30*D1*sum((1+0.5*f2)**-i for i in range(1,3))+sw30*D2*sum((1+0.5*f3)**-i for i in range(1,3))+sw30*D3*sum((1+0.5*f4)**-i for i in range(1,3))+sw30*D4*sum((1+0.5*f5)**-i for i in range(1,3))+sw30*D5*sum((1+0.5*f7)**-i for i in range(1,5))+sw30*D7*sum((1+0.5*f10)**-i for i in range(1,7))+sw30*D10*sum((1+0.5*f30)**-i for i in range(1,41))
        PV2=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))+f5*D4*sum((1+0.5*f5)**-i for i in range(1,3))+f7*D5*sum((1+0.5*f7)**-i for i in range(1,5))+f10*D7*sum((1+0.5*f10)**-i for i in range(1,7))+f30*D10*sum((1+0.5*f30)**-i for i in range(1,41))
        return PV- PV2
    forward_rate_30Y = fsolve(swap_present_value, sw30)
    return forward_rate_30Y[0]  
f30=swap_to_forward_30Y(0.03237, f1, f2,f3,f4,f5,f7,f10)
D30=D10/(1+f30*0.5)**20

# (a)
f1
# (b)
f2
# (c)
f_list=[f1,f2,f3,f4,f5,f7,f10,f30]
f_list
# (d)
def sw15(f1,f2,f3,f4,f5,f7,f10,f30):
    PV=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))+f5*D4*sum((1+0.5*f5)**-i for i in range(1,3))+f7*D5*sum((1+0.5*f7)**-i for i in range(1,5))+f10*D7*sum((1+0.5*f10)**-i for i in range(1,7))+f30*D10*sum((1+0.5*f30)**-i for i in range(1,11))
    PV/=sum((1+0.5*f1)**-i for i in range(1,3))+D1*sum((1+0.5*f2)**-i for i in range(1,3))+D2*sum((1+0.5*f3)**-i for i in range(1,3))+D3*sum((1+0.5*f4)**-i for i in range(1,3))+D4*sum((1+0.5*f5)**-i for i in range(1,3))+D5*sum((1+0.5*f7)**-i for i in range(1,5))+D7*sum((1+0.5*f10)**-i for i in range(1,7))+D10*sum((1+0.5*f30)**-i for i in range(1,11))
    return PV
sw15(f1, f2, f3, f4, f5, f7, f10, f30)

# (e)
D_list=[D1,D2,D3,D4,D5,D7,D10,D30]
zero_list=[np.log(D)/-T for D,T in zip(D_list,[1,2,3,4,5,7,10,30])]

# (f)
def f_add(f_list,basis_list):
    for i in range(len(f_list)):
        f_list[i]+=basis_list[i]
    f1,f2,f3,f4,f5,f7,f10,f30=f_list
    sw1=f1*sum((1+0.5*f1)**-i for i in range(1,3))/sum((1+0.5*f1)**-i for i in range(1,3))
    D1=D1=1  / (1+0.5*f1)**2
    sw2=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))
    sw2/=sum((1+0.5*f1)**-i for i in range(1,3))+D1*sum((1+0.5*f2)**-i for i in range(1,3))
    D2=D1/(1+0.5*f2)**2
    sw3=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))
    sw3/=sum((1+0.5*f1)**-i for i in range(1,3))+D1*sum((1+0.5*f2)**-i for i in range(1,3))+D2*sum((1+0.5*f3)**-i for i in range(1,3))
    D3=D2/(1+0.5*f3)**2
    sw4=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))
    sw4/=sum((1+0.5*f1)**-i for i in range(1,3))+D1*sum((1+0.5*f2)**-i for i in range(1,3))+D2*sum((1+0.5*f3)**-i for i in range(1,3))+D3*sum((1+0.5*f4)**-i for i in range(1,3))
    D4=D3/(1+0.5*f4)**2
    sw5=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))+f5*D4*sum((1+0.5*f5)**-i for i in range(1,3))
    sw5/=sum((1+0.5*f1)**-i for i in range(1,3))+D1*sum((1+0.5*f2)**-i for i in range(1,3))+D2*sum((1+0.5*f3)**-i for i in range(1,3))+D3*sum((1+0.5*f4)**-i for i in range(1,3))+D4*sum((1+0.5*f5)**-i for i in range(1,3))
    D5=D4/(1+0.5*f5)**2
    sw7=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))+f5*D4*sum((1+0.5*f5)**-i for i in range(1,3))+f7*D5*sum((1+0.5*f7)**-i for i in range(1,5))
    sw7/=sum((1+0.5*f1)**-i for i in range(1,3))+D1*sum((1+0.5*f2)**-i for i in range(1,3))+D2*sum((1+0.5*f3)**-i for i in range(1,3))+D3*sum((1+0.5*f4)**-i for i in range(1,3))+D4*sum((1+0.5*f5)**-i for i in range(1,3))+D5*sum((1+0.5*f7)**-i for i in range(1,5))
    D7=D5/(1+0.5*f7)**4
    sw10=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))+f5*D4*sum((1+0.5*f5)**-i for i in range(1,3))+f7*D5*sum((1+0.5*f7)**-i for i in range(1,5))+f10*D7*sum((1+0.5*f10)**-i for i in range(1,7))
    sw10/=sum((1+0.5*f1)**-i for i in range(1,3))+D1*sum((1+0.5*f2)**-i for i in range(1,3))+D2*sum((1+0.5*f3)**-i for i in range(1,3))+D3*sum((1+0.5*f4)**-i for i in range(1,3))+D4*sum((1+0.5*f5)**-i for i in range(1,3))+D5*sum((1+0.5*f7)**-i for i in range(1,5))+D7*sum((1+0.5*f10)**-i for i in range(1,7))
    D10=D7/(1+0.5*f10)**6
    sw30=f1*sum((1+0.5*f1)**-i for i in range(1,3))+f2*D1*sum((1+0.5*f2)**-i for i in range(1,3))+f3*D2*sum((1+0.5*f3)**-i for i in range(1,3))+f4*D3*sum((1+0.5*f4)**-i for i in range(1,3))+f5*D4*sum((1+0.5*f5)**-i for i in range(1,3))+f7*D5*sum((1+0.5*f7)**-i for i in range(1,5))+f10*D7*sum((1+0.5*f10)**-i for i in range(1,7))+f30*D10*sum((1+0.5*f30)**-i for i in range(1,41))
    sw30/=sum((1+0.5*f1)**-i for i in range(1,3))+D1*sum((1+0.5*f2)**-i for i in range(1,3))+D2*sum((1+0.5*f3)**-i for i in range(1,3))+D3*sum((1+0.5*f4)**-i for i in range(1,3))+D4*sum((1+0.5*f5)**-i for i in range(1,3))+D5*sum((1+0.5*f7)**-i for i in range(1,5))+D7*sum((1+0.5*f10)**-i for i in range(1,7))+D10*sum((1+0.5*f30)**-i for i in range(1,41))
    return sw1,sw2,sw3,sw4,sw5,sw7,sw10,sw30
basis_list=[0.01 for i in range(8)]
sw1,sw2,sw3,sw4,sw5,sw7,sw10,sw30=f_add(f_list, basis_list)
sw1,sw2,sw3,sw4,sw5,sw7,sw10,sw30

# (g)
swap_list=[0.028438,0.03060,0.03126,0.03144,0.03150,0.03169,0.03210,0.03237]
basis_list=[0,0,0,0.0005,0.001,0.0015,0.0025,0.005]
sw1,sw2,sw3,sw4,sw5,sw7,sw10,sw30=[sw+basis for sw,basis in zip(swap_list,basis_list)]

# (h)
f1=swap_to_forward_1Y(sw1)
D1=1  / (1+0.5*f1)**2
f2=swap_to_forward_2Y(sw2,f1)
D2=D1/((1+0.5*f2)**2)
f3=swap_to_forward_3Y(sw3, f1, f2)
D3=D2/(1+0.5*f3)**2
f4=swap_to_forward_4Y(sw4, f1, f2,f3)
D4=D3/(1+0.5*f4)**2
f5=swap_to_forward_5Y(sw5, f1, f2,f3,f4)
D5=D4/(1+0.5*f5)**2
f7=swap_to_forward_7Y(sw7, f1, f2,f3,f4,f5)
D7=D5/(1+f7*0.5)**4
f10=swap_to_forward_10Y(sw10, f1, f2,f3,f4,f5,f7)
D10=D7/(1+f10*0.5)**6
f30=swap_to_forward_30Y(sw30, f1, f2,f3,f4,f5,f7,f10)
D30=D10/(1+f30*0.5)**20
f_list_new=[f1,f2,f3,f4,f5,f7,f10,f30]

# (i)
swap_list=[0.028438,0.03060,0.03126,0.03144,0.03150,0.03169,0.03210,0.03237]
basis_list=[-0.005,-0.0025,-0.0015,-0.001,-0.0005,0,0,0]
sw1,sw2,sw3,sw4,sw5,sw7,sw10,sw30=[sw+basis for sw,basis in zip(swap_list,basis_list)]

# (j)
f1=swap_to_forward_1Y(sw1)
D1=1  / (1+0.5*f1)**2
f2=swap_to_forward_2Y(sw2,f1)
D2=D1/((1+0.5*f2)**2)
f3=swap_to_forward_3Y(sw3, f1, f2)
D3=D2/(1+0.5*f3)**2
f4=swap_to_forward_4Y(sw4, f1, f2,f3)
D4=D3/(1+0.5*f4)**2
f5=swap_to_forward_5Y(sw5, f1, f2,f3,f4)
D5=D4/(1+0.5*f5)**2
f7=swap_to_forward_7Y(sw7, f1, f2,f3,f4,f5)
D7=D5/(1+f7*0.5)**4
f10=swap_to_forward_10Y(sw10, f1, f2,f3,f4,f5,f7)
D10=D7/(1+f10*0.5)**6
f30=swap_to_forward_30Y(sw30, f1, f2,f3,f4,f5,f7,f10)
D30=D10/(1+f30*0.5)**20
f_list_new=[f1,f2,f3,f4,f5,f7,f10,f30]


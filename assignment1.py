import numpy as np

def find_period(L0,L1):
    
    if L0 <= 0 or L1 <=0:
        print("must be greater than 0")
        
    if L1 <= L0:
        print("l0 must be greater than L1")
        
    for L in range (L0,L1+1,1):
        g = 9.8 # in m/s^2
        T = 2 * np.pi * (np.sqrt(L/g)) # in s
        print("when L = %3.1f m, T = %2.1f s" %(L,T))
        T0 = T 
        T1 = T
        
    return T0, T1
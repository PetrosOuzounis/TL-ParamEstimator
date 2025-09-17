from scipy.special import expi,wrightomega
from numpy import *
from scipy.optimize import minimize_scalar

"function-calculator of a and Ca parameters and the symetrical factors"

def coefficients_calc(T1,T2,Tmax,Intensity_max,n_0,nm,bita):
    
    omega=abs(T1-T2)
    thelta=T2-Tmax
    tau=Tmax-T1
    Comega=(omega*Intensity_max)/(bita*n_0)
    Cthelta=(thelta*Intensity_max)/(bita*nm)
    Ctau=(tau*Intensity_max)/(bita*(n_0-nm))
    mg=thelta/omega
    mg_tone=nm/n_0
    
    return float(omega),float(thelta),float(tau),float(Comega),float(Cthelta),float(Ctau),float(mg),float(mg_tone)

"function-calculator of b-gen, using the Im/nm equation within an iteration"

def function_of_b(E,Tmax,mg_tone):
    
    k_b=8.617e-5
    b_initial=0
    diff=1e5 
    
    for i in range(1,30000):
        b=1+ i/10000
        Dm=(2*k_b*Tmax)/E
        fun_b=(b/(1+(b-1)*Dm))**(-1/(b-1))
        result=abs(mg_tone-fun_b)
        if result<diff:
            diff=result
            b_initial=b
   
    b_root=b_initial
    
    return float(b_root)

"function-calculator of a-mix "   

def function_of_a(mg_tone):
    dif=1e5 
    a_initial=0
    for i in range(1,10000):
        a=0+i/10000
        Fun=(1-a)/(2.58226 - 3.13911*a + 0.55071*a**2)
        result=abs(mg_tone-Fun)
        if result<dif:
            a_initial=a
            dif=result
    a_root=a_initial
   
    Fm=(2.58226 - 2.13911*a_root + 0.55071*a_root**2)
    bmix=(1+a_root/Fm)
    
    return float(a_root),float(bmix)

"function-calculator of R within a range of An values"

def function_of_R(E,Tmax,n_0,nm):
    
    k_b=8.617e-5
    R_initial=0
    best_result=1e5 
    mg_tone=nm/n_0
    Dm=2*k_b*Tmax/E
    for i in range(1,90000):
        
        R=i/100000
        FTL=(1-1.05*R**1.26)
        zm=(R/(1-R))-log((1-R)/R)+(1-Dm)/FTL
        Wzm=wrightomega(zm)
        result=abs(mg_tone-(R/((1-R)*Wzm)))
                
        if result<best_result:
            best_result=result
            R_initial=R
    best_R=R_initial
    FTL=(1-1.05*best_R**1.26) 
    zm=(best_R/(1-best_R))-log((1-best_R)/best_R)+(1-Dm)/FTL
    Wzm=wrightomega(zm)
    FR=(FTL/best_R)*(Wzm+Wzm**2)
    
    Am=1e-7
    An=best_R*Am
    return float(Wzm),float(best_R),An    
     
"function-calculator of r within a range of An values"

def function_of_r(E,Tmax,n_0,nm):
    
    k_b=8.617e-5
    r_initial=0
    best_result=1e5  
    mg_tone=nm/n_0
    Dm=2*k_b*Tmax/E
    for i in range(1,100000):
        
        r=i/100000
        z=r+log(r)+(1-Dm)*(1+0.7617*(r)**1.1486)
        Wz=wrightomega(z)
        result=abs(mg_tone-(r/Wz))
                
        if result<best_result:
            best_result=result
            r_initial=float(r)
   
    best_r=r_initial
    
    if best_r==1:
        def f_r(r):
            Dm=2*k_b*Tmax/E
            z=r+log(r)+(1-Dm)*(1+0.7617*(r)**1.1486)
            Wz=wrightomega(z)
            return abs(mg_tone-(r/Wz))

        # Minimize the residual function for r in (0, 1)
        result = minimize_scalar(f_r, bounds=(1e-6, 1e6), method='bounded')
        best_r = result.x
    
   
    zm=best_r+log(best_r)+(1-Dm)*(1+0.7617*(best_r)**1.1486)
    Wzm=wrightomega(zm)
    Am=1e-7
    AD=best_r*Am
    return Wzm,best_r,AD

"function-calculator of Energy GOK"

def Energy_calc_gok(E,Tmax,mg_tone,b,omega,thelta,tau,Comega,Cthelta,Ctau):
    
    k_b=8.617e-5
    Dm=(2*k_b*Tmax)/E
    mg_new=(b/(1+(b-1)*Dm))**(-1/(b-1))
    Eomega=(Comega*b*k_b*Tmax**2)/(mg_new*omega)
    Ethelta=Cthelta*b*(k_b*Tmax**2/thelta)
    Etau=Ctau*b*((1/mg_new)-1)*(k_b*Tmax**2/tau)
    
    return Eomega,Ethelta,Etau

"function-calculator of Energy MOK"

def Energy_calc_mok(a_root,mg_tone,Tmax,omega,thelta,tau,Comega,Cthelta,Ctau):
    
    k_b=8.617e-5
    a=a_root
    Fm=2.58226 - 2.13911*a + 0.55071*a**2
    bmix=(1+a/Fm)
    mg_new=(1-a)/(Fm-a)
    Eomega_mix=(Comega*bmix*k_b*Tmax**2)/(mg_new*omega)
    Ethelta_mix=Cthelta*bmix*(k_b*Tmax**2/thelta)
    Etau_mix=Ctau*bmix*((1/mg_new)-1)*(k_b*Tmax**2/tau)
    
    return Eomega_mix,Ethelta_mix,Etau_mix

"function-calculator of Energy DOTOR"

def Energy_calc_DOTOR(Wz,nm,n_0,R_root,omega,thelta,tau,Comega,Cthelta,Ctau,Tmax):
   k_b=8.617e-5
   mg_tone=nm/n_0
   FTL=(1-1.05*R_root**1.26)
   FR=(FTL/R_root)*(Wz+Wz**2)
   Eomega=(Comega*k_b*Tmax**2)*FR/omega
   Ethelta=Cthelta*mg_tone*FR*(k_b*Tmax**2/thelta)
   Etau=Ctau*(1-mg_tone)*FR*(k_b*Tmax**2/tau)
   
   return Eomega,Ethelta,Etau

"function-calculator of Energy LOTOR"

def Energy_calc_LOTOR(Wz,nm,n_0,r_root,omega,thelta,tau,Comega,Cthelta,Ctau,Tmax):
    k_b=8.617e-5
    mg_tone=nm/n_0
    FTL=(1+0.7617*(r_root)**1.1486)
    FR=(1/(r_root*FTL))*(Wz+Wz**2)
    Eomega=(Comega*k_b*Tmax**2)*FR/omega
    Ethelta=Cthelta*mg_tone*FR*(k_b*Tmax**2/thelta)
    Etau=Ctau*(1-mg_tone)*FR*(k_b*Tmax**2/tau)
    
    return Eomega,Ethelta,Etau

"Error calculation based on Einitial"

def En_error(Eomega,Eomeg):
    
    Error=abs((Eomega-Eomeg)/Eomega)*100
    
    return Error

"Frequency factor based on initial activation energy and order kinetics"

def frequency_factor(Einput,Tmax,bita,b):
    k_b=8.617e-5
    E=Einput
    s=(bita/Tmax**2)*(E/k_b)*(1/(1+(1-b)*(2*k_b*Tmax/E)))*exp(E/(k_b*Tmax))
    f_s="{:.3e}".format(s)
    return f_s

"OTOR's frequency factor based on Einitial and ratio"

def frequency_factor_OTOR(Einput,Tmax,bita,R):
    k_b=8.617e-5
    E=Einput
    exp_part=exp(E/(k_b*Tmax))
    # Your formula, now using mpmath for the exponential part
    s_calc=bita*E*exp_part/(k_b*Tmax**2*(1+0.7617326*R**1.1485711))
    f_s="{:.3e}".format(s_calc)
    return f_s

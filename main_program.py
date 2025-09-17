from prettytable import PrettyTable
from PSM_functions import coefficients_calc, function_of_b, function_of_a,function_of_R, function_of_r, Energy_calc_gok, Energy_calc_mok, Energy_calc_DOTOR, Energy_calc_LOTOR,En_error,frequency_factor,frequency_factor_OTOR
from Tables import GOK_Table, MOK_Table, D_OTOR_Table, L_OTOR_Table

def GOK(T1,Tmax,T2,Im,n_0,nm,bita):
    
    coefficients_results=coefficients_calc(T1, T2, Tmax, Im, n_0, nm, bita)
    omega,thelta,tau,Comega,Cthelta,Ctau,mg,mg_tone=coefficients_results
    k_b=8.617e-5
    
    "First calculation of Activation energy"
    
    E_initial=1
    b=function_of_b(E_initial,Tmax,mg_tone)
    Energy_of_gok_results=Energy_calc_gok(E_initial,Tmax, mg_tone, b, omega, thelta, tau, Comega, Cthelta, Ctau)
    Eomeg,_,_=Energy_of_gok_results
    
    "Second calculation of Activation energy"
    
    b1=function_of_b(Eomeg, Tmax, mg_tone)
    Energy_of_gok_results=Energy_calc_gok(Eomeg,Tmax, mg_tone, b1, omega, thelta, tau, Comega, Cthelta, Ctau)
    Eomega,_,_=Energy_of_gok_results
          
    s=frequency_factor(Eomeg, Tmax, bita, b)
    Error=En_error(Eomega,Eomeg)
    
    print("Would you like to save results ?")
    input1=input("y/n: ").lower()
    print("\n")
    
    tables= GOK_Table(T1,T2,Tmax,Im,n_0,nm,mg,mg_tone,b1,omega,thelta,tau,Comega,Cthelta,Ctau,Eomega,s,bita,Error,input1)
    print(tables)
    #print(Eomeg1,"\n",b1)
    
def MOK(T1,Tmax,T2,Im,n_0,nm,bita):
    k_b=8.617e-5
    coefficients_results=coefficients_calc(T1, T2, Tmax, Im, n_0, nm, bita)
    omega,thelta,tau,Comega,Cthelta,Ctau,mg,mg_tone=coefficients_results
    
    "First calculation of Activation energy"
    
    E_initial=1
    b=function_of_b(E_initial,Tmax,mg_tone)
    Energy_of_gok_results=Energy_calc_gok(E_initial,Tmax, mg_tone, b, omega, thelta, tau, Comega, Cthelta, Ctau)
    Eomeg,Ethel,Eta=Energy_of_gok_results
    
    "Second calculation of Activation energy"
    
    #b1=function_of_b(Eomeg, Tmax, mg_tone)
    #Energy_of_gok_results=Energy_calc_gok(Eomeg,Tmax, mg_tone, b1, omega, thelta, tau, Comega, Cthelta, Ctau)
    #Eomeg1,_,_=Energy_of_gok_results
    
    "Third calculation of Activation Energy"
    
    a_root,bmix=function_of_a(mg_tone)       
    Energy_of_mok_results=Energy_calc_mok(a_root,mg_tone, Tmax, omega, thelta, tau, Comega, Cthelta, Ctau)
    Eomega_mix,Ethelta_mix,Etau_mix=Energy_of_mok_results
    s=frequency_factor(Eomeg, Tmax, bita, b)
    Error=En_error(Eomega_mix,Eomeg)
   
    
    print("Would you like to save results ?")
    input1=input("y/n: ").lower()
    print("\n")
    
    tables=MOK_Table(T1,T2,Tmax,Im,n_0,nm,mg,mg_tone,a_root,bmix,omega,thelta,tau,Comega,Cthelta,Ctau,Eomega_mix,s,bita,Error,input1)
    print(tables)
    

def D_OTOR(T1,Tmax,T2,Im,n_0,nm,bita):
    k_b=8.617e-5
    Am=1e-7
    coefficients_results=coefficients_calc(T1, T2, Tmax, Im, n_0, nm,bita)
    omega,thelta,tau,Comega,Cthelta,Ctau,mg,mg_tone=coefficients_results
    
    "First calculation of Activation energy"
    
    E_initial=1
    Wzm1,R1,An1=function_of_R(E_initial,Tmax,n_0, nm)
    Energy_of_DOTOR=Energy_calc_DOTOR(Wzm1,nm,n_0,R1,omega,thelta,tau,Comega,Cthelta,Ctau,Tmax)
    Eomeg1,Ethelt,Eta=Energy_of_DOTOR
    
    "Second calculation of Activation energy"
    
    E_initial1=Eomeg1
    Wzm2,R2,An2=function_of_R(E_initial1,Tmax,n_0, nm)
    Energy_of_DOTOR=Energy_calc_DOTOR(Wzm2,nm,n_0,R2,omega,thelta,tau,Comega,Cthelta,Ctau,Tmax)
    Eomega,Ethelt,Eta=Energy_of_DOTOR
    
    s=frequency_factor_OTOR(Eomeg1, Tmax, bita, R1)
    Error=En_error(Eomega,Eomeg1)
    
    print("Would you like to save results ?")
    input1=input("y/n: ").lower()
    print("\n")
    
    tables=D_OTOR_Table(T1,T2,Tmax,Im,n_0,nm,mg,mg_tone,Am,An2,R2,omega,thelta,tau,Comega,Cthelta,Ctau,Eomega,s,bita,Error,input1)
    print(tables)


def L_OTOR(T1,Tmax,T2,Im,n_0,nm,bita):
    k_b=8.617e-5
    Am=1e-7
    coefficients_results=coefficients_calc(T1, T2, Tmax, Im, n_0, nm, bita)
    omega,thelta,tau,Comega,Cthelta,Ctau,mg,mg_tone=coefficients_results
    
    "First calculation of Activation energy"
    
    E_initial=1
    Wzm,r,AD=function_of_r(E_initial,Tmax,n_0,nm)
    Energy_of_LOTOR=Energy_calc_LOTOR(Wzm,nm,n_0,r,omega,thelta,tau,Comega,Cthelta,Ctau,Tmax)
    Eomeg1,Ethelt,Eta=Energy_of_LOTOR
    
    "Second calculation of Activation energy"
    
    E_initial2=Eomeg1
    Wzm1,r1,AD1=function_of_r(E_initial2,Tmax,n_0,nm)
    Energy_of_LOTOR=Energy_calc_LOTOR(Wzm1,nm,n_0,r1,omega,thelta,tau,Comega,Cthelta,Ctau,Tmax)
    Eomega,Ethelt,Eta=Energy_of_LOTOR
    
    s=frequency_factor_OTOR(Eomeg1, Tmax, bita, r1)
    Error=En_error(Eomega,Eomeg1)
    
    print("Would you like to save results ?")
    input1=input("y/n: ").lower()
    print("\n")
    
    tables=L_OTOR_Table(T1,T2,Tmax,Im,n_0,nm,mg,mg_tone,Am,AD1,r1,omega,thelta,tau,Comega,Cthelta,Ctau,Eomega,s,bita,Error,input1)
    print(tables)

"Table presentation"


Table1=PrettyTable()
Table1.title="Valid inputs for each model"
Table1.field_names=["For Models","Enter"]
Table1.add_row(["General order kinetics","gok"])
Table1.add_row(["Mixed order kinetics","mok"])
Table1.add_row(["Localized One Trap One Recombination","lotor"])
Table1.add_row(["Delocalized One Trap One Recombination","dotor"])
Table1.align = "l"

general_order_inputs=["general order kinetics", "g.ok", "general", "gok", "go"]
mixed_order_inputs=["mixed order kinetics", "m.ok", "mixed", "mok", "mo"]
l_otor_inputs=["localized","l otor","localized otor","l","lotor"]
d_otor_inputs=["delocalized","d otor","delocalized otor","d","dotor"]

# Store user input data
stored_data = {}
#stored_data_test={}
# Iteration program

    

while True:
    print(Table1)
    Test_input=input("Would you like to run a Test? (y/n):").strip().lower()
    if Test_input=="y":
        model_input_Test=input("In order to run a test you must select a model. Enter a model:")
        if model_input_Test in general_order_inputs + mixed_order_inputs + l_otor_inputs + d_otor_inputs:
            print("Based on this model insert the following data Test")
            
            Im=float(input("For maximum Intensity insert 80826.0, then press enter:")) 
            Tmax=float(input("For the maximum Temperature insert 354.0, then press enter:"))
            T1=float(input("For Temperature in the rising section of the TL glow curve insert 338.0, then press enter: "))
            T2=float(input("For Temperature in the falling section of the TL glow curve 365.0, then press enter: ")) 
            n_0=float(input("For total integrated signal of the TL peak n(0) insert 2440021.0, then press enter: "))
            nm=float(input("For high temperature half (right) integral of the TL peak n(m) insert 984822.0, then press enter: "))
            bita=float(input("Insert the heating rate as 1, then press enter:"))
            if model_input_Test in general_order_inputs:
                GOK(T1,Tmax,T2,Im,n_0,nm,bita)
            elif model_input_Test in mixed_order_inputs:
                MOK(T1,Tmax,T2,Im,n_0,nm,bita)
            elif model_input_Test in l_otor_inputs:
                L_OTOR(T1,Tmax,T2,Im,n_0,nm,bita)
            elif model_input_Test in d_otor_inputs:
                D_OTOR(T1,Tmax,T2,Im,n_0,nm,bita)
    elif Test_input=="n":
        break
    else:
        print("\n\n\nInsert and Enter y/n")
        
while True: 
    print("\n\n")
    print(Table1)
    # Get user input for model selection
    model_input=input("Insert model or 'exit' to quit: ").strip().lower()
    
    if model_input=="exit":
        print("Program terminated\n")
        break
          
    if model_input in general_order_inputs + mixed_order_inputs + l_otor_inputs + d_otor_inputs:
        
        if stored_data:
            reuse=input("Would you like to reuse the last entered data? (y/n): ").strip().lower()
        else:
            reuse="n"
        
        if reuse!="y":
            # Collect new data
            stored_data["Im"]=float(input("Enter max Intensity: "))
            stored_data["Tmax"]=float(input("Enter Tmax in Kelvin: "))
            stored_data["T1"]=float(input("Enter T1 in Kelvin: "))
            stored_data["T2"]=float(input("Enter T2 in Kelvin: "))
            stored_data["n_0"]=float(input("Enter n(0) total integrated signal of the TL peak: "))
            stored_data["nm"]=float(input("Enter n(m) high temperature half (right) integral of the TL peak: "))
            stored_data["bita"]=float(input("Enter Heating rate in Kelvin/second: "))
        
        # Apply the stored data to the selected model
        if model_input in general_order_inputs:
            GOK(**stored_data)
        elif model_input in mixed_order_inputs:
            MOK(**stored_data)
        elif model_input in l_otor_inputs:
            L_OTOR(**stored_data)
        elif model_input in d_otor_inputs:
            D_OTOR(**stored_data)
    
    else:
        print("\nInvalid input. Please enter 'gok', 'mok', 'dotor', or 'lotor'.")


"""Experimental data """
"""tl(number)c best TL glow curves"""
         
         #bita=0.5
         #Im=6700
         #Tmax=355 
         #T1=338 
         #T2=367 
         #n_0=424461 
         #nm=176815
         
         #bita=1
         #Im=23227.0  #tl1c
         #Tmax=358.0 
         #T1=342.0 
         #T2=369.0 
         #n_0=769407.0 
         #nm=328978.0
         #bita=1
         
         #Im=47108.0  #tl2c
         #Tmax=356.0 
         #T1=339.0 
         #T2=366.0 
         #n_0=1460369.0 
         #nm=559188.0
         #bita=1
         
         #Im=80826.0  #tl3c # it will be used
         #Tmax=354.0 
         #T1=338.0 
         #T2=365.0 
         #n_0=2440021.0 
         #nm=984822.0
         #bita=1
         
         #Im=235.0     #tl3b
         #Tmax=359.0 
         #T1=333.0 
         #T2=379.0 
         #n_0=12347.0 
         #nm=5106.0
         #bita=1
         
         #Im=563.0      #tl3a
         #Tmax=357.0 
         #T1=343.0 
         #T2=375.0 
         #n_0=29200.0 
         #nm=14634.0
         #bita=1
         
         #Im=15194.0   #tl4c
         #Tmax=355.0 
         #T1=339.0 
         #T2=366.0 
         #n_0=493600.0 
         #nm=211440.0
         #bita=1
         
         #Im=389.0     tl4b
         #Tmax=361.0 
         #T1=334.0 
         #T2=374.0 
         #n_0=20003.0 
         #nm=7150.0
         #bita=1
         
         #Im=2026.0    #tl4a
         #Tmax=358.0 
         #T1=339.0 
         #T2=372.0 
         #n_0=82986.0 
         #nm=38818.0
         #bita=1
         
         #Im=41059.0   #tl5c it will be used
         #Tmax=355.0 
         #T1=339.0 
         #T2=366.0 
         #n_0=1283303.0 
         #nm=519374.0
         #bita=1
         
         #Im=588.0    #tl5b
         #Tmax=357.0 
         #T1=342.0 
         #T2=376.0 
         #n_0=25349.0 
         #nm=12290.0
         #bita=1
         
         #Im=4920.0   #tl5a
         #Tmax=360.0 
         #T1=341.0 
         #T2=372.0 
         #n_0=187095.0 
         #nm=77335.0
         #bita=1
         
         #Im=72228.0   #tl6c
         #Tmax=355.0 
         #T1=339.0 
         #T2=366.0 
         #n_0=2210296.0 
         #nm=866902.0
         #bita=1
         
         #Im=422.0    #tl6b
         #Tmax=358.0 
         #T1=341.0 
         #T2=376.0 
         #n_0=22622.0 
         #nm=10590.0
         #bita=1
         
         #Im=5128.0   #tl6a check
         #Tmax=358.0 
         #T1=341.0 
         #T2=373.0 
         #n_0=203123.0 
         #nm=97475.0
         #bita=1
         
         #Im=53124.0  #tl7c it will be used
         #Tmax=352.0 
         #T1=336.0 
         #T2=362.0 
         #n_0=1586602.0 
         #nm=628862.0
         #bita=1
         
         #Im=381.0     #tl7b
         #Tmax=358.0 
         #T1=333.0 
         #T2=373.0 
         #n_0=18941.0 
         #nm=8218.0
         #bita=1
         
         #Im=113830.0   #tl8c it  will be used
         #Tmax=351.0 
         #T1=336.0 
         #T2=361.0 
         #n_0=3310966.0 
         #nm=1308990.0
         #bita=1
         
         #Im=993.0       #tl8b check 
         #Tmax=359.0 
         #T1=340.0 
         #T2=374.0 
         #n_0=41446.0 
         #nm=18362.0
         #bita=1
         
    
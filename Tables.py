from prettytable import PrettyTable
import os
from datetime import datetime
from numpy import log


def save_tables_to_file(input1, tables, model_name):
    
    if input1=="y":
       
        outputs=[str(table)+"\n" for table in tables]

        filename=f"{model_name}_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename,"w",encoding="utf-8") as file:
            for i in outputs:
                file.write(i+"\n")  # Adds a newline after each section
            print(f"Data successfully written to {filename} in the current directory: {os.getcwd()}")

    elif input1=="n":
        pass
    
    else:
        raise ValueError("Input must be y or n")

def GOK_Table(T1,T2,Tmax,Im,n_0,nm,mg,mg_tone,b_root,omega,thelta,tau,Comega,Cthelta,Ctau,Eomega,s,bita,Error,input1):
    table=PrettyTable()
    table.title="Inputs"
    table.field_names=["T1","Tmax","T2","Im","n0","nm","Heating rate"]
    table.add_row([T1,Tmax,T2,Im,n_0,nm,bita])
    
    table1=PrettyTable()
    table1.title="Outputs"
    table1.field_names=["omega","thelta","tau","Comega","Cthelta","Ctau","mg","mg_tone"]
    table1.add_row([round(omega,4), round(thelta,4), round(tau,4), round(Comega,4), round(Cthelta,4), round(Ctau,4), round(mg,4), round(mg_tone,4)])
    
    table2=PrettyTable()
    table2.add_column("General outputs",["b-gen (Order kinetics)","E (Activation energy)","s (frequency factor)"])
    table2.add_column("Values",[round(b_root,4),round(Eomega,4),s])
    table2.add_column("Error %",["-",round(Error,4),"-"])  
    print(table,"\n")
    print(table1,"\n")
    print(table2,"\n")
    
    save_tables_to_file(input1, [table, table1, table2],"General_Order_Kinetics")
   
    return ""

def MOK_Table(T1,T2,Tmax,Im,n_0,nm,mg, mg_tone,a_root,bmix,omega,thelta,tau,Comega,Cthelta,Ctau,Eomega,s,bita,Error,input1):
    table=PrettyTable()
    table.title="Inputs"
    table.field_names=["T1","Tmax","T2","Im","n0","nm","Heating rate"]
    table.add_row([T1,Tmax,T2,Im,n_0,nm,bita])
    
    table1=PrettyTable()
    table1.title="Outputs"
    table1.field_names=["omega","thelta","tau","Comega","Cthelta","Ctau","mg","mg_tone"]
    table1.add_row([round(omega,4), round(thelta,4), round(tau,4), round(Comega,4), round(Cthelta,4), round(Ctau,4), round(mg,4), round(mg_tone,4)])
    
    table2=PrettyTable()
    table2.add_column("Mixed outputs",["a-mix","b_mix (Mixed order kinetics)","E (Activation energy)","s (frequency factor)"])
    table2.add_column("Values",[round(a_root,4),round(bmix,4),round(Eomega,4),s])
    table2.add_column("Error %",["-","-",round(Error,4),"-"])
    
    print(table,"\n")
    print(table1,"\n")
    print(table2,"\n")
    
    save_tables_to_file(input1, [table, table1, table2],"Mixed_Order_Kinetics")
    
    return ""

def D_OTOR_Table(T1,T2,Tmax,Im,n_0,nm,mg,mg_tone,Am,An,R_root,omega,thelta,tau,Comega,Cthelta,Ctau,Eomega,s,bita,Error,input1):
    
    table=PrettyTable()
    table.title="Inputs"
    table.field_names=["T1","Tmax","T2","Im","n0","nm","Heating rate"]
    table.add_row([T1,Tmax,T2,Im,n_0,nm,bita])
    
    table1=PrettyTable()
    table1.title="Outputs 1"
    table1.field_names=["omega","thelta","tau","Comega","Cthelta","Ctau"]
    table1.add_row([round(omega,4), round(thelta,4), round(tau,4), round(Comega,4), round(Cthelta,4), round(Ctau,4)])
    table2=PrettyTable()
    table2.title="Outputs 2"
    table2.field_names=["mg","mg_tone","Am","An"]
    table2.add_row([round(mg,4),round(mg_tone,4),Am,"{:.5e}".format(An)])
    
    table3=PrettyTable()
    table3.add_column("D-OTOR outputs",["E (Activation Energy)","R (Retrapping Ratio)","s (frequency factor)"])
    table3.add_column("Values",[round(Eomega,4),round(R_root,5),s])
    table3.add_column("Error %",[round(Error,4),"-","-"])
      
    print(table,"\n")
    print(table1,"\n")
    print(table2,"\n")
    print(table3,"\n")
    
    save_tables_to_file(input1, [table, table1, table2,table3],"DOTOR")
    
    return ""

def L_OTOR_Table(T1,T2,Tmax,Im,n_0,nm,mg,mg_tone,Am,AD,r_root,omega,thelta,tau,Comega,Cthelta,Ctau,Eomega,s,bita,Error,input1):
    
    table=PrettyTable()
    table.title="Inputs"
    table.field_names=["T1","Tmax","T2","Im","n0","nm","Heating rate"]
    table.add_row([T1,Tmax,T2,Im,n_0,nm,bita])
    
    table1=PrettyTable()
    table1.title="Outputs 1"
    table1.field_names=["omega","thelta","tau","Comega","Cthelta","Ctau"]
    table1.add_row([round(omega,4), round(thelta,4), round(tau,4), round(Comega,4), round(Cthelta,4), round(Ctau,4)])
    table2=PrettyTable()
    table2.title="Outputs 2"
    table2.field_names=["mg","mg_tone","Am","AD"]
    table2.add_row([round(mg,4),round(mg_tone,4),Am,"{:.5e}".format(AD)])
    
    table3=PrettyTable()
    table3.add_column("L-OTOR outputs",["E (Activation Energy)","r (Retrapping Ratio)","s (frequency factor)"])
    table3.add_column("Values",[round(Eomega,4),round(r_root,5),s])
    table3.add_column("Error %",[round(Error,4),"-","-"])
      
    print(table,"\n")
    print(table1,"\n")
    print(table2,"\n")
    print(table3,"\n")
    
    save_tables_to_file(input1, [table, table1, table2,table3],"LOTOR")
    
    return ""
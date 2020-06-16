from pandas import DataFrame

import tkinter as tk 
import statsmodels.api as sm
import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_excel('GermanCredit.xlsx',sheetname='Data')
X = df.iloc[:,1:31]
y = df.iloc[:,-1]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)



# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train,y_train)

#
#y_pred=logreg.predict(X_test)


# with sklearn
#regr = linear_model.LinearRegression()
#regr.fit(X, Y)

#print('Intercept: \n', regr.intercept_)
#print('Coefficients: \n', regr.coef_)


# with statsmodels
#X = sm.add_constant(X) # adding a constant
 
#model = sm.OLS(Y, X).fit()
#predictions = model.predict(X) 
 


# tkinter GUI
root= tk.Tk() 
 
canvas1 = tk.Canvas(root, width = 1200, height = 650)
canvas1.pack()

# with sklearn
#Intercept_result = ('Intercept: ', regr.intercept_)
#label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
#canvas1.create_window(260, 280, window=label_Intercept)

# with sklearn
#Coefficients_result  = ('Coefficients: ', regr.coef_)
#label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
#canvas1.create_window(260, 320, window=label_Coefficients)

# with statsmodels
#print_model = model.summary()
#label_model = tk.Label(root, text=print_model, justify = 'center', relief = 'solid', bg='LightSkyBlue1')
#canvas1.create_window(800, 220, window=label_model)



label1 = tk.Label(root, text=' CHK_ACCT: ')
canvas1.create_window(120, 20, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 20, window=entry1)


label2 = tk.Label(root, text=' DURATION: ')
canvas1.create_window(120, 40, window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 40, window=entry2)


label3 = tk.Label(root, text=' HISTORY: ')
canvas1.create_window(120, 60, window=label3)

entry3 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 60, window=entry3)


label4 = tk.Label(root, text=' NEW_CAR: ')
canvas1.create_window(120, 80, window=label4)

entry4 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 80, window=entry4)


label5 = tk.Label(root, text=' USED_CAR: ')
canvas1.create_window(120, 100, window=label5)

entry5 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 100, window=entry5)


label6= tk.Label(root, text=' FURNITURE: ')
canvas1.create_window(120, 120, window=label6)

entry6 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry6)


label7= tk.Label(root, text=' RADIO/TV: ')
canvas1.create_window(120, 140, window=label7)

entry7 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 140, window=entry7)

label8= tk.Label(root, text=' EDUCATION: ')
canvas1.create_window(120, 160, window=label8)

entry8 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 160, window=entry8)


label9= tk.Label(root, text=' RETRAINING: ')
canvas1.create_window(120, 180, window=label9)

entry9 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 180, window=entry9)

label10= tk.Label(root, text=' AMOUNT: ')
canvas1.create_window(120, 200, window=label10)

entry10 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 200, window=entry10)



label11= tk.Label(root, text=' SAV_ACCT: ')
canvas1.create_window(120, 220, window=label11)

entry11 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 220, window=entry11)


label12= tk.Label(root, text=' EMPLOYMENT: ')
canvas1.create_window(120, 240, window=label12)

entry12 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 240, window=entry12)



label13= tk.Label(root, text=' INSTALL_RATE: ')
canvas1.create_window(120, 260, window=label13)

entry13 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 260, window=entry13)


label14= tk.Label(root, text=' MALE_DIV: ')
canvas1.create_window(120, 280, window=label14)

entry14 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 280, window=entry14)


label15= tk.Label(root, text=' MALE_SINGLE: ')
canvas1.create_window(120, 300, window=label15)

entry15 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 300, window=entry15)

#Start Here

label16= tk.Label(root, text=' MALE_MAR_or_WID: ')
canvas1.create_window(500, 20, window=label16)

entry16 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 20, window=entry16)


label17= tk.Label(root, text=' CO-APPLICANT: ')
canvas1.create_window(500, 40, window=label17)

entry17 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 40, window=entry17)


label18= tk.Label(root, text=' GUARANTOR: ')
canvas1.create_window(500, 60, window=label18)

entry18 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 60, window=entry18)


label19= tk.Label(root, text=' PRESENT_RESIDENT: ')
canvas1.create_window(500, 80, window=label19)

entry19 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 80, window=entry19)


label20= tk.Label(root, text=' REAL_ESTATE: ')
canvas1.create_window(500, 100, window=label20)

entry20 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 100, window=entry20)


label21= tk.Label(root, text=' PROP_UNKN_NONE: ')
canvas1.create_window(500, 120, window=label21)

entry21 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 120, window=entry21)


label22= tk.Label(root, text=' AGE: ')
canvas1.create_window(500, 140, window=label22)

entry22 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 140, window=entry22)


label23= tk.Label(root, text=' OTHER_INSTALL: ')
canvas1.create_window(500, 160, window=label23)

entry23 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 160, window=entry23)


label24= tk.Label(root, text=' RENT: ')
canvas1.create_window(500, 180, window=label24)

entry24 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 180, window=entry24)


label25= tk.Label(root, text=' OWN_RES: ')
canvas1.create_window(500, 200, window=label25)

entry25 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 200, window=entry25)


label26= tk.Label(root, text=' NUM_CREDITS: ')
canvas1.create_window(500, 220, window=label26)

entry26 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 220, window=entry26)


label27= tk.Label(root, text=' JOB: ')
canvas1.create_window(500, 240, window=label27)

entry27 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 240, window=entry27)


label28= tk.Label(root, text=' NUM_DEPENDENTS: ')
canvas1.create_window(500, 260, window=label28)

entry28 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 260, window=entry28)


label29= tk.Label(root, text=' TELEPHONE: ')
canvas1.create_window(500, 280, window=label29)

entry29 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 280, window=entry29)


label30= tk.Label(root, text=' FOREIGN: ')
canvas1.create_window(500, 300, window=label30)

entry30 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(650, 300, window=entry30)


def values(): 
    global CHK_ACCT 
    CHK_ACCT = int(entry1.get()) 
    
    global DURATION 
    DURATION = int(entry2.get()) 

    global HISTORY 
    HISTORY = int(entry3.get()) 
    
    global NEW_CAR 
    NEW_CAR = int(entry4.get()) 

    global USED_CAR 
    USED_CAR = int(entry5.get()) 
    
    global FURNITURE 
    FURNITURE = int(entry6.get()) 

    global RADIO_TV 
    RADIO_TV = int(entry7.get()) 
    
    global EDUCATION 
    EDUCATION = int(entry8.get()) 

    global RETRAINING 
    RETRAINING = int(entry9.get()) 
    
    global AMOUNT 
    AMOUNT = int(entry10.get()) 

    global SAV_ACCT 
    SAV_ACCT = int(entry11.get()) 
    
    global EMPLOYMENT 
    EMPLOYMENT = int(entry12.get()) 




    global INSTALL_RATE 
    INSTALL_RATE = int(entry13.get()) 
    
    global MALE_DIV 
    MALE_DIV = int(entry14.get()) 

    global MALE_SINGLE 
    MALE_SINGLE = int(entry15.get()) 
    
    global MALE_MAR_or_WID 
    MALE_MAR_or_WID = int(entry16.get()) 

    global CO_APPLICANT 
    CO_APPLICANT = int(entry17.get()) 
    
    global GUARANTOR 
    GUARANTOR = int(entry18.get()) 

    global PRESENT_RESIDENT 
    PRESENT_RESIDENT= int(entry19.get()) 
    
    global REAL_ESTATE 
    REAL_ESTATE = int(entry20.get()) 

    global PROP_UNKN_NONE 
    PROP_UNKN_NONE = int(entry21.get()) 
    
    global AGE 
    AGE = int(entry22.get()) 

    global OTHER_INSTALL 
    OTHER_INSTALL = int(entry23.get()) 
    
    global RENT 
    RENT = int(entry24.get()) 

    global OWN_RES 
    OWN_RES = int(entry25.get()) 
    
    global NUM_CREDITS 
    NUM_CREDITS = int(entry26.get()) 

    global JOB 
    JOB = int(entry27.get()) 
    
    global NUM_DEPENDENTS 
    NUM_DEPENDENTS = int(entry28.get()) 

    global TELEPHONE 
    TELEPHONE = int(entry29.get()) 
    
    global FOREIGN
    FOREIGN = int(entry30.get()) 


    
  
 
    if logreg.predict([[CHK_ACCT, DURATION, HISTORY, NEW_CAR, USED_CAR, FURNITURE, RADIO_TV,EDUCATION, RETRAINING, AMOUNT,SAV_ACCT,EMPLOYMENT,INSTALL_RATE,MALE_DIV,MALE_SINGLE,MALE_MAR_or_WID,CO_APPLICANT,GUARANTOR,PRESENT_RESIDENT,REAL_ESTATE,PROP_UNKN_NONE,AGE,OTHER_INSTALL,RENT,OWN_RES,NUM_CREDITS,JOB,NUM_DEPENDENTS,TELEPHONE,FOREIGN]]) == 1:
      Prediction_result = ("Your loan request has approved")
    #Prediction_result  = ('Credit Approval Result: ', logreg.predict([[CHK_ACCT, DURATION, HISTORY, NEW_CAR, USED_CAR, FURNITURE, RADIO_TV,EDUCATION, RETRAINING, AMOUNT,SAV_ACCT,EMPLOYMENT,INSTALL_RATE,MALE_DIV,MALE_SINGLE,MALE_MAR_or_WID,CO_APPLICANT,GUARANTOR,PRESENT_RESIDENT,REAL_ESTATE,PROP_UNKN_NONE,AGE,OTHER_INSTALL,RENT,OWN_RES,NUM_CREDITS,JOB,NUM_DEPENDENTS,TELEPHONE,FOREIGN]]))
    else: 
      Prediction_result = ("We are unable to approve your loan request")
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(400, 380, window=label_Prediction)
    
button1 = tk.Button (root, text='Credit Approval',command=values, bg='orange') 
canvas1.create_window(400, 450, window=button1)

root.mainloop()



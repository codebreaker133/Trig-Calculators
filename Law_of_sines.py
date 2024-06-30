import math


A=float(input("what is side A (CB): "))
B=float(input("what is side B (AC): "))
C=float(input("what is side C (AB): "))
Aknown=True
Bknown=True
Cknown=True
allsidesknown=False

angleA=math.radians(float(input("what is angle A: ")))
angleB=math.radians(float(input("what is angle B: ")))
angleC=math.radians(float(input("what is angle C: ")))
angleAknown=True
angleBknown=True
angleCknown=True
allanglesknown=False
compleetTriangle=False
def check_Knowns():
    global A,B,C,angleA,angleB,angleC,Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown,allsidesknown,allanglesknown,compleetTriangle
    print("starting check of values...")
    if A==0:
        Aknown=False
        print("Akown=",Aknown)
    else:
        Aknown=True
    if B==0:
        Bknown=False
        print("Bknown=",Bknown)
    else:
        Bknown=True
    if C==0:
        Cknown=False
        print("Cknown=",Cknown)
    else:
        Cknown=True
    if angleA==0:
        angleAknown=False
        print("angleAknown=",angleAknown)
    if angleB==0:
        angleBknown=False
        print("angleBknown=",angleBknown)
    if angleC==0:
        angleCknown=False
        print("angleCknown=",angleCknown)
    if Aknown==True and Bknown==True and Cknown==True:
        allsidesknown=True
        print("all sides are solved!")
    if angleAknown==True and angleBknown==True and angleCknown==True:
        allanglesknown=True
        print("all angles are solved!")
    if allanglesknown==True and allsidesknown==True:
        compleetTriangle=True
    print('Known values checked and stored')
    return Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown,allsidesknown,allanglesknown,compleetTriangle

Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown,allsidesknown,allanglesknown,compleetTriangle=check_Knowns()
def findmissingangles():
    global angleA,angleB,angleC,angleAknown,angleBknown,angleCknown
    print("finding missing angles...")
    print("current angles:",angleA," ",angleB," ",angleC)
    calculation=False
    if angleAknown==False and angleBknown == True and angleCknown == True: #find angle a
        angleA=math.radians((180-math.degrees(angleB+angleC)))
        print(math.degrees(angleA))
        print('found angle a')
        angleAknown=True
        calculation=True
        return angleA,angleB,angleC

    if angleBknown==False and angleAknown == True and angleCknown == True: #find angle b
        angleB=math.radians((180-math.degrees(angleA+angleC)))
        print(math.degrees(angleB))
        print('found angle b')
        angleBknown=True
        calculation=True
        return angleA,angleB,angleC
    
    if angleCknown==False and angleAknown == True and angleBknown == True: #find angle c
        angleC=math.radians((180-math.degrees(angleA+angleB)))
        print(math.degrees(angleC))
        print('found angle c')
        angleCknown=True
        calculation=True
        return angleA,angleB,angleC
    
    elif calculation==False:
        angleA=angleA
        angleB=angleB
        angleC=angleC
        print("no angles found :( -----------------------------FLAG DEBUG")
        return angleA,angleB,angleC
    

angleA,angleB,angleC=findmissingangles()

def findA():
    global A,B,C,angleA,angleB,angleC,Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown

    if Bknown and angleBknown and angleAknown == True:
        A=((B*math.sin(angleA))/math.sin(angleB))
        print(A)
        return A
    if Cknown and angleCknown and angleAknown == True:
        A=((C*math.sin(angleA))/math.sin(angleC))
        print(A)
        return A
    if angleAknown==True and Bknown==True and Cknown==True:
        A=math.sqrt(((B*B)+(C*C))-(2*B*C*math.cos(angleA)))
        return A
    return A


def findB():
    global A,B,C,angleA,angleB,angleC,Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown
    if Aknown and angleAknown and angleBknown == True:
        B=((A*math.sin(angleB))/math.sin(angleA))
        print(B)
        return(B)
    if Cknown and angleCknown and angleBknown == True:
        B=((C*math.sin(angleB)/math.sin(angleC)))
        print(B)
        return(B)
    if angleBknown==True and Cknown==True and Aknown==True:
        B=math.sqrt((A*A)+(C*C)-2*A*C*math.cos(angleB))
        return(B)
    return B


def findC():
    global A,B,C,angleA,angleB,angleC,Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown
    if Aknown and angleAknown and angleCknown == True:
        C=((A*math.sin(angleC))/math.sin(angleA))
        print("C=",C)
        return(C)
    if Bknown and angleBknown and angleCknown == True:
        C=((B*math.sin(angleC))/math.sin(angleB))
        print("C=",C)
        return(C)
    if angleCknown==True and Aknown==True and Bknown==True:
        C=math.sqrt((A*A)+(B*B)-2*A*B*math.cos(angleC))
        return(C)
    return C


def findangleA():
        calculation=False
        global A,B,C,angleA,angleB,angleC,Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown
        print("finding A curent values are:","A=",A,"B=",B,"C=",C," angle A=",angleA," angle B=",angleB," angle C=",angleC)
        if angleBknown == True and Bknown == True and Aknown == True:
            angleA=(math.asin((A*math.sin(angleB))/B))
            print("angle A==",angleA)
            calculation=True
            return angleA
        
        if angleCknown == True and Cknown == True and Aknown==True:
            angleA=(math.asin((A*math.sin(angleC))/C))
            print("angle A==",angleA)
            calculation=True
            return angleA
        
        if Aknown==True and Bknown==True and Cknown==True:
            angleA=math.acos((B*B+C*C-A*A)/2*B*C)
        
        elif calculation==False:
            angleA=angleA
            return angleA


def findangleB():
        calculation=False
        global A,B,C,angleA,angleB,angleC,Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown
        print("finding B curent values are:","A=",A,"B=",B,"C=",C," angle A=",angleA," angle B=",angleB," angle C=",angleC)
        if angleCknown == True and Cknown == True and Bknown == True:
            angleB=(math.asin((B*math.sin(angleC))/C))
            print("angle B==",angleB)
            calculation=True
            return angleB

        if angleAknown == True and Aknown == True and Bknown==True:
            angleB=(math.asin((B*math.sin(angleA))/A))
            print("angle B==",angleB)
            calculation=True
            return angleB
        
        if Aknown==True and Bknown==True and Cknown==True:
            angleB=math.acos((A*A+C*C-B*B)/2*A*C)
            return angleB
        
        elif calculation==False:
            angleB=angleB
            return angleB


def findangleC():
        calculation=False
        global A,B,C,angleA,angleB,angleC,Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown
        print("finding c curent values are:","A=",A,"B=",B,"C=",C," angle A=",angleA," angle B=",angleB," angle C=",angleC)
        if angleBknown == True and Bknown == True and Cknown == True:
            angleC=(math.asin((C*math.sin(angleB))/B))
            print("angle C==",angleC)
            calculation=True
            return angleC

        if angleAknown == True and Aknown == True and Cknown==True:
            angleC=(math.asin(C*math.sin(angleA)/A))
            print("angle C==",angleC)
            calculation=True
            return angleC
        
        if Aknown==True and Bknown==True and Cknown==True:
            angleC=math.acos((A*A+B*B-C*C)/2*A*B)
            return angleC
        
        elif calculation==False:
            angleC=angleC
            return angleC

A=findA()
B=findB()
C=findC()
angleA=findangleA()
angleB=findangleB()
angleC=findangleC()

def solveloop():
    global A,B,C,angleA,angleB,angleC,Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown,allsidesknown,allanglesknown,compleetTriangle
    while compleetTriangle==False:
        A=findA()
        angleA=findangleA()
        B=findB()
        angleB=findangleB()
        C=findC()
        angleC=findangleC()
        print(A," | ",B," | ",C)
        print(angleA," | ",angleB," | ",angleC)
        angleA,angleB,angleC=findmissingangles()
        Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown,allsidesknown,allanglesknown,compleetTriangle=check_Knowns()
    return A,B,C,angleA,angleB,angleC

        

print(A,'  ',B,'  ',C,'  ',angleA,'  ',angleB,'  ',angleC,' a= ',Aknown,' b= ',Bknown,' c= ',Cknown,'  ',angleAknown,'  ',angleBknown,'  ',angleCknown)

opRun = True
while opRun == True:

    oper=input("what would you like to calculate: ")
    accepted=False

    if oper=="a":
        accepted=True
        A=findA()
        print('a=',A)
    if oper=='b':
        accepted=True
        B=findB()
        print('b=',B)
    if oper=='c':
        accepted=True
        C=findC()
        print('c=',C)
    if oper=='angle a':
        angleA=findangleA()
        accepted=True
        print('angle A=',math.degrees(angleA))
    if oper=='angle b':
        angleB=findangleB()
        accepted=True
        print('angle B=',math.degrees(angleB))
    if oper=='angle c':
        angleC=findangleC()
        accepted=True
        print('angle C=',math.degrees(angleC))
    if accepted==False:
        print('not an accepted value, Try again! \n')
    if oper=='clearvalues':
        opRun=False
    if oper=="findangles":
        angleA,angleB,angleC=findmissingangles()
    if oper=='loop':
        A,B,C,angleA,angleB,angleC=solveloop()

    angleA,angleB,angleC=findmissingangles()
    Aknown,Bknown,Cknown,angleAknown,angleBknown,angleCknown,allsidesknown,allanglesknown,compleetTriangle=check_Knowns()
    print(A,'  ',B,'  ',C,' \n angle a=',math.degrees(angleA),'  angle b=',math.degrees(angleB),'  angle c=',math.degrees(angleC),' \na= ',Aknown,' b= ',Bknown,' c= ',Cknown,' \n *Aknown=',angleAknown,'  *Bknown=',angleBknown,' *Cknown=',angleCknown," \nfinished triangle=",compleetTriangle)

'''
Created on May 15, 2018

@author: Ezhilmani Aakaash
'''
#from assign.grades import maxMarkList

import math

def calcIndFile(col,maxx):
    name=mergeFile(maxx, 50, 0)
    with open(name, 'r') as file1:
        for m in file1:
            f1=m.rstrip("\n").split("|")
            print('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[1])+", "+'{:<6}'.format(f1[2])+" "+'{:<2}'.format(f1[col]))
    file1.close()    
    
def mergeFile(maxMM,pf=50.00,i=1):
    gradeNum=0.0
    grade=''
    ff = open("consol.txt", "w")
        
    with open('class1.txt', 'r') as file1:
        for m in file1:
            f1=m.rstrip('\n').split(" ")
            a1mark=getMark(f1[0],"a11.txt")
            a2mark=getMark(f1[0],"a22.txt")
            prmark=getMark(f1[0],"proj.txt")
            t1mark=getMark(f1[0],"test11.txt")
            t2mark=getMark(f1[0],"test22.txt")
            gradeNum=gradeN(a1mark,a2mark,prmark,t1mark,t2mark,maxMM)
            grade=gradeCalc(gradeNum,pf)
            #lines = open(my_file, 'r').readlines()
            #print(f1[0]+" "+f1[1]+" "+f1[2]+" "+a1mark+" "+a2mark+" "+prmark+" "+t1mark+" "+t2mark,gradeNum,grade)
            ff.write('{:<5}'.format(f1[0])+"|"+'{:<6}'.format(f1[2])+"|"+'{:<6}'.format(f1[1])+"|"+'{:<3}'.format(a1mark)+"|"'{:<3}'.format(a2mark)+"|"+'{:<3}'.format(prmark)+"|"+'{:<3}'.format(t1mark)+"|"+'{:<3}'.format(t2mark)+"|"+'{:<6}'.format(str(gradeNum))+"|"+'{:<2}'.format(grade))
            ff.write("\n")
        
    ff.close()
    file1.close()
    if(i==1):
        print("\n")
        print('{:<5}'.format("ID")+" "+'{:<6}'.format("LN")+" "+'{:<6}'.format("FN")+" "+'{:<3}'.format("A1")+" "'{:<3}'.format("A2")+" "+'{:<3}'.format("PR")+" "+'{:<3}'.format("T1")+" "+'{:<3}'.format("T2")+" "+'{:<6}'.format("GR")+" "+'{:<2}'.format("FL"))
        print("\n")
        lines = open("consol.txt", 'r').readlines()
        for line in sorted(lines, reverse=False, key=lambda line: line.split()[0]):
            f1=line.rstrip("\n").split("|")
            print('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[1])+" "+'{:<6}'.format(f1[2])+" "+'{:<3}'.format(f1[3])+" "'{:<3}'.format(f1[4])+" "+'{:<3}'.format(f1[5])+" "+'{:<3}'.format(f1[6])+" "+'{:<3}'.format(f1[7])+" "+'{:<6}'.format(f1[8])+" "+'{:<2}'.format(f1[9]))
    else:
        return "consol.txt"
     
        
    
def gradeN(a1mark,a2mark,prmark,t1mark,t2mark,maxMM):
    if(a1mark.isdigit()==False):
        a1mark=0
    if(a2mark.isdigit()==False):
        a2mark=0
    if(prmark.isdigit()==False):
        prmark=0
    if(t1mark.isdigit()==False):
        t1mark=0
    if(t2mark.isdigit()==False):
        t2mark=0
     
    gg=0.0
    gg=(((int(a1mark)/int(maxMM[0]))*7.5)+((int(a2mark)/int(maxMM[1]))*7.5)+((int(prmark)/int(maxMM[2]))*25)+((int(t1mark)/int(maxMM[3]))*30)+((int(t2mark)/int(maxMM[4]))*30))
    return round(gg,2)

def gradeCalc(gradeNum,pf):
    temp=0.0
    x=''
    temp=((100-pf)/7)
    if gradeNum>(100-temp):
        x='A+'
    elif gradeNum>(100-(2*temp)):
        x='A'
    elif gradeNum>(100-(3*temp)):
        x='A-'
    elif gradeNum>(100-(4*temp)):
        x='B+'
    elif gradeNum>(100-(5*temp)):
        x='B'
    elif gradeNum>(100-(6*temp)):
        x='B-'
    elif gradeNum>(pf):
        x='C'
    elif gradeNum<=pf:
        x='F'
    return x

def getMark(studentId,fileName):
    mark=''
    with open(fileName, 'r') as file2:
                for n in file2:
                    f2=n.rstrip('\n').split(" ")
                    if studentId==f2[0]:
                        if(f2[1] is None):
                            mark=' '
                            continue
                        else:
                            mark=f2[1]
                return mark
    
def avg(ss,comp,maxM):
    c=0
    summ=0
    avgg=0.0
    
    count = 0
    for line in open("class1.txt"): 
        count += 1
    with open(comp, 'r') as file1:
        for m in file1:
            f1=m.split(" ")
            #print(f1[1])
            #if (f1[1]!="\n"):
            c=c+1
            if(f1[1]=="\n"):
                summ=summ+0
            else:
                summ=summ+int(f1[1])              
    file1.close()
    #print(summ)
    #print(c)
    if ss=='a1':
        avgg=summ/count
        #print(avgg)
        print(ss.upper(),'average:',avgg,'/',maxM[0])
    elif ss=='a2':
        avgg=summ/count
        #print(avgg)
        print(ss.upper(),'average:',avgg,'/',maxM[1])
    elif ss=='pr':
        avgg=summ/count
        #print(avgg)
        print(ss.upper(),'average:',avgg,'/',maxM[2])
    elif ss=='test1':
        avgg=summ/count
        #print(avgg)
        print(ss.upper(),'average:',avgg,'/',maxM[3])
    elif ss=='test2':
        avgg=summ/count
        #print(avgg)
        print(ss.upper(),'average:',avgg,'/',maxM[4])

def indComponent(maxMark):
    cond=True
    while(cond):
        
        comp = input('Enter the component needed (A1, A2, PR, T1, or T2) :')
        print("\n")
        if comp.lower()=='a1':
            print(comp.upper()+" Grades ("+maxMark[0]+")")
            print("\n")
            calcIndFile(3,maxMark)
            cond=False
        elif comp.lower()=='a2':
            print(comp.upper()+" Grades ("+maxMark[1]+")")
            print("\n")
            calcIndFile(4,maxMark)
            cond=False
        elif comp.lower()=='pr':
            print(comp.upper()+" Grades ("+maxMark[2]+")")
            print("\n")
            calcIndFile(5,maxMark)
            cond=False
        elif comp.lower()=='t1':
            print(comp.upper()+" Grades ("+maxMark[3]+")")
            print("\n")
            calcIndFile(6,maxMark)
            cond=False
        elif comp.lower()=='t2':
            print(comp.upper()+" Grades ("+maxMark[4]+")")
            print("\n")
            calcIndFile(7,maxMark)
            cond=False
        else:
            print("Not a valid option. ")
            print("Please enter again")
            cond=True    
        
def compAvg(maxMark):
    cond=True
    while(cond):
        comp = input('Enter the component needed (A1, A2, PR, T1, or T2) :')
        print("\n")
        if comp.lower()=='a1':
            avg("a1","a11.txt",maxMark)
            cond=False
        elif comp.lower()=='a2':
            avg("a2","a22.txt",maxMark)
            cond=False
        elif comp.lower()=='pr':
            avg("pr","proj.txt",maxMark)
            cond=False
        elif comp.lower()=='t1':
            avg("test1","test11.txt",maxMark)
            cond=False
        elif comp.lower()=='t2':
            avg("test2","test22.txt",maxMark)
            cond=False
        else:
            print("Not a valid option")
            print("Please enter again: ")
            
def twoSort(maxMark):
    cond=True
    while(cond):
        srt=input("Do you want the output sorted based on Last Name(LN) or Numeric Grade(GR)? ")
        if srt.lower()=='ln' or srt.lower()=='gr':
            break
        else:
            print("Wrong Input, Enter Again")
            
        
    pf=50
    gradeNum=0.0
    grade=''
    ff = open("consol.txt", "w")
        
    with open('class1.txt', 'r') as file1:
        for m in file1:
            f1=m.rstrip('\n').split(" ")
            a1mark=getMark(f1[0],"a11.txt")
            a2mark=getMark(f1[0],"a22.txt")
            prmark=getMark(f1[0],"proj.txt")
            t1mark=getMark(f1[0],"test11.txt")
            t2mark=getMark(f1[0],"test22.txt")
            gradeNum=gradeN(a1mark,a2mark,prmark,t1mark,t2mark,maxMark)
            grade=gradeCalc(gradeNum,pf)
            ff.write('{:<5}'.format(f1[0])+"|"+'{:<6}'.format(f1[2])+"|"+'{:<6}'.format(f1[1])+"|"+'{:<3}'.format(a1mark)+"|"'{:<3}'.format(a2mark)+"|"+'{:<3}'.format(prmark)+"|"+'{:<3}'.format(t1mark)+"|"+'{:<3}'.format(t2mark)+"|"+'{:<6}'.format(str(gradeNum))+"|"+'{:<2}'.format(grade))
            ff.write("\n")
        
    ff.close()
    file1.close()
    ff = open("sort.txt", "w")
    print("\n")
    print('{:<5}'.format("ID")+" "+'{:<6}'.format("LN")+" "+'{:<6}'.format("FN")+" "+'{:<3}'.format("A1")+" "'{:<3}'.format("A2")+" "+'{:<3}'.format("PR")+" "+'{:<3}'.format("T1")+" "+'{:<3}'.format("T2")+" "+'{:<6}'.format("GR")+" "+'{:<2}'.format("FL"))
    print("\n")
    if (srt.lower()=='ln'):
        lines = open("consol.txt", 'r').readlines()
        for line in sorted(lines, reverse=False, key=lambda line: line.split("|")[1]):
            f1=line.rstrip('\n').split("|")
            ff.write('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[1])+" "+'{:<6}'.format(f1[2])+" "+'{:<3}'.format(f1[3])+" "'{:<3}'.format(f1[4])+" "+'{:<3}'.format(f1[5])+" "+'{:<3}'.format(f1[6])+" "+'{:<3}'.format(f1[7])+" "+'{:<6}'.format(f1[8])+" "+'{:<2}'.format(f1[9]))
            print('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[1])+" "+'{:<6}'.format(f1[2])+" "+'{:<3}'.format(f1[3])+" "'{:<3}'.format(f1[4])+" "+'{:<3}'.format(f1[5])+" "+'{:<3}'.format(f1[6])+" "+'{:<3}'.format(f1[7])+" "+'{:<6}'.format(f1[8])+" "+'{:<2}'.format(f1[9]))         
            
            #ff.write(line)
            #f1=line.rstrip("\n").split(" ")
            #ff.write('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[2])+" "+'{:<6}'.format(f1[1])+" "+'{:<3}'.format(a1mark)+" "'{:<3}'.format(a2mark)+" "+'{:<3}'.format(prmark)+" "+'{:<3}'.format(t1mark)+" "+'{:<3}'.format(t2mark)+" "+'{:<6}'.format(str(gradeNum))+" "+'{:<2}'.format(grade))
            #print("\n")
            #print('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[1])+" "+'{:<6}'.format(f1[2])+" "+'{:<3}'.format(f1[3])+" "'{:<3}'.format(f1[4])+" "+'{:<3}'.format(f1[5])+" "+'{:<3}'.format(f1[6])+" "+'{:<3}'.format(f1[7])+" "+'{:<6}'.format(str(f1[8]))+" "+'{:<2}'.format(f1[9]))
            #print(line)
    if(srt.lower()=='gr'):
        lines = open("consol.txt", 'r').readlines()
        for line in sorted(lines, reverse=True, key=lambda line: line.split("|")[8]):
            f1=line.rstrip('\n').split("|")
            ff.write('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[1])+" "+'{:<6}'.format(f1[2])+" "+'{:<3}'.format(f1[3])+" "'{:<3}'.format(f1[4])+" "+'{:<3}'.format(f1[5])+" "+'{:<3}'.format(f1[6])+" "+'{:<3}'.format(f1[7])+" "+'{:<6}'.format(f1[8])+" "+'{:<2}'.format(f1[9]))
            print('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[1])+" "+'{:<6}'.format(f1[2])+" "+'{:<3}'.format(f1[3])+" "'{:<3}'.format(f1[4])+" "+'{:<3}'.format(f1[5])+" "+'{:<3}'.format(f1[6])+" "+'{:<3}'.format(f1[7])+" "+'{:<6}'.format(f1[8])+" "+'{:<2}'.format(f1[9]))         
            
            #ff.write('{:<5}'.format(f1[0])+" "+'{:<6}'.format(f1[2])+" "+'{:<6}'.format(f1[1])+" "+'{:<3}'.format(a1mark)+" "'{:<3}'.format(a2mark)+" "+'{:<3}'.format(prmark)+" "+'{:<3}'.format(t1mark)+" "+'{:<3}'.format(t2mark)+" "+'{:<6}'.format(str(gradeNum))+" "+'{:<2}'.format(grade))
            #print("\n")
    ff.close()
    
        



        
        
    
    
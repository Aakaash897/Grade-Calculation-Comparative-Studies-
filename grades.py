'''
Created on May 15, 2018

@author: Ezhilmani Aakaash
'''

from assign.compute import indComponent,compAvg, mergeFile, twoSort

maxMarkList=[]

with open("a1.txt") as f:
    maxMarkList.append((f.readline()).rstrip('\n'))
    ff = open("a11.txt", "w")
    for m in f:
        #print(m)
        if (m[1]=="\n"):
            ff.write(" ")
            ff.write("\n")
        else:                        
            ff.write(" ".join(m.rstrip('\n').split('|')))
            ff.write("\n")
    ff.close()
    f.close()
    
with open("a2.txt") as f:
    maxMarkList.append((f.readline()).rstrip('\n'))
    ff = open("a22.txt", "w")
    for m in f:
        if (m[1]=="\n"):
            ff.write(" ")
            ff.write("\n")
        else:                        
            ff.write(" ".join(m.rstrip('\n').split('|')))
            ff.write("\n")
    ff.close()
    f.close()
    
with open("project.txt") as f:
    maxMarkList.append((f.readline()).rstrip('\n'))
    ff = open("proj.txt", "w")
    for m in f:
        if (m[1]=="\n"):
            ff.write(" ")
            ff.write("\n")
        else:                        
            ff.write(" ".join(m.rstrip('\n').split('|')))
            ff.write("\n")
    ff.close()
    f.close()
    
with open("test1.txt") as f:
    maxMarkList.append((f.readline()).rstrip('\n'))
    ff = open("test11.txt", "w")
    for m in f:
        if (m[1]=="\n"):
            ff.write(" ")
            ff.write("\n")
        else:                        
            ff.write(" ".join(m.rstrip('\n').split('|')))
            ff.write("\n")
    ff.close()
    f.close()
    
with open("test2.txt") as f:
    maxMarkList.append((f.readline()).rstrip('\n'))
    ff = open("test22.txt", "w")
    for m in f:
        if (m[1]=="\n"):
            ff.write(" ")
            ff.write("\n")
        else:                        
            ff.write(" ".join(m.rstrip('\n').split('|')))
            ff.write("\n")
    ff.close()
    f.close()
    
with open("class.txt") as f:
    ff = open("class1.txt", "w")
    for m in f:
        ff.write(" ".join(m.rstrip('\n').split('|')))
        ff.write("\n")
    ff.close()
    f.close()



def options():
    get=""
    condd=True
    while(condd):
        print("\n")
        print('1. Display individual component')
        print('2. Display component average')
        print('3. Display Standard Report')
        print('4. Sort by alternate column')
        print('5. Change Pass/Fail point')
        print('6. Exit')
        return  input("Select option between 1- 6:")

   
cond=True

while (cond):
    caseval=options()
    if(caseval.isnumeric()):
        case=int(caseval)
        if (case == 1) :
            print("\n")
            print ("Display individual component")
            indComponent(maxMarkList)
        elif (case == 2) :
            print("\n")
            print ("Display component average")
            compAvg(maxMarkList)
        elif (case == 3) :
            print("\n")
            print ("Display Standard Report")
            mergeFile(maxMarkList,50,1)
            
        elif (case == 4) :
            print("\n")
            print ("Sort by alternate column")
            print("\n")
            #srt=input("Do you want the output sorted based on Last Name(LN) or Numeric Grade(GR)? ")
            twoSort(maxMarkList)
            
        elif (case == 5) :
            print("\n")
            print ("Change Pass/Fail point")
            print("\n")
            cond1=True
            while(cond1):
                try:
                    pf=float(input("Enter the new Pass/Fail value: "))
                    break
                except ValueError:
                    print("Invalid Input, Enter a valid number")
            mergeFile(maxMarkList, abs(pf),1)
          
        elif (case == 6) :
            print("\n")
            print ("Good bye")
            exit(0)
            
            cond=False
        else:
            print("Not a valid option")
            print("\n")
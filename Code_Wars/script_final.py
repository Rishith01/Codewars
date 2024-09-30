import random
import math

name = "scriptblue"

def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    
def checkFight(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    right = pirate.investigate_right()
    left = pirate.investigate_left()
    sw = pirate.investigate_sw()
    se = pirate.investigate_se()
    nw = pirate.investigate_nw()
    ne = pirate.investigate_ne()
    list=[up,down,left,right,sw,se,nw,ne]
    result=(False,0)
    for i in list:
        if i[1] in ["both","enemy"] and i[0]=="island1":
            result=[True,1]
            break
        elif i[1] in ["both","enemy"] and i[0]=="island2":
            result=[True,2]
            break
        elif i[1] in ["both","enemy"] and i[0]=="island3":
            result=[True,3]
            break
    return result

def SignalToStr(signal):
    islandSignal1=[]
    for i in signal:
        islandSignal1.append(":".join(i))
    islandSignal2= ";".join(islandSignal1)
    return islandSignal2
    
def findIndex(str,list):
    for i in list:    
        if str in i:
            return list.index(i)
    return False
    
def removeSig(team,str):
    sig=team.getTeamSignal()
    sigList=sig.split(";")
    while True:
        index=findIndex(str,sigList)
        if index==False:
            break
        sigList.pop(index)
    team.setTeamSignal(";".join(sigList))

def removeSigSelf(pirate,str):
    sig=pirate.getSignal()
    sigList=sig.split(";")
    while True:
        index=findIndex(str,sigList)
        if isinstance(index,bool) and index==False:
            break
        sigList.pop(index)
    pirate.setSignal(";".join(sigList))
    
def start(pirate):
    dimX = pirate.getDimensionX()
    dimY = pirate.getDimensionY()
    (x_i,y_i) = pirate.getDeployPoint()
    (x_curr,y_curr) = pirate.getPosition()
    if (pirate.getSignal() == ""):
        pirate.setSignal("000;")  
    x=0
    y=0
    if (x_i==0):
        x=1
    else:
        x=-1
    if y_i==0:
        y=1
    else:
        y=-1
    result=0
    for i in range(1,5):
        if int(pirate.getID())%8==i:
            if (pirate.getPosition()==(dimX/2+x,dimY/2-y*(7-(i-1)*2))):
                pirate.setSignal("end")
            if (moveTo(x_i+x*(7-(i-1)*2),y_i,pirate)!=0 and pirate.getSignal() == "000;"):
                result= moveTo(x_i+x*(7-(i-1)*2),y_i,pirate)
            if (moveTo(x_i+x*(7-(i-1)*2),y_i,pirate)==0 and pirate.getSignal() == "000;"):
                pirate.setSignal("100;")
            if (pirate.getSignal() == "100;" or pirate.getSignal() == "101;"):
                if(pirate.getSignal() == "100;"):
                    pirate.setSignal("101;")
                    result= moveTo(x_curr+x,y_curr,pirate)
                elif (pirate.getSignal() == "101;"):
                    pirate.setSignal("100;")
                    result= moveTo(x_curr,y_curr+y,pirate)
            break
    for i in range(5,9):
        if int(pirate.getID())%8==i:
            j=i-4
            if (pirate.getPosition()==(dimX/2-x*(2*j-1),dimY/2+y)):
                pirate.setSignal("end")
            if (moveTo(x_i,y_i+y*(7-(j-1)*2),pirate)!=0 and pirate.getSignal() == "000;"):
                result= moveTo(x_i,y_i+y*(7-(j-1)*2),pirate)
            if (moveTo(x_i,y_i+y*(7-(j-1)*2),pirate)==0 and pirate.getSignal() == "000;"):
                pirate.setSignal("100;")
            if (pirate.getSignal() == "100;" or pirate.getSignal() == "101;"):
                if(pirate.getSignal() == "100;"):
                    pirate.setSignal("101;")
                    result= moveTo(x_curr+x,y_curr,pirate)
                elif (pirate.getSignal() == "101;"):
                    pirate.setSignal("100;")
                    result= moveTo(x_curr,y_curr+y,pirate)
            break
    return result


def cleanIsland(pirate):
    sig=pirate.getTeamSignal()
    frame=pirate.getCurrentFrame()
    id=int(pirate.getID())
    x=sig.split(";")
    y=pirate.getSignal().split(";")
    index=findIndex("clr",x)
    frame0=int(x[index].split(":")[1])
    move=[1,2,3,4,1,2,3,4]
    result=None
    if "island" not in pirate.investigate_current()[0]:
        removeSigSelf(pirate,"#")
    elif(frame-frame0 <= 20 and "#" in y):
        if(id%4==0):
            result= move[(frame-frame0)%4]
        elif(id%4==1):
            result= move[(frame-frame0)%4+1]
        elif(id%4==2):
            result= move[(frame-frame0)%4+2]
        else:
            result= move[(frame-frame0)%4+3]
    elif(frame-frame0>20 or "att" not in sig):
        removeSig(pirate,"clr")
        removeSigSelf(pirate,"#")
        pirate.setSignal(";".join(y))
    return result

def centerIsland(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    right = pirate.investigate_right()
    left = pirate.investigate_left()
    x, y = pirate.getPosition()
    if up[0][0:-1] == "island" and down[0][0:-1] == "island" and right[0][0:-1] == "island" and left[0][0:-1] == "island":
        return (x,y)    
    if up[0][0:-1] != "island" and right[0][0:-1] == "island" and left[0][0:-1] != "island" and down[0][0:-1] == "island":
        return (x+1,y+1)
    if up[0][0:-1] != "island" and right[0][0:-1] != "island" and left[0][0:-1] == "island" and down[0][0:-1] == "island":
        return (x-1,y+1)
    if up[0][0:-1] == "island" and right[0][0:-1] != "island" and left[0][0:-1] == "island" and down[0][0:-1] != "island":
        return (x-1,y-1)
    if up[0][0:-1] == "island" and right[0][0:-1] == "island" and left[0][0:-1] != "island" and down[0][0:-1] != "island":
        return (x+1,y-1)
    if up[0][0:-1] == "island" and down[0][0:-1] == "island" and left[0][0:-1] == "island" and right[0][0:-1] != "island":
        return (x-1,y)
    if up[0][0:-1] == "island" and down[0][0:-1] == "island" and left[0][0:-1] != "island" and right[0][0:-1] == "island":
        return (x+1,y)
    if up[0][0:-1] != "island" and down[0][0:-1] == "island" and left[0][0:-1] == "island" and right[0][0:-1] == "island":
        return (x,y+1)
    if up[0][0:-1] == "island" and down[0][0:-1] != "island" and left[0][0:-1] == "island" and right[0][0:-1] == "island":
        return (x,y-1)
        

def checkClash(pirate):
    sig=pirate.getTeamSignal()
    cur=pirate.investigate_current()
    s=pirate.trackPlayers()
    fight=checkFight(pirate)
    result=False
    if fight[0]:
        if ("isl1;" not in sig and fight[1]==1) or (cur[0]=="island1" and s[0]==""):
            result= True
        
        elif ("isl2;" not in sig and fight[1]==2) or (cur[0]=="island2" and s[1]==""):
            result= True
            
        elif ("isl3;" not in sig and fight[1]==3) or (cur[0]=="island3" and s[2]==""):
            result= True
    return result

def General_motion_p1(pirate):#to set them to move tot the starting point
    sig=pirate.getSignal()
    sigTeam=pirate.getTeamSignal()
    p = sigTeam.split(";")
    total=int(p[0])
    X = pirate.getDimensionX()
    Y = pirate.getDimensionY()
    n = int(pirate.getID())
    x, y = pirate.getPosition() 
    
    n =(n)//1 % (X // 2)
    res=-1
    if x >= 0 and x < X / 2 and y >= 0 and y < Y / 2:
        res=moveTo(n, n, pirate)
    elif x >= 0 and x < X / 2 and y >= Y / 2 and y <= Y:
        res=moveTo(n, Y - n, pirate)
    elif x >= X / 2 and x <= X  and y >= 0 and y < Y / 2:
        res=moveTo(X - n, n, pirate)
    elif x >= X / 2 and x <= X  and y >= Y / 2 and y <= Y:
        res=moveTo(X - n, Y - n, pirate)
    if res==0:
        pirate.setSignal(sig+"str;")
    return res
    
            
def General_motion_p2(pirate):#to move them in a spiral square pattern
    n = int(pirate.getID())
    X = pirate.getDimensionX()
    Y = pirate.getDimensionY()
    
    n =(n)//1 % (X // 2)
    x , y = pirate.getPosition()
    res=-1
    if x > 0 and x <= X / 2 and y > 0 and y <= Y / 2:
        res= moveTo(X - n , n, pirate)
    elif x > 0 and x <= X / 2 and y > Y / 2 and y <= Y:
        res= moveTo(n , n, pirate)
    elif x > X / 2 and x <= X and y > 0 and y <= Y / 2:
        res= moveTo(X - n , Y - n, pirate)
    elif x > X / 2 and x <= X and y > Y / 2 and y <= Y:
        res= moveTo(n , Y - n, pirate)
    if x == X/2 or y==Y/2:
        removeSigSelf(pirate,"str")
    return res

def General_motion_p3(pirate):#to move them in a spiral square pattern
    n = int(pirate.getID())
    X = pirate.getDimensionX()
    Y = pirate.getDimensionY()
    
    n =(n)//1 % (X // 2)
    x , y = pirate.getPosition()
    res=-1
    if x > 0 and x <= X / 2 and y > 0 and y <= Y / 2:
        res= moveTo(n ,Y- n, pirate)
    elif x > 0 and x <= X / 2 and y > Y / 2 and y <= Y:
        res= moveTo(X- n ,Y- n, pirate)
    elif x > X / 2 and x <= X and y > 0 and y <= Y / 2:
        res= moveTo(n , n, pirate)
    elif x > X / 2 and x <= X and y > Y / 2 and y <= Y:
        res= moveTo(X- n ,  n, pirate)
    if x == X/2 or y==Y/2:
        removeSigSelf(pirate,"str")
    return res

def movingAlongAxes(pirate):
    dimX = pirate.getDimensionX()    #Gets length of map
    dimY = pirate.getDimensionY()    #Gets width of map

    spawn = list(pirate.getDeployPoint())    #Figures out the spawn point
    if spawn[0] > 0 and spawn[1] > 0:
        spawn = [dimX - 1,dimY - 1]
    elif spawn[0] > 0 and spawn[1] == 0:
        spawn = [dimX - 1,0]
    elif spawn[0] == 0 and spawn[1] > 0:
        spawn = [0,dimY - 1]
    else:
        spawn = [0,0]
    
    x = pirate.getPosition()[0]         # x-coordinate of pirate
    y = pirate.getPosition()[1]         # y-coordinate of pirate
    
    for i in range(dimX//2-1):
        if(y ==dimY/2+i and (spawn == [0,0] or spawn == [dimX - 1,0])): 
            pirate.setSignal('z1')       
            return moveTo(x, dimY - 1, pirate)
        if(y ==dimY/2+i and (spawn == [0,dimY - 1] or spawn == [dimX - 1 - 1,dimY])):
            pirate.setSignal('z2')
            return moveTo(x, 0, pirate)
        if(x ==dimX/2+i and (spawn == [0,0] or spawn == [0,dimY - 1])):
            pirate.setSignal('z3')      
            return moveTo(dimX - 1 , y, pirate)
        if(x ==dimX/2+i and (spawn ==[dimX - 1,0] or spawn == [dimX - 1,dimY - 1])):
            pirate.setSignal('z4')
            return moveTo(0, y ,pirate)
    
    if(y ==dimY-2 and 'z1' in pirate.getSignal() and spawn == [0,0]):   
        pirate.setSignal('z5')     
        return moveTo(x+1, dimY - 2, pirate)
    if(y ==0 and 'z2' in pirate.getSignal() and spawn == [dimX - 1,dimY - 1]):
        pirate.setSignal('z6')
        return moveTo(x-1, 0, pirate)
    if(x ==dimX-2 and 'z3' in pirate.getSignal() and spawn == [0,dimY - 1]): 
        pirate.setSignal('z7')     
        return moveTo(dimX - 2 , y-1, pirate)
    if(x ==0 and 'z4' in pirate.getSignal() and spawn == [dimX - 1,dimY - 1]):
        pirate.setSignal('z8')
        return moveTo(0, y-1 ,pirate) 
    if(y ==dimY-2 and 'z1' in pirate.getSignal() and spawn == [dimX - 1,0]):
        pirate.setSignal('z5')       
        return moveTo(x-1, dimY - 2, pirate)
    if(y ==0 and 'z2' in pirate.getSignal() and spawn == [0,dimY - 1]):
        pirate.setSignal('z6')
        return moveTo(x+1, 0, pirate)
    if(x ==dimX-2 and 'z3' in pirate.getSignal() and spawn == [0,0]): 
        pirate.setSignal('z7')     
        return moveTo(dimX - 2 , y+1, pirate)
    if(x ==0 and 'z4' in pirate.getSignal() and spawn ==[dimX - 1,0]):
        pirate.setSignal('z8')
        return moveTo(0, y+1 ,pirate)
    
    for j in range(0,dimX//2,-1):
        if('z5' in pirate.getSignal() and (spawn == [0,0] or spawn == [dimX - 1,0])):       
            return moveTo(x, dimY//2+j, pirate)
        if('z6' in pirate.getSignal() and (spawn == [0,dimY - 1] or spawn == [dimX - 1,dimY - 1])):
            return moveTo(x, dimY//2+j, pirate)
        if('z7' in pirate.getSignal() and (spawn == [0,0] or spawn == [0,dimY - 1])):      
            return moveTo(dimX//2+j , y, pirate)
        if('z8' in pirate.getSignal() and (spawn ==[dimX - 1,0] or spawn == [dimX - 1,dimY - 1])):
            return moveTo(dimX//2+j, y ,pirate)

def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()[1]
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum
    
def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )

    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 , y == 0):
        return random.randint(1,4)
    
    if(sorted_dict[list(sorted_dict())[3]] == 0 ):
        return random.randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)
    
def newGuy(pirate):
    dimX = pirate.getDimensionX()
    dimY = pirate.getDimensionY()
    (x_i,y_i) = pirate.getDeployPoint()

    if (x_i==0 and y_i==0):
        if (int(pirate.getID())>8 and int(pirate.getID())%2==0 and int(pirate.getID())<(dimX+8)):
            i=int(pirate.getID())-8
            if (pirate.getSignal() == ""):
                pirate.setSignal("000")
            if (moveTo(x_i+i,y_i,pirate)!= 0 and pirate.getSignal() == "000"):
                return moveTo(x_i+i,y_i,pirate)
            if (pirate.getPosition() == (x_i+i,y_i)):
                pirate.setSignal("100")
            if (pirate.getPosition()[0]!=(dimX-1)):
                if (pirate.getSignal() == "100"):
                    pirate.setSignal("101")
                    return 3
                elif (pirate.getSignal() == "101"):
                    pirate.setSignal("100")
                    return 2
            if (pirate.getPosition()[0]==(dimX-1)):
                pirate.setSignal("end")
        elif (int(pirate.getID())>8 and int(pirate.getID())%2!=0 and int(pirate.getID())<(dimX+8)):
            i=int(pirate.getID())-8
            if (pirate.getSignal() == ""):
                pirate.setSignal("000")
            if (moveTo(x_i,y_i+1,pirate)!= 0 and pirate.getSignal() == "000"):
                return moveTo(x_i,y_i+i,pirate)
            if (pirate.getPosition() == (x_i,y_i+i)):
                pirate.setSignal("100")
            if (pirate.getPosition()[1]!=(dimY-1)):
                if (pirate.getSignal() == "100"):
                    pirate.setSignal("101")
                    return 2
                elif (pirate.getSignal() == "101"):
                    pirate.setSignal("100")
                    return 3
            if (pirate.getPosition()[0]==(dimY-1)):
                pirate.setSignal("end")    
    if (x_i==(dimX-1) and y_i==0):
        if (int(pirate.getID())>8 and int(pirate.getID())%2==0 and int(pirate.getID())<(dimX+8)):
            i=int(pirate.getID())-8
            if (pirate.getSignal() == ""):
                pirate.setSignal("000")
            if (moveTo(x_i,y_i+1,pirate)!= 0 and pirate.getSignal() == "000"):
                return moveTo(x_i,y_i+i,pirate)
            if (pirate.getPosition() == (x_i,y_i+i)):
                pirate.setSignal("100")
            if (pirate.getPosition()[1]!=(dimY-1)):
                if (pirate.getSignal() == "100"):
                    pirate.setSignal("101")
                    return 4
                elif (pirate.getSignal() == "101"):
                    pirate.setSignal("100")
                    return 3
            if (pirate.getPosition()[1]==(dimY-1)):
                pirate.setSignal("end")
        elif (int(pirate.getID())>8 and int(pirate.getID())%2!=0 and int(pirate.getID())<(dimX+8)):
            i=int(pirate.getID())-8
            if (pirate.getSignal() == ""):
                pirate.setSignal("000")
            if (moveTo(x_i-1,y_i,pirate)!= 0 and pirate.getSignal() == "000"):
                return moveTo(x_i-i,y_i,pirate)
            if (pirate.getPosition() == (x_i-i,y_i)):
                pirate.setSignal("100")
            if (pirate.getPosition()[0]!=(0)):
                if (pirate.getSignal() == "100"):
                    pirate.setSignal("101")
                    return 3
                elif (pirate.getSignal() == "101"):
                    pirate.setSignal("100")
                    return 4
            if (pirate.getPosition()[0]==(0)):
                pirate.setSignal("end")
    if (x_i==0 and y_i==(dimY-1)):
        if (int(pirate.getID())>8 and int(pirate.getID())%2==0 and int(pirate.getID())<(dimX+8)):
            i=int(pirate.getID())-8
            if (pirate.getSignal() == ""):
                pirate.setSignal("000")
            if (moveTo(x_i,y_i-1,pirate)!= 0 and pirate.getSignal() == "000"):
                return moveTo(x_i,y_i-i,pirate)
            if (pirate.getPosition() == x_i,y_i-i):
                pirate.setSignal("100")
            if (pirate.getPosition()[1]!=(0)):
                if (pirate.getSignal() == "100"):
                    pirate.setSignal("101")
                    return 2
                elif (pirate.getSignal() == "101"):
                    pirate.setSignal("100")
                    return 1
            if (pirate.getPosition()[1]==(0)):
                pirate.setSignal("end")
        elif (int(pirate.getID())>8 and int(pirate.getID())%2!=0 and int(pirate.getID())<(dimX+8)):
            i=int(pirate.getID())-8
            if (pirate.getSignal() == ""):
                pirate.setSignal("000")
            if (moveTo(x_i+1,y_i,pirate)!= 0 and pirate.getSignal() == "000"):
                return moveTo(x_i+i,y_i,pirate)
            if (pirate.getPosition() == (x_i+i,y_i)):
                pirate.setSignal("100")
            if (pirate.getPosition()[0]!=(dimX-1)):
                if (pirate.getSignal() == "100"):
                    pirate.setSignal("101")
                    return 1
                elif (pirate.getSignal() == "101"):
                    pirate.setSignal("100")
                    return 2
            if (pirate.getPosition()[0]==(dimX-1)):
                pirate.setSignal("end")
    if (x_i==(dimX-1) and y_i==(dimY-1)):
        if (int(pirate.getID())>8 and int(pirate.getID())%2==0 and int(pirate.getID())<(dimX+8)):
            i=int(pirate.getID())-8
            if (pirate.getSignal() == ""):
                pirate.setSignal("000")
            if (moveTo(x_i-1,y_i,pirate)!= 0 and pirate.getSignal() == "000"):
                return moveTo(x_i-i,y_i,pirate)
            if (pirate.getPosition() == (x_i-i,y_i)):
                pirate.setSignal("100")
            if (pirate.getPosition()[0]!=(0)):
                if (pirate.getSignal() == "100"):
                    pirate.setSignal("101")
                    return 1
                elif (pirate.getSignal() == "101"):
                    pirate.setSignal("100")
                    return 4
            if (pirate.getPosition()[0]==(0)):
                pirate.setSignal("end")
        elif (int(pirate.getID())>8 and int(pirate.getID())%2!=0 and int(pirate.getID())<(dimX+8)):
            i=int(pirate.getID())-8
            if (pirate.getSignal() == ""):
                pirate.setSignal("000")
            if (moveTo(x_i,y_i-1,pirate)!= 0 and pirate.getSignal() == "000"):
                return moveTo(x_i,y_i-i,pirate)
            if (pirate.getPosition() == (x_i,y_i-i)):
                pirate.setSignal("100")
            if (pirate.getPosition()[1]!=(0)):
                if (pirate.getSignal() == "100"):
                    pirate.setSignal("101")
                    return 4
                elif (pirate.getSignal() == "101"):
                    pirate.setSignal("100")
                    return 1
            if (pirate.getPosition()[0]==(0)):
                pirate.setSignal("end")
                

def ActPirate(pirate):
    islandSignal=[["8"],["isl1"],["isl2"],["isl3"],""]
    if(pirate.getCurrentFrame()==1):
        islandSignalStr=SignalToStr(islandSignal)
        pirate.setTeamSignal(islandSignalStr)
        

    sig=pirate.getTeamSignal()
    sigSelf=pirate.getSignal()
    dimX = pirate.getDimensionX()
    pos=pirate.getPosition()
    
    
    
    if pirate.getCurrentFrame()<2*(dimX/2 - 1) and int(pirate.getID())<=15 and "end" not in sigSelf:
        return start(pirate)
    if (int(pirate.getID())>15 and pirate.getCurrentFrame() < 20*dimX - 1) or(pirate.getCurrentFrame()<15*dimX):
        if "str;" in sigSelf:
            if int(pirate.getID())%2==1:
                return General_motion_p2(pirate)
            else:
                return General_motion_p3(pirate)
        return General_motion_p1(pirate)
    
    
    if pirate.getTotalGunpowder()<=100:
        return spread(pirate)
    
    if "clr" in sig:
        e=cleanIsland(pirate)
        if isinstance(e,int):
            return e
        
    clash=checkClash(pirate)
    
    current= pirate.investigate_current()
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    sw = pirate.investigate_sw()
    se = pirate.investigate_se()
    nw = pirate.investigate_nw()
    ne = pirate.investigate_ne()
    x, y = pirate.getPosition()
    s = pirate.trackPlayers()
    
    if(current[0] != "island1" and current[0] != "island2" and current[0] != "island3" and not clash):
        if (
            (up[0] == "island1" and s[0] != "myCaptured")
            or (up[0] == "island2" and s[1] != "myCaptured")
            or (up[0] == "island3" and s[2] != "myCaptured")
        ):
            if(s[int(up[0][-1])-1]!="myCapturing"):
                pirate.setSignal("att:" + up[0][-1]+ ":" + str(x) + ":" + str(y - 1) + ";")

        if (
            (down[0] == "island1" and s[0] != "myCaptured")
            or (down[0] == "island2" and s[1] != "myCaptured")
            or (down[0] == "island3" and s[2] != "myCaptured")
        ):
            if(s[int(down[0][-1])-1]!="myCapturing"):
                pirate.setSignal("att:" + down[0][-1]+ ":" + str(x) + ":" + str(y + 1) + ";")

        if (
            (left[0] == "island1" and s[0] != "myCaptured")
            or (left[0] == "island2" and s[1] != "myCaptured")
            or (left[0] == "island3" and s[2] != "myCaptured")
        ):
            if(s[int(left[0][-1])-1]!="myCapturing"):
                pirate.setSignal("att:" + left[0][-1]+ ":" + str(x - 1) + ":" + str(y) + ";")

        if (
            (right[0] == "island1" and s[0] != "myCaptured")
            or (right[0] == "island2" and s[1] != "myCaptured")
            or (right[0] == "island3" and s[2] != "myCaptured")
        ):
            if(s[int(right[0][-1])-1]!="myCapturing"):
                pirate.setSignal("att:" + right[0][-1]+ ":" + str(x + 1) + ":" + str(y) + ";")
    
    
    elif(current[0] == "island1" or current[0] == "island2" or current[0]=="island3"):
        teamSignal= pirate.getTeamSignal()
        num=current[0][-1]
        (x0,y0)=centerIsland(pirate)
        islandSignal[int(num)].append(str(x0))
        islandSignal[int(num)].append(str(y0))
        newSig=":".join(islandSignal[int(num)])
        sigList=teamSignal.split(";")
        sigList[int(num)]=newSig
        pirate.setTeamSignal(";".join(sigList))

        if(clash):
            teamSignal= pirate.getTeamSignal()
            s = "att:" + num + ":" + str(x0) +":" + str(y0) + ";"
            if s not in teamSignal:
                new=teamSignal+s
                pirate.setTeamSignal(new)

    sig=pirate.getTeamSignal()
    sigSelf=pirate.getSignal()
    
    
    if("att" not in sig and "att" not in sigSelf):
        if "str;" in sigSelf:
            return General_motion_p2(pirate)
        return General_motion_p1(pirate)
    
    if pirate.getCurrentFrame()>=1200:
        if "att" in pirate.getTeamSignal() and pirate.getCurrentFrame()>400:
            sigList=pirate.getTeamSignal().split(";")
            index=findIndex("att",sigList)
            s = sigList[index]
            l = s.split(":")
            x = int(l[2])
            y = int(l[3])

            if moveTo(x,y,pirate)==0:
                curSig=pirate.getSignal()
                if "enemy" in [up[1],down[1],left[1],right[1],nw[1],ne[1],sw[1],se[1]] and "#" not in curSig and pirate.getTotalGunpowder()>=100:
                    pirate.setSignal(curSig+"#;")

            return moveTo(x, y, pirate)

    elif "att" in pirate.getSignal():
        sigList=pirate.getSignal().split(";")
        index=findIndex("att",sigList)
        s = sigList[index]
        l = s.split(":")
        x = int(l[2])
        y = int(l[3])

        t = pirate.trackPlayers()
        island_no = int(l[1])
        signal = t[island_no - 1]
        if signal == "myCaptured":
            removeSigSelf(pirate,"att")
    
        return moveTo(x, y, pirate)
    else:
        return spread(pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    print(team.getCurrentFrame())


    list = s.split(";")
    list[0]=str(team.getTotalPirates())
    team.setTeamSignal(";".join(list))
    index=findIndex("att",list)
    if index:
        list2 = list[index].split(":")
        island_no = int(list2[1])
        signal = l[island_no - 1]
        signal0= l[island_no + 2]
        if signal == "myCaptured" and signal0!="oppCapturing":
                removeSig(team,"att")
    
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    if ("clr" not in s) and ("att" in s):
        pirSigList=team.getListOfSignals()
        num=0
        for i in pirSigList:
            if "#" in i:
                num+=1
        if num>=0.7*team.getTotalPirates():
            team.setTeamSignal(s+"clr:"+str(team.getCurrentFrame())+";")

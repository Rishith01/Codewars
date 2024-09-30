import random 
import math
import time
import numpy as np

name='one_night_work_high_on_caffeine'

def team_signal_update(pirate,x1=-1,y1=-1,x2=-1,y2=-1,x3=-1,y3=-1):    
    
    a=[int(i) for i in pirate.getTeamSignal().split("_")]
    print(a)
    if(x1 != -1):
        a[0]=x1
    if(y1 != -1):
        a[1]=y1
    if(x2 != -1):
        a[2]=x2
    if(y2 != -1):
        a[3]=y2
    if(x3 != -1):
        a[4]=x3
    if(y3 != -1):
        a[5]=y3
    b=""
    for i in range(6):
        b+=str(a[i])+"_"
    b+=str(a[5])
    pirate.setTeamSignal(b)

def checkIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]

    pos = pirate.getPosition()

    s=[int(i) for i in pirate.getTeamSignal().split("_")]
 
    # if(s[0] != -1 or s[1] != -1 or s[2] != -1 or s[3] != -1 or s[4] != -1 or s[5] != -1):
    if(up == "island1"):
        team_signal_update(pirate,x1=pos[0],y1=pos[1]-1)
        return True
    if(up == "island2"):
        team_signal_update(pirate,x2=pos[0],y2=pos[1]-1)
        return True
    if(up == "island3"):
        team_signal_update(pirate,x3=pos[0],y3=pos[1]-1)
        return True
    
    if(right == "island1"):
        team_signal_update(pirate,x1=pos[0]+1,y1=pos[1])
        return True
    if(right == "island2"):
        team_signal_update(pirate,x2=pos[0]+1,y2=pos[1])
        return True
    if(right == "island3"):
        team_signal_update(pirate,x3=pos[0]+1,y3=pos[1])
        return True
    if(left == "island1"):
        team_signal_update(pirate,x1=pos[0]-1,y1=pos[1])
        return True
    if(left == "island2"):
        team_signal_update(pirate,x2=pos[0]-1,y2=pos[1])
        return True
    if(left == "island3"):
        team_signal_update(pirate,x3=pos[0]-1,y3=pos[1])
        return True
    
    if(down == "island1"):
        team_signal_update(pirate,x1=pos[0],y1=pos[1]+1)
        return True
    if(down == "island2"):
        team_signal_update(pirate,x2=pos[0],y2=pos[1]+1)
        return True
    if(down == "island3"):
        team_signal_update(pirate,x3=pos[0],y3=pos[1]+1)
        return True
    return False

    

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


   
def checkEnemy(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    pos = pirate.getPosition()
    if(up=='enemy'):
        moveTo(pos[0]-1,pos[1],pirate)
    if(down=='enemy'):
        moveTo(pos[0]-1,pos[1],pirate)
    if(left=='enemy'):
        moveTo(pos[0],pos[1]-1,pirate)
    if(right=='enemy'):
        moveTo(pos[0],pos[1]-1,pirate)


def circleAround(Pirate):
    id=int(Pirate.getID())
    x=Pirate.getDimensionX()/2
    y=Pirate.getDimensionY()/2
    deploy=Pirate.getDeployPoint()
    b=int(Pirate.getTeamSignal().split('_')[-1])
    # if(deploy==Pirate.getPosition()):
    #     if(Pirate.getSignal != ""):
    #         a=random.randint(0,1)
    #         diag_no = int(random.random()**2 * random.randint(1, x))
            
    #         Pirate.setSignal(str(a)+" "+str(diag_no))
    #signal =int(Pirate.getTeamSignal().split("_")[-1])
    # signal=[]
    # l=Pirate.getSignal().split(" ")
    # for x in l:
    #     signal=signal.append(int(x))
    a=""
    for i in range(len(Pirate.getTeamSignal().split("_"))-1):
       a=a+Pirate.getTeamSignal().split("_")[i]+'_'
    diag_no=id%int(Pirate.getDimensionX()/2)-1
    if(diag_no==-1):
        diag_no=0
    # if(Pirate.getSignal()!=''):
    #   signal=int(Pirate.getSignal())
    # else:
    
    if(Pirate.getSignal()==''):
        b+=1
        Pirate.setSignal(str(b))
    c =int(Pirate.getSignal())
    if(c%8==0 or c%8==1 or c%8==2 or c%8==3 ):
        signal=1

    elif(c%8==5 or c%8==6 or c%8==7 or c%8==4):
        signal=0

    Pirate.setTeamSignal(a+str(b))

    clockwise=False
    if(signal==1):
        clockwise=True
       
    elif(signal==0):
        clockwise=False
       
    radius=int(abs(Pirate.getDimensionX()/2-diag_no))
    # if(random.randint(0,70)==0 and radius!=0):
    #     clockwise = not clockwise
    #     radius+=2
    
    if(chk(Pirate)==1):
        initial = (deploy[0]+diag_no,deploy[0]+diag_no)

    if(chk(Pirate)==2):
        initial = (deploy[0]+diag_no,deploy[1]+(-1)*diag_no)

    if(chk(Pirate)==3):
        initial = (deploy[0]+(-1)*diag_no,deploy[1]+diag_no)

    if(chk(Pirate)==4):
        initial = (deploy[0]+(-1)*diag_no,deploy[1]+(-1)*diag_no)

    position = Pirate.getPosition()
    
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if position not in pos:
            return moveTo(initial[0],initial[1],Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return moveAway(x, y, Pirate)
        else:
            return moveTo(x, y, Pirate)
    else:
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate)
    
def moveAway(x,y,pirate):
    position = pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] > y) * 2 + 1
    if position[1] == y:
        return (position[0] < x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1
    

def chk(pirate):
    posx, posy = pirate.getDeployPoint()
    
    if posx >3 :
        if posy >3:
            return 4
        else:
            return 3
    else:
        if posy >3:
            return 2
        else:
            return 1    

def ActPirate(pirate):
    if(pirate.getCurrentFrame()==1):
        pirate.setTeamSignal("-1_-1_-1_-1_-1_-1_0")
    checkIsland(pirate)
    print(pirate.getTeamSignal())
    print(pirate.getCurrentFrame())
    flag=False
    x=pirate.trackPlayers()
    if x[-1]=="oppCaptured"and x[-2]=="oppCaptured" :
        flag=True
    if x[-1]=="oppCaptured"and x[-3]=="oppCaptured" :
        flag=True
    if x[-3]=="oppCaptured"and x[-2]=="oppCaptured" :
        flag=True

    if(pirate.getCurrentFrame()<=500 and (not flag)):
        return circleAround(pirate)
    else:
        if(pirate.getSignal() is not 'c1' and pirate.getSignal() is not 'c2' and pirate.getSignal() is not 'c3'):
            a=random.randint(0,3)
            if(a==1):
                pirate.setSignal('c1')
            elif(a==2):
                pirate.setSignal('c2')
            else:
                pirate.setSignal('c3')
            
        return Capture(pirate)


def Capture(pirate):
    x=pirate.getSignal()
    z=pirate.getTeamSignal().split('_')
    if(x=='c1'):
        return moveTo(int(z[0]),int(z[1]),pirate)
    elif(x=='c2'):
        return moveTo(int(z[2]),int(z[3]),pirate)
    elif(x=='c3'):
        return moveTo(int(z[4]),int(z[5]),pirate)
       

def ActTeam(team):
    pass
    

import random
import math

name = "Babbar Sher"

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
    
def checkIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        if up[0:-1] == "island":
            return up
        if down[0:-1] == "island":
            return down
        if right[0:-1] == "island":
            return right
        if left[0:-1] == "island":
            return left 
    else:
        return False
    
def CenterNkill(pirate, up, down, left, right, ne, nw, se, sw):
    x, y = pirate.getPosition()
    center = [x, y]
    islNum = 0
    if(up[:-1] == "island" and down[:-1] == "island" and left[:-1] == "island" and right[:-1] == "island" and ne[:-1] == "island" and nw[:-1] == "island" and se[:-1] == "island" and sw[:-1] == "island"):
        center = [x, y]
        islNum = int(up[-1])
    elif(up[:-1] != "island" and down[:-1] == "island" and left[:-1] == "island" and right[:-1] == "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] == "island" and sw[:-1] == "island"):
        center = [x, y + 1]
        islNum = int(down[-1])
    elif(up[:-1] != "island" and down[:-1] == "island" and left[:-1] == "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] != "island" and sw[:-1] == "island"):
        center = [x - 1, y + 1]
        islNum = int(down[-1])
    elif(up[:-1] == "island" and down[:-1] == "island" and left[:-1] == "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] == "island" and se[:-1] != "island" and sw[:-1] == "island"):
        center = [x - 1, y]
        islNum = int(up[-1])
    elif(up[:-1] == "island" and down[:-1] != "island" and left[:-1] == "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] == "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x - 1, y - 1]
        islNum = int(up[-1])
    elif(up[:-1] == "island" and down[:-1] != "island" and left[:-1] == "island" and right[:-1] == "island" and ne[:-1] == "island" and nw[:-1] == "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x, y - 1]
        islNum = int(up[-1])
    elif(up[:-1] == "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] == "island" and ne[:-1] == "island" and nw[:-1] != "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x + 1, y - 1]
        islNum = int(up[-1])
    elif(up[:-1] == "island" and down[:-1] == "island" and left[:-1] != "island" and right[:-1] == "island" and ne[:-1] == "island" and nw[:-1] != "island" and se[:-1] == "island" and sw[:-1] != "island"):
        center = [x + 1, y]
        islNum = int(up[-1])
    elif(up[:-1] != "island" and down[:-1] == "island" and left[:-1] != "island" and right[:-1] == "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] == "island" and sw[:-1] != "island"):
        center = [x + 1, y + 1]
        islNum = int(down[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] == "island" and sw[:-1] != "island"):
        center = [x + 2, y + 2]
        islNum = int(se[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] == "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] == "island" and sw[:-1] != "island"):
        center = [x + 2, y + 1]
        islNum = int(se[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] == "island" and ne[:-1] == "island" and nw[:-1] != "island" and se[:-1] == "island" and sw[:-1] != "island"):
        center = [x + 2, y]
        islNum = int(se[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] == "island" and ne[:-1] == "island" and nw[:-1] != "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x + 2, y - 1]
        islNum = int(ne[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] == "island" and nw[:-1] != "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x + 2, y - 2]
        islNum = int(ne[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] != "island" and sw[:-1] == "island"):
        center = [x - 2, y + 2]
        islNum = int(sw [-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] == "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] != "island" and sw[:-1] == "island"):
        center = [x - 2, y + 1]
        islNum = int(sw[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] == "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] == "island" and se[:-1] != "island" and sw[:-1] == "island"):
        center = [x - 2, y]
        islNum = int(sw[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] == "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] == "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x - 2, y - 1]
        islNum = int(nw[-1])
    elif(up[:-1] != "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] == "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x - 2, y - 2]
        islNum = int(nw[-1])
    elif(up[:-1] != "island" and down[:-1] == "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] == "island" and sw[:-1] != "island"):
        center = [x + 1, y + 2]
        islNum = int(down[-1])
    elif(up[:-1] != "island" and down[:-1] == "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] == "island" and sw[:-1] == "island"):
        center = [x, y + 2]
        islNum = int(down[-1])
    elif(up[:-1] != "island" and down[:-1] == "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] != "island" and se[:-1] != "island" and sw[:-1] == "island"):
        center = [x - 1, y + 2]
        islNum = int(down[-1])
    elif(up[:-1] == "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] == "island" and nw[:-1] != "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x + 1 , y - 2]
        islNum = int(up[-1])
    elif(up[:-1] == "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] == "island" and nw[:-1] == "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x, y - 2]
        islNum = int(up[-1])
    elif(up[:-1] == "island" and down[:-1] != "island" and left[:-1] != "island" and right[:-1] != "island" and ne[:-1] != "island" and nw[:-1] == "island" and se[:-1] != "island" and sw[:-1] != "island"):
        center = [x - 1, y - 2]
        islNum = int(up[-1])
    return [center[0], center[1], islNum]

def MoveX(pirate, y_coordi, x_end):
    if pirate.getPosition()[1] != y_coordi:
        return moveTo(pirate.getPosition()[0], y_coordi, pirate)
    else:
        return moveTo(x_end, y_coordi, pirate)
    
def MoveY(pirate, x_coordi, y_end):
    if pirate.getPosition()[0] != x_coordi:
        return moveTo(x_coordi, pirate.getPosition()[1], pirate)
    else:
        return moveTo(x_coordi, y_end, pirate)
    
def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if initial != "abc":
            return moveTo(pos[0], pos[1], Pirate)
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
            Pirate,
        )
    
def Sweep(x_start, y_start, pirate, dimX, dimY, n):
    if n % 2 == 0 and n <= dimY:
        if n <= dimY//2:
            if (x_start,y_start) == (0,0):
                return MoveX(pirate, (dimY/2)-n+1, dimY -1 -((dimY/2)-n+1))
            if (x_start,y_start) == (dimX-1,0):
                return MoveX(pirate, (dimY/2)-n+1, (dimY/2)-n+1)
            if (x_start,y_start) == (0,dimY-1):
                return MoveX(pirate, (dimY/2)+n-2, (dimY/2)+n-2)
            if (x_start,y_start) == (dimX-1,dimY-1):
                return MoveX(pirate, (dimY/2)+n-2, dimY-1 -((dimY/2)+n-2))
        else:
            if (x_start,y_start) == (0,0):
                return MoveX(pirate, (dimY)-n, n-1)
            if (x_start,y_start) == (dimX-1,0):
                return MoveX(pirate, (dimY)-n, (dimY)-n)
            if (x_start,y_start) == (0,dimY-1):
                return MoveX(pirate, n-1, n-1)
            if (x_start,y_start) == (dimX-1,dimY-1):
                return MoveX(pirate, n-1, dimY-n)
    if n % 2 == 1 and n <= dimX:
        if n <= dimX//2:
            if (x_start,y_start) == (0,0):
                return MoveY(pirate, (dimX/2)-n, (dimX/2)+n-1)
            if (x_start,y_start) == (dimX-1,0):
                return MoveY(pirate, (dimX/2)+n-1, (dimX/2)+n-1)
            if (x_start,y_start) == (0,dimY-1):
                return MoveY(pirate, (dimX/2)-n, (dimX/2)-n)
            if (x_start,y_start) == (dimX-1,dimY-1):
                return MoveY(pirate, (dimX/2)+n-1, (dimX/2)-n)
        else:
            if (x_start,y_start) == (0,0):
                return MoveY(pirate, dimX-n-1, n)
            if (x_start,y_start) == (dimX-1,0):
                return MoveY(pirate, n, n)
            if (x_start,y_start) == (0,dimY-1):
                return MoveY(pirate, dimX-n-1, dimX-n-1)
            if (x_start,y_start) == (dimX-1,dimY-1):
                return MoveY(pirate, n, dimX-n-1)
            
def Attack(x_start, y_start, pirate, dimX, dimY, n, x_end, y_end, x, y):
    if n % 2 == 0:
        if y_start == 0:
            return MoveY(pirate, x, dimY-1)
        else:
            return MoveY(pirate, x, 0)
    if n % 2 == 1:
        if x_start == 0:
            return MoveX(pirate, y, dimX-1)
        else:
            return MoveX(pirate, y, 0)

def quadrantAttack(pirate, quadrant, radius): ## Divide the plane into four parts about its center, and then traditional Cartesian Conventions
    pid = pirate.getID()
    dimX = int(pirate.getDimensionX())
    dimY = int(pirate.getDimensionY())
    if 0 <= quadrant < 5 and type(quadrant) == int:
        x_cen = dimX/4
        y_cen = dimY/4
        if(quadrant == 2):
            x_cen = dimX/4
            y_cen = dimY/4
        elif(quadrant == 1):
            x_cen = 3* dimX/4 - 1
            y_cen = dimY/4
        elif(quadrant == 3):
            x_cen = dimX/4
            y_cen = 3* dimY/4 - 1
        else: ## quadrant = 4
            x_cen = 3 * dimX/4 - 1
            y_cen = 3 * dimY/4 - 1
        return circleAround(x_cen, y_cen, radius, pirate)
    else:
        print("Logical Error in quadrant attack")

def ActPirate(pirate):
    # print(len(pirate.getTeamSignal().split(" ")))
    global List
    global b
    currFrame = pirate.getCurrentFrame()

    pid = int(pirate.getID())
    deploy_quad = -1
    x_deploy, y_deploy = pirate.getDeployPoint()
    if(x_deploy == 0 and y_deploy == 0):
        deploy_quad = 2
    elif x_deploy == 0:
        deploy_quad = 3
    elif y_deploy == 0:
        deploy_quad = 1
    else: 
        deploy_quad = 0
    
    print(List)
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]
    x, y = pirate.getPosition()
    s = pirate.trackPlayers()
    x_start,y_start = pirate.getDeployPoint()
    dimX = int(pirate.getDimensionX())
    dimY = int(pirate.getDimensionY())
    n = int(pirate.getID())
    for i in [0,dimX-1]: 
        if i != x_start: 
            x_end=i
    for i in [0,dimY-1]: 
        if i != y_start: 
            y_end=i
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
        or (up == "island1" and s[3] == "oppCapturing")
        or (up == "island2" and s[4] == "oppCapturing")
        or (up == "island2" and s[5] == "oppCapturing")
    ):
        Result = CenterNkill(pirate, up, down, left, right, ne, nw, se, sw)
        x_c = Result[0]
        y_c = Result[1]
        # islNum = int(Result[2])
        # print(type(Result), type(x_c), type(y_c), type(islNum))
        # for i in range(3):
        #     for j in range(3):
        #         print(islNum)
        #         List[islNum-1][3*i+j] = [x_c + i - 1, y_c + j - 1]
        if pirate.getTeamSignal() == "":
            sig=up[-1] + "," + str(x_c) + "," + str(y_c) + ",0"
            pirate.setTeamSignal(sig)
        elif len(pirate.getTeamSignal().split(" ")) == 1 and up[-1] != pirate.getTeamSignal()[0]:
            team_assigned = pirate.getTeamSignal()[-1]
            team_to_be_assigned = "1" if team_assigned == "0" else "0"
            sig=up[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
            s=pirate.getTeamSignal()
            pirate.setTeamSignal(s+" "+sig)
        elif len(pirate.getTeamSignal().split(" ")) == 2:
            s=pirate.getTeamSignal()
            L=s.split(" ")
            listi=[x[0] for x in L]
            listt=[x[-1] for x in L]
            if up[-1] not in listi:
                for a in ["0","1","2"]:
                    if a not in listt:
                        team_to_be_assigned=a
                sig=up[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
                s=pirate.getTeamSignal()
                pirate.setTeamSignal(s+" "+sig)
    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
        or (down == "island1" and s[3] == "oppCapturing")
        or (down == "island2" and s[4] == "oppCapturing")
        or (down == "island2" and s[5] == "oppCapturing")
    ):
        Result = CenterNkill(pirate, up, down, left, right, ne, nw, se, sw)
        x_c = Result[0]
        y_c = Result[1]
        # islNum = int(Result[2])
        # print(type(Result), type(x_c), type(y_c), type(islNum))
        # for i in range(3):
        #     for j in range(3):
        #         print(islNum)
        #         List[islNum-1][3*i+j] = [x_c + i - 1, y_c + j - 1]
        if pirate.getTeamSignal() == "":
            sig=down[-1] + "," + str(x_c) + "," + str(y_c) + ",0"
            pirate.setTeamSignal(sig)
        elif len(pirate.getTeamSignal().split(" ")) == 1 and down[-1] != pirate.getTeamSignal()[0]:
            team_assigned = pirate.getTeamSignal()[-1]
            team_to_be_assigned = "1" if team_assigned == "0" else "0"
            sig=down[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
            s=pirate.getTeamSignal()
            pirate.setTeamSignal(s+" "+sig)
        elif len(pirate.getTeamSignal().split(" ")) == 2:
            s=pirate.getTeamSignal()
            L=s.split(" ")
            listi=[x[0] for x in L]
            listt=[x[-1] for x in L]
            if down[-1] not in listi:
                for a in ["0","1","2"]:
                    if a not in listt:
                        team_to_be_assigned=a
                sig=down[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
                s=pirate.getTeamSignal()
                pirate.setTeamSignal(s+" "+sig)

    if (
        (ne == "island1" and s[0] != "myCaptured")
        or (ne == "island2" and s[1] != "myCaptured")
        or (ne == "island3" and s[2] != "myCaptured")
        or (ne == "island1" and s[3] == "oppCapturing")
        or (ne == "island2" and s[4] == "oppCapturing")
        or (ne == "island2" and s[5] == "oppCapturing")
    ):
        Result = CenterNkill(pirate, up, down, left, right, ne, nw, se, sw)
        x_c = Result[0]
        y_c = Result[1]
        # islNum = int(Result[2])
        # print(type(Result), type(x_c), type(y_c), type(islNum))
        # for i in range(3):
        #     for j in range(3):
        #         print(islNum)
        #         List[islNum-1][3*i+j] = [x_c + i - 1, y_c + j - 1]
        if pirate.getTeamSignal() == "":
            sig=ne[-1] + "," + str(x_c) + "," + str(y_c) + ",0"
            pirate.setTeamSignal(sig)
        elif len(pirate.getTeamSignal().split(" ")) == 1 and ne[-1] != pirate.getTeamSignal()[0]:
            team_assigned = pirate.getTeamSignal()[-1]
            team_to_be_assigned = "1" if team_assigned == "0" else "0"
            sig=ne[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
            s=pirate.getTeamSignal()
            pirate.setTeamSignal(s+" "+sig)
        elif len(pirate.getTeamSignal().split(" ")) == 2:
            s=pirate.getTeamSignal()
            L=s.split(" ")
            listi=[x[0] for x in L]
            listt=[x[-1] for x in L]
            if ne[-1] not in listi:
                for a in ["0","1","2"]:
                    if a not in listt:
                        team_to_be_assigned=a
                sig=ne[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
                s=pirate.getTeamSignal()
                pirate.setTeamSignal(s+" "+sig)

    if (
        (nw == "island1" and s[0] != "myCaptured")
        or (nw == "island2" and s[1] != "myCaptured")
        or (nw == "island3" and s[2] != "myCaptured")
        or (nw == "island1" and s[3] == "oppCapturing")
        or (nw == "island2" and s[4] == "oppCapturing")
        or (nw == "island2" and s[5] == "oppCapturing")
    ):
        Result = CenterNkill(pirate, up, down, left, right, ne, nw, se, sw)
        x_c = Result[0]
        y_c = Result[1]
        islNum = int(Result[2])
        # print(type(Result), type(x_c), type(y_c), type(islNum))
        # for i in range(3):
        #     for j in range(3):
        #         print(islNum)
        #         List[islNum-1][3*i+j] = [x_c + i - 1, y_c + j - 1]
        if pirate.getTeamSignal() == "":
            sig=nw[-1] + "," + str(x_c) + "," + str(y_c) + ",0"
            pirate.setTeamSignal(sig)
        elif len(pirate.getTeamSignal().split(" ")) == 1 and nw[-1] != pirate.getTeamSignal()[0]:
            team_assigned = pirate.getTeamSignal()[-1]
            team_to_be_assigned = "1" if team_assigned == "0" else "0"
            sig=nw[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
            s=pirate.getTeamSignal()
            pirate.setTeamSignal(s+" "+sig)
        elif len(pirate.getTeamSignal().split(" ")) == 2:
            s=pirate.getTeamSignal()
            L=s.split(" ")
            listi=[x[0] for x in L]
            listt=[x[-1] for x in L]
            if nw[-1] not in listi:
                for a in ["0","1","2"]:
                    if a not in listt:
                        team_to_be_assigned=a
                sig=nw[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
                s=pirate.getTeamSignal()
                pirate.setTeamSignal(s+" "+sig)

    if (
        (se == "island1" and s[0] != "myCaptured")
        or (se == "island2" and s[1] != "myCaptured")
        or (se == "island3" and s[2] != "myCaptured")
        or (se == "island1" and s[3] == "oppCapturing")
        or (se == "island2" and s[4] == "oppCapturing")
        or (se == "island2" and s[5] == "oppCapturing")
    ):
        Result = CenterNkill(pirate, up, down, left, right, ne, nw, se, sw)
        x_c = Result[0]
        y_c = Result[1]
        # islNum = int(Result[2])
        # print(type(Result), type(x_c), type(y_c), type(islNum))
        # for i in range(3):
        #     for j in range(3):
        #         print(islNum)
        #         List[islNum-1][3*i+j] = [x_c + i - 1, y_c + j - 1]
        if pirate.getTeamSignal() == "":
            sig=se[-1] + "," + str(x_c) + "," + str(y_c) + ",0"
            pirate.setTeamSignal(sig)
        elif len(pirate.getTeamSignal().split(" ")) == 1 and se[-1] != pirate.getTeamSignal()[0]:
            team_assigned = pirate.getTeamSignal()[-1]
            team_to_be_assigned = "1" if team_assigned == "0" else "0"
            sig=se[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
            s=pirate.getTeamSignal()
            pirate.setTeamSignal(s+" "+sig)
        elif len(pirate.getTeamSignal().split(" ")) == 2:
            s=pirate.getTeamSignal()
            L=s.split(" ")
            listi=[x[0] for x in L]
            listt=[x[-1] for x in L]
            if se[-1] not in listi:
                for a in ["0","1","2"]:
                    if a not in listt:
                        team_to_be_assigned=a
                sig=se[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
                s=pirate.getTeamSignal()
                pirate.setTeamSignal(s+" "+sig)

    if (
        (sw == "island1" and s[0] != "myCaptured")
        or (sw == "island2" and s[1] != "myCaptured")
        or (sw == "island3" and s[2] != "myCaptured")
        or (sw == "island1" and s[3] == "oppCapturing")
        or (sw == "island2" and s[4] == "oppCapturing")
        or (sw == "island2" and s[5] == "oppCapturing")
    ):
        Result = CenterNkill(pirate, up, down, left, right, ne, nw, se, sw)
        x_c = Result[0]
        y_c = Result[1]
        # islNum = int(Result[2])
        # print(type(Result), type(x_c), type(y_c), type(islNum))
        # for i in range(3):
        #     for j in range(3):
        #         print(islNum)
        #         List[islNum-1][3*i+j] = [x_c + i - 1, y_c + j - 1]
        if pirate.getTeamSignal() == "":
            sig=sw[-1] + "," + str(x_c) + "," + str(y_c) + ",0"
            pirate.setTeamSignal(sig)
        elif len(pirate.getTeamSignal().split(" ")) == 1 and sw[-1] != pirate.getTeamSignal()[0]:
            team_assigned = pirate.getTeamSignal()[-1]
            team_to_be_assigned = "1" if team_assigned == "0" else "0"
            sig=sw[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
            s=pirate.getTeamSignal()
            pirate.setTeamSignal(s+" "+sig)
        elif len(pirate.getTeamSignal().split(" ")) == 2:
            s=pirate.getTeamSignal()
            L=s.split(" ")
            listi=[x[0] for x in L]
            listt=[x[-1] for x in L]
            if sw[-1] not in listi:
                for a in ["0","1","2"]:
                    if a not in listt:
                        team_to_be_assigned=a
                sig=sw[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
                s=pirate.getTeamSignal()
                pirate.setTeamSignal(s+" "+sig)

    
    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
        or (left == "island1" and s[3] == "oppCapturing")
        or (left == "island2" and s[4] == "oppCapturing")
        or (left == "island2" and s[5] == "oppCapturing")
    ):
        Result = CenterNkill(pirate, up, down, left, right, ne, nw, se, sw)
        x_c = Result[0]
        y_c = Result[1]
        # islNum = int(Result[2])
        # print(type(Result), type(x_c), type(y_c), type(islNum))
        # for i in range(3):
        #     for j in range(3):
        #         print(islNum)
        #         List[islNum-1][3*i+j] = [x_c + i - 1, y_c + j - 1]
        if pirate.getTeamSignal() == "":
            sig=left[-1] + "," + str(x_c) + "," + str(y_c) + ",0"
            pirate.setTeamSignal(sig)
        elif len(pirate.getTeamSignal().split(" ")) == 1 and left[-1] != pirate.getTeamSignal()[0]:
            team_assigned = pirate.getTeamSignal()[-1]
            team_to_be_assigned = "1" if team_assigned == "0" else "0"
            sig=left[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
            s=pirate.getTeamSignal()
            pirate.setTeamSignal(s+" "+sig)
        elif len(pirate.getTeamSignal().split(" ")) == 2:
            s=pirate.getTeamSignal()
            L=s.split(" ")
            listi=[x[0] for x in L]
            listt=[x[-1] for x in L]
            if left[-1] not in listi:
                for a in ["0","1","2"]:
                    if a not in listt:
                        team_to_be_assigned=a
                sig=left[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
                s=pirate.getTeamSignal()
                pirate.setTeamSignal(s+" "+sig)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
        or (right == "island1" and s[3] == "oppCapturing")
        or (right == "island2" and s[4] == "oppCapturing")
        or (right == "island2" and s[5] == "oppCapturing")
    ):
        Result = CenterNkill(pirate, up, down, left, right, ne, nw, se, sw)
        x_c = int(Result[0])
        y_c = Result[1]
        # islNum = int(Result[2])
        # print(type(Result), type(x_c), type(y_c), type(islNum))
        # for i in range(3):
        #     for j in range(3):
        #         print(islNum)
        #         List[islNum-1][3*i+j] = [x_c + i - 1, y_c + j - 1]
        if pirate.getTeamSignal() == "":
            sig=right[-1] + "," + str(x_c) + "," + str(y_c) + ",0"
            pirate.setTeamSignal(sig)
        elif len(pirate.getTeamSignal().split(" ")) == 1 and right[-1] != pirate.getTeamSignal()[0]:
            team_assigned = pirate.getTeamSignal()[-1]
            team_to_be_assigned = "1" if team_assigned == "0" else "0"
            sig=right[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
            s=pirate.getTeamSignal()
            pirate.setTeamSignal(s+" "+sig)
        elif len(pirate.getTeamSignal().split(" ")) == 2:
            s=pirate.getTeamSignal()
            L=s.split(" ")
            listi=[x[0] for x in L]
            listt=[x[-1] for x in L]
            if right[-1] not in listi:
                for a in ["0","1","2"]:
                    if a not in listt:
                        team_to_be_assigned=a
                sig=right[-1] + "," + str(x_c) + "," + str(y_c) + "," + team_to_be_assigned
                s=pirate.getTeamSignal()
                pirate.setTeamSignal(s+" "+sig)
    if dimX+dimY+20 < currFrame < 1000:
        b = b + 1
        if(b < 58):
            if(b % 58 in range(1,21)):
                return circleAround(dimX//2, dimY//2, b, pirate)
            elif(b % 58 in range(21, 32)):
                return circleAround(dimX//2, dimY//2, b-16, pirate)
            elif(b % 58 in range(32, 48)):
                return circleAround(dimX//2, dimY//2, b-27, pirate)
            elif(b % 58 in range(48, 58)):
                return circleAround(dimX//2, dimY//2, (((b)%58)//2)-13, pirate)
        if(b-57 < 58):
            if((b-57) % 58 in range(1,21)):
                return circleAround(dimX//2, dimY//2, b-57, pirate)
            elif((b-57) % 58 in range(21, 32)):
                return circleAround(dimX//2, dimY//2, b-57-16, pirate)
            elif((b-57) % 58 in range(32, 48)):
                return circleAround(dimX//2, dimY//2, b-57-27, pirate)
            elif((b-57) % 58 in range(48, 58)):
                return circleAround(dimX//2, dimY//2, (((b-57)%58)//2)-13, pirate)
    if (n % 2 == 0 and n <= dimY) or (n % 2 == 0 and n <= 2 * dimY):
        if (pirate.getSignal() != "1" and pirate.getSignal() != "12") and ((y_start == 0 and x_start == 0 and x + y != dimX - 1) or (y_start == dimY-1 and x_start == 0 and x != y) or (x_start == dimX - 1 and y_start == 0 and x != y) or (x_start == dimX - 1 and y_start == dimY - 1 and x+y != dimX-1)):
            if n <= dimY:
                return Sweep(x_start, y_start, pirate, dimX, dimY, n)
            else:
                return Sweep(x_start, y_start, pirate, dimX, dimY, n-dimX)
        elif pirate.getSignal() != "12":
            pirate.setSignal("1")
            if (y_start == 0 and y == dimY-2) or (y_start == dimY-1 and y == 1):
                pirate.setSignal("12")
            if n <= dimY:
                return Attack(x_start, y_start, pirate, dimX, dimY, n, x_end, y_end, x, y)
            else:
                return Attack(x_start, y_start, pirate, dimX, dimY, n-dimX, x_end, y_end, x, y)
    if n % 2 == 1 and n <= 2 * dimX:
        if (pirate.getSignal() != "1" and pirate.getSignal() != "12") and ((y_start == 0 and x_start == 0 and x + y != dimX - 1) or (y_start == dimY-1 and x_start == 0 and x != y) or (x_start == dimX - 1 and y_start == 0 and x != y) or (x_start == dimX - 1 and y_start == dimY - 1 and x+y != dimX-1)):
            if n <= dimX:
                return Sweep(x_start, y_start, pirate, dimX, dimY, n)
            else:
                return Sweep(x_start, y_start, pirate, dimX, dimY, n-dimX)
        elif pirate.getSignal() != "12":
            pirate.setSignal("1")
            if (x_start == 0 and x == dimX -2) or (x_start == dimX-1 and x == 1):
                pirate.setSignal("12")
            if n <= dimX:
                return Attack(x_start, y_start, pirate, dimX, dimY, n, x_end, y_end, x, y)
            else:
                return Attack(x_start, y_start, pirate, dimX, dimY, n-dimX, x_end, y_end, x, y)
            
    # currFrame = pirate.getCurrentFrame()

    # pid = int(pirate.getID())
    # deploy_quad = -1
    # x_deploy, y_deploy = pirate.getDeployPoint()
    # if(x_deploy == 0 and y_deploy == 0):
    #     deploy_quad = 2
    # elif x_deploy == 0:
    #     deploy_quad = 3
    # elif y_deploy == 0:
    #     deploy_quad = 1
    # else: 
    #     deploy_quad = 4

    # if currFrame < 1000:
    #     b = b + 1
    #     if(pid % 16 in [1,2,3,4,5]):
    #         return quadrantAttack(pirate, deploy_quad, pid % 15)
    #     elif(pid % 16 in range(6, 16)):
    #         return quadrantAttack(pirate, deploy_quad, 5 + (pid - 5))
        
    # if b < dimX//2:
    #     b = b + 1
    #     return circleAround(dimX//2, dimY//2, b-1, pirate)
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        List = s.split(" ")
        for i in List:
            List2 = i.split(',')
            x = int(List2[1])
            y = int(List2[2])
            if n % 3 == int(i[-1]):
                return circleAround(x, y, random.randint(0, 1), pirate)
    return circleAround(dimX//2, dimY//2, (int(pirate.getID())%(dimX//2)) + 1, pirate)

def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    if team.getCurrentFrame() > 1000:
        team.buildWalls(1)
        team.buildWalls(2)
        team.buildWalls(3)
    print(s)
    global List
    global b
    b=0
    try:
        abc=List[0]
    except:
        List=[[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        L=s.split(" ")
        for i in L:
            print(i[0])
            island_no = int(i[0])
            signal = l[island_no - 1]
            if signal == "myCaptured":
                L.remove(i)
                print(L)
                if L != []:
                    team.setTeamSignal(L[0])
                else:
                    team.setTeamSignal('')
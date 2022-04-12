import sys
DIRECTIONS={-1:"west", 1:"east", -2:"north", 2:"south"}

def heal(robot,amount,log):
    robot[0]+=int(amount)
    log.write(f"Healed for {amount} HP.\n")
    return(robot)

def defend(robot,log):
    robot[1]=True
    log.write("Defended.\n")
    return(robot)

def take_dmg(robot,amount,log):
    if robot[1]:
        robot[0]-=int(amount)//2
        robot[1]=False
        log.write(f"Took {int(amount)//2} damage (Blocked half) and is no longer defending.\n")
    else:
        robot[0]-=int(amount)
        log.write(f"Took {amount} damage.\n")
    return(robot)

def turn(robot,direction,log):
    directions={"west":-1, "east":1, "north":-2, "south":2}
    robot[2]=directions[direction]
    log.write(f"Turned {direction}.\n")
    return(robot)

def move(robot,amount,log):
    newpos = 0
    directions={-1:"west", 1:"east", -2:"north", 2:"south"}
    if  1 == abs(robot[2]):
        newpos = robot[3][0] + int(amount)*robot[2]
    if 2 == abs(robot[2]):
        newpos = robot[3][1] + int(amount)*(robot[2]//2)
    log.write(f"Moved {amount} spaces {directions[robot[2]]}.\n")
    robot[3][abs(robot[2]//2)] = newpos
    if newpos > 63 or newpos < 0:
        robot[3][abs(robot[2]//2)] = 0
        log.write("Cannot move forward!\n")
    return(robot)

def do_turn(command,log,robot):
    if command[0] == "heal":
        robot = heal(robot,command[1],log)
    if command[0] == "defend":
        robot = defend(robot,log)
    if command[0] == "take_dmg":
        robot = take_dmg(robot,command[1],log)
    if command[0] == "turn":
        robot = turn(robot,command[1],log)
    if command[0] == "move":
        robot = move(robot,command[1],log)
    log.write(f"HP: {robot[0]}, Defending: {robot[1]}, Facing: {DIRECTIONS[robot[2]]}, Position: {robot[3]}\n\n")
    return(robot)

robot=[100,False,-1,[0,0]]#x,y
args = (sys.argv)
args.pop(0)
def main(commands,logfile,robot):
    with open(logfile,"w") as log:
        for line in commands:
            
            line = line.replace("\n","")
            line = line.split(" ")
            robot = do_turn(line,log,robot)
            if robot[0] < 1:
                log.write("Robot has died.")
                break

if "start" in args:
    if args[2] == "start":
        with open(args[1],"r") as commands:
            main(commands,args[0],robot)
    with open("usercommands.txt","w") as log:
        while True:
            arg = input("Input next command ")
            if arg == "stop":
                log.write("Stopped.")
                break
            arg = arg.split(" ")
            robot = do_turn(arg,log,robot)
            if robot[0] < 1:
                log.write("Robot has died.")
                break
else:
    with open(args[1],"r") as commands:
        main(commands,args[0],robot)

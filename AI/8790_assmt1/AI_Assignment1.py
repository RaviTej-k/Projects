import sys,os.path
import numpy as np

# Defining methods used
methods = ["bfs","ucs","dfs","dls","ids","greedy","a*"]
# Defining the default method to be used
method = "a*"

# Function to read goal/start file and store it in numpy 2D array
def read(file):
    txt_file = open(file,"r")
    puzzle = txt_file.read()
    puzzle_nums = puzzle.replace("\n"," ").split(" ")
    txt_file.close()
    # Consider only elements needed from the file
    puzzle_nums = list(map(int, puzzle_nums[:9]))
    return np.array(puzzle_nums).reshape(3, 3)

# Function to define the action to be taken
def action(tile,direction,move):
    action = move.copy()
    action.append(" Move "+ str(tile) + " " +direction)
    return action

# Function to define the path
def path(pathway,node):
    path = pathway.copy()
    path.append(node)
    return path

# Function to add node and its details to the fringe
def addtofringe(state_n,cost_n,level,path_n,action_n):
    fringe["states"].append(state_n) 
    fringe["cost"].append(cost_n) 
    fringe["level"].append(level+1)
    fringe["path"].append(path_n)
    fringe["action"].append(action_n)
    
    # To append only heuristic value for GREEDY and A* search
    if method == "greedy" or method == "a*":  
            heuristic_n = heuristic_value(state_n)
            fringe["heuristic"].append(heuristic_n)
            
            # To append f(n) value for A* search
            if method == "a*":
                fringe["fvalue"].append(cost_n+heuristic_n)


# Function to expand all possible child nodes
def expand_all_possible_nodes(node,cost,level,method,pathway,move):
    if node[0][0] == 0:
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[0][1]
        path_n = path(pathway,node)
        action_n = action(state_n[0][1],"Left",move)
        state_n[0][0],state_n[0][1] = state_n[0][1],state_n[0][0]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[1][0]
        path_n = path(pathway,node)
        action_n = action(state_n[1][0],"Up",move)
        state_n[0][0],state_n[1][0] = state_n[1][0],state_n[0][0]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 2
    
    elif node[0][1] == 0:
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[0][2]
        path_n = path(pathway,node)
        action_n = action(state_n[0][2],"Left",move)
        state_n[0][1],state_n[0][2] = state_n[0][2],state_n[0][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[1][1]
        path_n = path(pathway,node)
        action_n = action(state_n[1][1],"Up",move)
        state_n[0][1],state_n[1][1] = state_n[1][1],state_n[0][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Third state
        state_n = node.copy()
        cost_n = cost + state_n[0][0]
        path_n = path(pathway,node)
        action_n = action(state_n[0][0],"Right",move)
        state_n[0][1],state_n[0][0] = state_n[0][0],state_n[0][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 3
    
    elif node[0][2] == 0:
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[1][2]
        path_n = path(pathway,node)
        action_n = action(state_n[1][2],"Up",move)
        state_n[0][2],state_n[1][2] = state_n[1][2],state_n[0][2]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[0][1]
        path_n = path(pathway,node)
        action_n = action(state_n[0][1],"Right",move)
        state_n[0][2],state_n[0][1] = state_n[0][1],state_n[0][2]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 2
    
    elif node[1][0] == 0:
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[0][0]
        path_n = path(pathway,node)
        action_n = action(state_n[0][0],"Down",move)
        state_n[1][0],state_n[0][0] = state_n[0][0],state_n[1][0]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[1][1]
        path_n = path(pathway,node)
        action_n = action(state_n[1][1],"Left",move)
        state_n[1][0],state_n[1][1] = state_n[1][1],state_n[1][0]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Third state
        state_n = node.copy()
        cost_n = cost + state_n[2][0]
        path_n = path(pathway,node)
        action_n = action(state_n[2][0],"Up",move)
        state_n[1][0],state_n[2][0] = state_n[2][0],state_n[1][0]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 3
    
    elif node[1][1] == 0:
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[1][0]
        path_n = path(pathway,node)
        action_n = action(state_n[1][0],"Right",move)
        state_n[1][1],state_n[1][0] = state_n[1][0],state_n[1][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)
    
        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[0][1]
        path_n = path(pathway,node)
        action_n = action(state_n[0][1],"Down",move)
        state_n[1][1],state_n[0][1] = state_n[0][1],state_n[1][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Third state
        state_n = node.copy()
        cost_n = cost + state_n[1][2]
        path_n = path(pathway,node)
        action_n = action(state_n[1][2],"Left",move)
        state_n[1][1],state_n[1][2] = state_n[1][2],state_n[1][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Fourth state 
        state_n = node.copy()
        cost_n = cost + state_n[2][1]
        path_n = path(pathway,node)
        action_n = action(state_n[2][1],"Up",move)
        state_n[1][1],state_n[2][1] = state_n[2][1],state_n[1][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 4
    
    elif node[1][2] == 0:
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[2][2]
        path_n = path(pathway,node)
        action_n = action(state_n[2][2],"Up",move)
        state_n[1][2],state_n[2][2] = state_n[2][2],state_n[1][2]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[1][1]
        path_n = path(pathway,node)
        action_n = action(state_n[1][1],"Right",move)
        state_n[1][2],state_n[1][1] = state_n[1][1],state_n[1][2]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Third state
        state_n = node.copy()
        cost_n = cost + state_n[0][2]
        path_n = path(pathway,node)
        action_n = action(state_n[0][2],"Down",move)
        state_n[1][2],state_n[0][2] = state_n[0][2],state_n[1][2]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 3
    
    elif node[2][0] == 0:
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[1][0]
        path_n = path(pathway,node)
        action_n = action(state_n[1][0],"Down",move)
        state_n[2][0],state_n[1][0] = state_n[1][0],state_n[2][0]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[2][1]
        path_n = path(pathway,node)
        action_n = action(state_n[2][1],"Left",move)
        state_n[2][0],state_n[2][1] = state_n[2][1],state_n[2][0]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 2
    
    elif node[2][1] == 0:
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[2][0]
        path_n = path(pathway,node)
        action_n = action(state_n[2][0],"Right",move)
        state_n[2][1],state_n[2][0] = state_n[2][0],state_n[2][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[1][1]
        path_n = path(pathway,node)
        action_n = action(state_n[1][1],"Down",move)
        state_n[2][1],state_n[1][1] = state_n[1][1],state_n[2][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        # Third state
        state_n = node.copy()
        cost_n = cost + state_n[2][2]
        path_n = path(pathway,node)
        action_n = action(state_n[2][2],"Left",move)
        state_n[2][1],state_n[2][2] = state_n[2][2],state_n[2][1]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 3
    
    else :
        # First state
        state_n = node.copy()
        cost_n = cost + state_n[2][1]
        path_n = path(pathway,node)
        action_n = action(state_n[2][1],"Right",move)
        state_n[2][2],state_n[2][1] = state_n[2][1],state_n[2][2]
        addtofringe(state_n,cost_n,level,path_n,action_n)
        
        # Second state
        state_n = node.copy()
        cost_n = cost + state_n[1][2]
        path_n = path(pathway,node)
        action_n = action(state_n[1][2],"Down",move)
        state_n[2][2],state_n[1][2] = state_n[1][2],state_n[2][2]
        addtofringe(state_n,cost_n,level,path_n,action_n)

        return 2

# To find the total manhattan distance of a node
def heuristic_value(node):
    h_n = 0
    # itemindex = numpy.where(array == item)
    for n in range(1,9):
        itemindex = np.where(node == n)
        if n == 1:
            h_n += int(abs(itemindex[0]-0) + abs(itemindex[1] - 0))
        elif n == 2:
            h_n += int(abs(itemindex[0]-0) + abs(itemindex[1] - 1))
        elif n == 3:
            h_n += int(abs(itemindex[0]-0) + abs(itemindex[1] - 2))
        elif n == 4:
            h_n += int(abs(itemindex[0]-1) + abs(itemindex[1] - 0))
        elif n == 5:
            h_n += int(abs(itemindex[0]-1) + abs(itemindex[1] - 1))
        elif n == 6:
            h_n += int(abs(itemindex[0]-1) + abs(itemindex[1] - 2))
        elif n == 7:
            h_n += int(abs(itemindex[0]-2) + abs(itemindex[1] - 0))
        elif n == 8:
            h_n += int(abs(itemindex[0]-2) + abs(itemindex[1] - 1))
            
    return h_n

# Function to write all the parameters to the dump file
def writetodumpfile(node,cost,level,pathway,move,successors,fvalue=None):
    if method == "a*":
        with open("dump.txt","a") as file1:
            file1.write("\n Generating successors to < state = {}, action = {}, g(n) = {}, d = {}, f(n) = {}, parent = {} >:".format(node,move,cost,level,fvalue,pathway))
            file1.write("\n{} successors generated".format(successors))
            file1.write("\nClosed: {}".format(closed))
            file1.write("\nFringe:")
            for i in range(len(fringe["states"])):
                file1.write("\n< state = {}, action = {}, g(n) = {}, d = {}, f(n) = {}, parent = {} >".format(fringe["states"][i],fringe["action"][i][-1],fringe["cost"][i],fringe["level"][i],fringe["fvalue"][i],fringe["path"][i][-1]))
    else:
        with open("dump.txt","a") as file1:
            file1.write("\nGenerating successors to < state = {}, action = {}, g(n) = {}, d = {}, parent = {} >:".format(node,move,cost,level,pathway))
            file1.write("\n{} successors generated".format(successors))
            if method == "ids" or method == "dls":
                pass
            else:
                file1.write("\nClosed: {}".format(closed))
            file1.write("\nFringe:")
            for i in range(len(fringe["states"])):
                file1.write("\n< state = {}, action = {}, g(n) = {}, d = {}, parent = {} >".format(fringe["states"][i],fringe["action"][i][-1],fringe["cost"][i],fringe["level"][i],fringe["path"][i][-1]))

# Function to write the goal parameters to the dump file
def writegoaltofile(node,cost,level,pathway,move,fvalue=None):
    if method == "a*":
        with open("dump.txt","a") as file1:
            file1.write("\nGoal Found: < state = {}, action = {}, g(n) = {}, d = {}, f(n) = {}, parent = {} >:".format(node,move,cost,level,fvalue,pathway))
            file1.write("\nNodes Popped: {}".format(nodes_popped))
            file1.write("\nNodes Expanded: {}".format(nodes_expanded))
            file1.write("\nNodes Generated: {}".format(nodes_generated))
            file1.write("\nMax Fringe Size: {}".format(fringe_size)) 
    else:
        with open("dump.txt","a") as file1:
            file1.write("\nGoal Found: < state = {}, action = {}, g(n) = {}, d = {}, parent = {} >:".format(node,move,cost,level,pathway))
            file1.write("\nNodes Popped: {}".format(nodes_popped))
            file1.write("\nNodes Expanded: {}".format(nodes_expanded))
            file1.write("\nNodes Generated: {}".format(nodes_generated))
            file1.write("\nMax Fringe Size: {}".format(fringe_size)) 


# To find the number of arguments passed in the command line
n = len(sys.argv)
if n == 1:
    print("Please pass a valid start file as the 2rd argument of the command\n")
elif n == 2:
    print("Please pass a valid goal file as the 3rd argument of the command\n")
elif n > 5:
    print("Please enter command of the following format : \n")
    print("python filename.py <start-file> <goal-file> <method> <dump-flag> \n")
else :
    # Check for the start file
    if os.path.isfile(sys.argv[1]) == 1:
        start = read(sys.argv[1])

    # Check for the goal file
    if os.path.isfile(sys.argv[2]) == 1:
        goal = read(sys.argv[2])

# Dump Flag
Flag = "false"

arguments = []
for i in range(len(sys.argv)):
    arguments.append(sys.argv[i])

if "true" in arguments:
    Flag = "true"

for argument in arguments:
    if argument in methods:
        method = argument

if Flag == "true":
    file1 = open("dump.txt","w")
    file1.write("Command-Line Arguments: ")
    file1.write(str(arguments[1:]))
    file1.write("\nMethod Selected: {}".format(method))
    file1.write("\nRunning {}".format(method))
    file1.close()

i = 0
# Fringe Declaration
fringe = {"states" : [],
          "cost" : [],
          "level" : [],
          "path" : [],
          "action" : [],
          "heuristic" : [],
          "fvalue" : []}
closed = []
node = start.copy()
fringe["states"].append(node)
fringe["cost"].append(0)
fringe["level"].append(0)
pathway = []
pathway.append(None)
fringe["path"].append(pathway)
move = []
move.append(None)
fringe["action"].append(move)
fringe["heuristic"].append(heuristic_value(node))
fringe["fvalue"].append(fringe["cost"][0]+fringe["heuristic"][0])
nodes_popped = 0
nodes_expanded = 0
nodes_generated = 1
fringe_size = len(fringe["states"])

# Methods Defination
# Breadth First Search
if method == 'bfs':
    while fringe["states"]:
        node = fringe["states"].pop(0)
        cost = fringe["cost"].pop(0)
        level = fringe["level"].pop(0)
        pathway = fringe["path"].pop(0)
        move = fringe["action"].pop(0)
        nodes_popped+=1
        if (node == goal).all():
            print("Nodes Popped: ",nodes_popped)
            print("Nodes Expanded: ",nodes_expanded)
            print("Nodes Generated: ",nodes_generated)
            print("Max Fringe Size: ",fringe_size)
            print("Nodes enclosed :",len(closed))
            print("Goal reached at depth {} at a cost of {}.".format(level,cost))
            print("Steps :")
            for step in move[1:]:
                print(step)
            writegoaltofile(node,cost,level,pathway[-1],move[-1])
            break
        else:
            if any((node == x).all() for x in closed):
                pass
            else:
                successors = expand_all_possible_nodes(node,cost,level,method,pathway,move)
                nodes_generated += successors
                closed.append(node)
                if Flag == "true":
                    writetodumpfile(node,cost,level,pathway[-1],move[-1],successors)
                nodes_expanded+=1
                if len(fringe["states"]) > fringe_size:
                    fringe_size = len(fringe["states"])

# Depth First Search
if method == 'dfs':
    while fringe["states"]:
        node = fringe["states"].pop()
        cost = fringe["cost"].pop()
        level = fringe["level"].pop()
        pathway = fringe["path"].pop()
        move = fringe["action"].pop()
        nodes_popped+=1
        if (node == goal).all():
            print("Nodes Popped: ",nodes_popped)
            print("Nodes Expanded: ",nodes_expanded)
            print("Nodes Generated: ",nodes_generated)
            print("Max Fringe Size: ",fringe_size)
            print("Goal reached at depth {} at a cost of {}.".format(level,cost))
            print("Steps :")
            for step in move[1:]:
                print(step)
            writegoaltofile(node,cost,level,pathway[-1],move[-1])
            break
        else:
            if any((node == x).all() for x in closed):
                pass
            else:
                successors = expand_all_possible_nodes(node,cost,level,method,pathway,move)
                nodes_generated += successors
                closed.append(node)                
                if Flag == "true":
                    writetodumpfile(node,cost,level,pathway[-1],move[-1],successors)
                nodes_expanded+=1
                if len(fringe["states"]) > fringe_size:
                    fringe_size = len(fringe["states"])

# Uniformed Cost Search
if method == 'ucs':
    while fringe["states"]:
        value = fringe["cost"][0]
        lowest_cost = 0
        for x in range (len(fringe["cost"])):
            if value > fringe["cost"][x]:
                value = fringe["cost"][x]
                lowest_cost = x
        node = fringe["states"].pop(lowest_cost)
        cost = fringe["cost"].pop(lowest_cost)
        level = fringe["level"].pop(lowest_cost)
        pathway = fringe["path"].pop(lowest_cost)
        move = fringe["action"].pop(lowest_cost)
        nodes_popped+=1
        if (node == goal).all():
            print("Nodes Popped: ",nodes_popped)
            print("Nodes Expanded: ",nodes_expanded)
            print("Nodes Generated: ",nodes_generated)
            print("Max Fringe Size: ",fringe_size)
            print("Goal reached at depth {} at a cost of {}.".format(level,cost))
            print("Steps :")
            for step in move[1:]:
                print(step)
            writegoaltofile(node,cost,level,pathway[-1],move[-1])
            break
        else:
            if any((node == x).all() for x in closed):
                pass
            else:
                successors = expand_all_possible_nodes(node,cost,level,method,pathway,move)
                nodes_generated += successors
                closed.append(node)
                if Flag == "true":
                    writetodumpfile(node,cost,level,pathway[-1],move[-1],successors)
                nodes_expanded+=1
                if len(fringe["states"]) > fringe_size:
                    fringe_size = len(fringe["states"])

# Depth Limit Search
if method == 'dls':
    limit = int(input("Enter the depth limit: "))
    while fringe["states"]:
        node = fringe["states"].pop()
        cost = fringe["cost"].pop()
        level = fringe["level"].pop()
        pathway = fringe["path"].pop()
        move = fringe["action"].pop()
        nodes_popped+=1
        if (node == goal).all():
            print("Nodes Popped: ",nodes_popped)
            print("Nodes Expanded: ",nodes_expanded)
            print("Nodes Generated: ",nodes_generated)
            print("Max Fringe Size: ",fringe_size)
            print("Goal reached at depth {} at a cost of {}.".format(level,cost))
            print("Steps :")
            for step in move[1:]:
                print(step)
            writegoaltofile(node,cost,level,pathway[-1],move[-1])
            break
        else:
            if level >= limit:
                continue
            successors = expand_all_possible_nodes(node,cost,level,method,pathway,move)               
            nodes_generated += successors
            if Flag == "true":
                    writetodumpfile(node,cost,level,pathway[-1],move[-1],successors)
            nodes_expanded+=1
            if len(fringe["states"]) > fringe_size:
                fringe_size = len(fringe["states"])

# Iterative Deepening Search
if method == 'ids':
    limit = 0
    while not (node == goal).all():
        fringe = {"states" : [],
          "cost" : [],
          "level" : [],
          "path" : [],
          "action" : [],
          "heuristic" : [],
          "fvalue" : []}
        fringe["states"].append(start)
        fringe["cost"].append(0)
        fringe["level"].append(0)
        pathway = []
        pathway.append(None)
        fringe["path"].append(pathway)
        move = []
        move.append(None)
        fringe["action"].append(move)
        while fringe["states"]:
            node = fringe["states"].pop()
            cost = fringe["cost"].pop()
            level = fringe["level"].pop()
            pathway = fringe["path"].pop()
            move = fringe["action"].pop()
            nodes_popped+=1
            if (node == goal).all():
                print("Nodes Popped: ",nodes_popped)
                print("Nodes Expanded: ",nodes_expanded)
                print("Nodes Generated: ",nodes_generated)
                print("Max Fringe Size: ",fringe_size)
                print("Goal reached at depth {} at a cost of {}.".format(level,cost))
                print("Steps :")
                for step in move[1:]:
                    print(step)
                writegoaltofile(node,cost,level,pathway[-1],move[-1])
                break
            else:
                if level >= limit:
                    continue
                successors = expand_all_possible_nodes(node,cost,level,method,pathway,move)               
                nodes_generated += successors
                if Flag == "true":
                    writetodumpfile(node,cost,level,pathway[-1],move[-1],successors)
                nodes_expanded+=1
                if len(fringe["states"]) > fringe_size:
                    fringe_size = len(fringe["states"])
        limit +=1

# Greedy Search
if method == "greedy":
    while fringe["states"]:
        heuristic = fringe["heuristic"][0]
        lowest_heuristic = 0
        for x in range (len(fringe["heuristic"])):
            if heuristic > fringe["heuristic"][x]:
                heuristic = fringe["heuristic"][x]
                lowest_heuristic = x
        node = fringe["states"].pop(lowest_heuristic)
        cost = fringe["cost"].pop(lowest_heuristic)
        level = fringe["level"].pop(lowest_heuristic)
        pathway = fringe["path"].pop(lowest_heuristic)
        move = fringe["action"].pop(lowest_heuristic)
        heuristic = fringe["heuristic"].pop(lowest_heuristic)
        nodes_popped+=1
        if (node == goal).all():
            print("Nodes Popped: ",nodes_popped)
            print("Nodes Expanded: ",nodes_expanded)
            print("Nodes Generated: ",nodes_generated)
            print("Max Fringe Size: ",fringe_size)
            print("Goal reached at depth {} at a cost of {}.".format(level,cost))
            print("Steps :")
            for step in move[1:]:
                print(step)
            writegoaltofile(node,cost,level,pathway[-1],move[-1])
            break
        else:
            if any((node == x).all() for x in closed):
                pass
            else:
                successors = expand_all_possible_nodes(node,cost,level,method,pathway,move)
                nodes_generated += successors
                closed.append(node)
                if Flag == "true":
                    writetodumpfile(node,cost,level,pathway[-1],move[-1],successors)
                nodes_expanded+=1
                if len(fringe["states"]) > fringe_size:
                    fringe_size = len(fringe["states"])

# A* Search
if method == "a*":
    while fringe["states"]:
        fvalue = fringe["fvalue"][0]
        lowest_fvalue = 0
        for x in range (len(fringe["fvalue"])):
            if fvalue > fringe["fvalue"][x]:
                fvalue = fringe["fvalue"][x]
                lowest_fvalue = x
        node = fringe["states"].pop(lowest_fvalue)
        cost = fringe["cost"].pop(lowest_fvalue)
        level = fringe["level"].pop(lowest_fvalue)
        pathway = fringe["path"].pop(lowest_fvalue)
        move = fringe["action"].pop(lowest_fvalue)
        heuristic = fringe["heuristic"].pop(lowest_fvalue)
        fvalue = fringe["fvalue"].pop(lowest_fvalue)
        nodes_popped+=1
        if (node == goal).all():
            print("Nodes Popped: ",nodes_popped)
            print("Nodes Expanded: ",nodes_expanded)
            print("Nodes Generated: ",nodes_generated)
            print("Max Fringe Size: ",fringe_size)
            print("Goal reached at depth {} at a cost of {}.".format(level,cost))
            print("Steps :")
            for step in move[1:]:
                print(step)
            writegoaltofile(node,cost,level,pathway[-1],move[-1],fvalue)
            break
        else:
            if any((node == x).all() for x in closed):
                pass
            else:
                successors = expand_all_possible_nodes(node,cost,level,method,pathway,move)
                nodes_generated += successors
                closed.append(node)
                if Flag == "true":
                    writetodumpfile(node,cost,level,pathway[-1],move[-1],fvalue,successors)
                nodes_expanded+=1
                if len(fringe["states"]) > fringe_size:
                    fringe_size = len(fringe["states"])

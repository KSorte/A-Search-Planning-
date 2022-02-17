#!/usr/bin/env python
# coding: utf-8

# In[1]:


# EXTRACTING THE NODES AND EDGES INFORMATION FROM THE FILES 
# The number of nodes extracted will determine the length of all the lists used in this code
import csv
import numpy as np 
from numpy import ndarray 
# Extracting Nodes 
nodes_file = open('D:/ROBOTICS/V-REP_scenes/Scene5_example/results/nodes.csv')
nodereader = csv.reader(nodes_file) # This variable will allow to read the csv file and extract information
node_header = [] 
node_header = next(nodereader)
#print(node_header)
nodes = []        # List for storing nodes information
for node in nodereader:
    node[0] = int(node[0])    # Converting node indices to integars
    for i in range(1,len(node)):
# Using len(node) to make the code more generalized, since a node row can be of any size depending on the dimensions of  configuration
        node[i] = float(node[i])        # Converting the coordinates and heuristic values to float
    nodes.append(node)                  # Adding the converted values to the list of nodes
#print(nodes)
opt_cost = []   # List for optimistic cost to go to the goal from the node
for node in nodes:
    opt_cost.append(node[len(node)-1])
#print(opt_cost)
    

# Extracting Edges 
edges_file = open('D:/ROBOTICS/V-REP_scenes/Scene5_example/results/edges.csv')
edgereader = csv.reader(edges_file)

edge_header = []   
edge_header = next(edgereader)
edges = []              # List for storing edges information  
for edge in edgereader:
    for i in range(0,len(edge)-1):
        edge[i] = int(edge[i])          # Converting the extracting values to float
    edge[len(edge)-1] = float(edge[len(edge)-1])       # Converting the edge length to float
    edges.append(edge)                  # Adding the converted float value to the list of edges
        
#print(edges)

start_node = nodes[0][0]
goal_node = nodes[len(nodes)-1][0]



# In[2]:


# CREATING A DICTIONARY TO STORE NEIGHBOUR INFORMATION OF EACH NODE
# Keys would be node IDs and the associated value would be a list of neighbours for that node

# Dictionary 
nbr = {neighbour_list: [] for neighbour_list in range(1,len(nodes))}

i=1 
while i < len(nodes):
    for edge in edges:
        if i == edge[1]:
            nbr[i].append(edge[0])
            
    i+=1
            
print('Neighbour information for each node:\n')
print(nbr)   
        
# OPEN AND CLOSE LISTS
OPEN = []            # Would contain the node ID and the estimated total cost of the node
CLOSED = []
past_cost = []
est_total_cost = [0]*len(nodes) 
parent_node = [0]*len(nodes)      # Setting all parent nodes to zero 
# Optimistic cost to go list created while extracting nodes.


# In[3]:


past_cost.append(0)
for j in range(0,len(nodes)-1):
    past_cost.append(float('inf'))
OPEN.append([1,opt_cost[0]])


# In[4]:


# A* Search Begins 
path = []              # Path returned by the algorithm
SUCCESS = 0;           # Will become 1 if the path is returned
while len(OPEN) > 0:
    current = OPEN[0][0]
    print('Current =  :',current)
    OPEN.remove(OPEN[0])
    #print(OPEN)
    CLOSED.append(current)
    if current == goal_node:
        path_node = current
        # Constructing the path by back tracking parent of current node
        for i in range(0,len(nodes)):
            path.append(path_node)
            if path_node == start_node:
                break                  # Stop the backtracking when the path is constructed
            path_node = parent_node[path_node-1]
        path.sort()       # Path of the nodes sorted from the start node to the goal node in ascending order    
        print("Search successful")
        print("The path is : ",path) 
        SUCCESS = 1
    if SUCCESS == 1:
        break    
    for neighbour in nbr[current]:
        if neighbour not in CLOSED:
            # Getting the path cost from current-> neighbour from the edges list
            print("Current is {}, neighbour is {}".format(current, neighbour))
            for edge in edges:
                
                if (current in edge) and (neighbour in edge):
                    
                
                    cost_to_nbr = edge[len(edge)-1]             # Cost from current to neighbour node found            
                    tent_past_cost = past_cost[current-1] + cost_to_nbr
                
                # If tentative past cost is less than the past cost, than the neighbour's past cost updated
            
            if tent_past_cost < past_cost[neighbour -1]:
                past_cost[neighbour -1] = tent_past_cost 
                
                parent_node[neighbour -1] = current
                
                est_total_cost[neighbour -1] = past_cost[neighbour -1] + opt_cost[neighbour -1]
    
                # Sorting OPEN according to the estimated total cost
                # In the beginning, whrn OPEN is empty, the case needs to be handled differently
                if len(OPEN) == 0:
                    OPEN.append([neighbour,est_total_cost[neighbour -1]])   # Adding the neighbour node to OPEN at the last place
                    print("OPEN list :\n")
                    print(OPEN)
                else:    # When OPEN is not empty, a new node is added according to its estimated total cost
                    for node in OPEN: 
                        if node[1]> est_total_cost[int(neighbour -1)]:            # Comparing estimated total cost of OPEN elements 
                            OPEN.insert(OPEN.index(node),[neighbour, est_total_cost[neighbour -1]])      # New node added to OPEN at sorted place   
                            print("OPEN list :\n")
                            print(OPEN)
                            break 
if SUCCESS == 0:
    print("Path not found")


# In[11]:


# WRITING THE PATH TO A CSV FILE
path = np.array(path)       # Converting path list to array for convenience
path.tofile("D:/ROBOTICS/V-REP_scenes/Scene5_example/results/path.csv", sep = ',')


# In[ ]:





# In[ ]:





# A-Search-Planning-
This Python code executes the A* Search algorithm on the sample data provided by the Coursera course Modern Robotics :  Robot Motion Planning and Control.

- Nodes and Edges information is imported to the code from csv files and converted to lists.
- In the nodes file : 1st column - Node ID; 2nd, 3rd column - x,y coordinates : 4th Column -  Heuristic Cost to go
- In the edges fle : 1st,2nd column - Node IDs; 3rd Column - Edge length 
- Then a Dictionary is created with the keys being node IDs and values being a list of the neighbours for that node.
- OPEN, CLOSED list defined. heuristic cost to go from the node to the goal information taken from the nodes list. 
- Lsits to store past cost to a node, estimated total cost, parent node information are intialized
- The length of the above lists are determined by the number of nodes in the .csv file provided
- Then the algorithm is implememted and the OPEN, CLOSED, past cost to a node, estimated total cost, parent node information are appropriately updated.
- At the end when the goal node is reached, the path is constructed by backtracking the parent nodes from the parent nodes list generated.
- The path is outputted to a csv file and fed to a Coppelia Sim Scene provided by the course. 
- The screenshot shows the location of the nodes(blue), edges(yellow), obstacles(gray) and the optimal path(green) found by the algorithm.
- The below text is the output on the console to track the changes in the OPEN list and the nodes considered. "current" is the node whose neighbours are currently explored.

Current =  : 1
Current is 1, neighbour is 3
Heuristic is : 1.1244
OPEN list :

[[3, 1.4147]]
Current is 1, neighbour is 2
Heuristic is : 1.0762
Length of the OPEN list is : 2
Current =  : 3
Current is 3, neighbour is 4
Heuristic is : 0.8494
OPEN list :

[[4, 1.4914], [2, 1.4982]]
Current is 3, neighbour is 2
Length of the OPEN list is : 2
Current =  : 4
Current is 4, neighbour is 8
Heuristic is : 0.5014
Current is 4, neighbour is 2
Current is 4, neighbour is 5
Heuristic is : 0.7604
OPEN list :

[[2, 1.4982], [5, 1.5124], [8, 1.6233999999999997]]
Length of the OPEN list is : 3
Current =  : 2
Current is 2, neighbour is 5
Heuristic is : 0.7604
OPEN list :

[[5, 1.3614], [5, 1.5124], [8, 1.6233999999999997]]
Length of the OPEN list is : 3
Current =  : 5
Current is 5, neighbour is 9
Heuristic is : 0.6134
Current is 5, neighbour is 7
Heuristic is : 0.5719
OPEN list :

[[5, 1.5124], [7, 1.6130999999999998], [8, 1.6233999999999997], [9, 1.8138]]
Length of the OPEN list is : 4
Current =  : 5
Current is 5, neighbour is 9
Current is 5, neighbour is 7
Length of the OPEN list is : 3
Current =  : 7
Current is 7, neighbour is 10
Heuristic is : 0.3135
OPEN list :

[[10, 1.6132999999999997], [8, 1.6233999999999997], [9, 1.8138]]
Length of the OPEN list is : 3
Current =  : 10
Current is 10, neighbour is 12
Heuristic is : 0.0
OPEN list :

[[12, 1.6132999999999997], [8, 1.6233999999999997], [9, 1.8138]]
Current is 10, neighbour is 11
Heuristic is : 0.214
OPEN list :

[[12, 1.6132999999999997], [8, 1.6233999999999997], [11, 1.6915999999999998], [9, 1.8138]]
Length of the OPEN list is : 4
Current =  : 12
The path is :  [1, 2, 5, 7, 10, 12]

This Python code executes the A* Search algorithm on the sample data provided by the Coursera course Modern Robotics :  Robot Motion Planning and Control.

- Nodes and Edges information is imported to the code from csv files and converted to lists.
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
OPEN list :

[[3, 1.4147]]
Current is 1, neighbour is 2
Current =  : 3
Current is 3, neighbour is 4
OPEN list :

[[4, 1.4914]]
Current =  : 4
Current is 4, neighbour is 8
OPEN list :

[[8, 1.6233999999999997]]
Current is 4, neighbour is 5
OPEN list :

[[5, 1.5124], [8, 1.6233999999999997]]
Current =  : 5
Current is 5, neighbour is 9
Current is 5, neighbour is 7
Current =  : 8
Current is 8, neighbour is 12
OPEN list :

[[12, 1.6233999999999997]]
Current is 8, neighbour is 9
Current =  : 12
Search successful
The path is :  [1, 3, 4, 8, 12] 
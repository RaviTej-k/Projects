Program Statement : Your task is to build an agent to solve a modifed version of the 8 puzzle problem (called the Expense 8 puzzle problem). The task is still to take a 3X3 grid on which 8 tiles have been placed, where you can only move one tile at a time to an adjacent location (as long as it is blank) and figure out the order in which to move the tiles to get it to a desired configuration. However now the number on the tile now also represents the cot of moving that tile (moving the tile marked 6 costs 6).
<start-file> and <goal-file> are required.
 <method> can be
bfs - Breadth First Search
ucs - Uniform Cost Search
dfs - Depth First Search [Note: This part is EC for CSE 4308 students]
dls - Depth Limited Search (Note: Depth Limit will be obtained as a Console Input) [Note: This part is EC for CSE 4308 students]
ids - Iterative Deepening Search [Note: This part is EC for CSE 4308 students]
greedy - Greedy Seach
a* - A* Search (Note: if no <method> is given, this should be the default option)
If <dump-flag>  is given as true, search trace is dumped for analysis in trace-<date>-<time>.txt (Note: if <dump-flag> is not given, assume it is false)
search trace contains: fringe and closed set contents per loop of search(and per iteration for IDS), counts of nodes expanded and nodes

Programming language : Python
Version : 3.11.9

Code Structure:
Line 10
Read()  -- to read the start and goal file
Line 32
Addtofringe() -- to add details of path, action and other parameters as operations are performed
Line 50
Expandallpossiblenodes() -- to expand the tree and select action to perform
Line 296
writetofile() -- write details to parameters
Line 401
Methods for diffrents approaches to solve 8_puzzle problem

Command Line instruction:
python <file-name> <start-file> <goal-file> <method> <dump-flag>

example command:
python AI_Assignment1.py start.txt goal.txt bsf

Please make sure start and goal file are in same directory



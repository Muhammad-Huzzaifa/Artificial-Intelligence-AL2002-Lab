from Task4 import DLS

def IDS(start_state, goal_state):
    ''' Iterative deepening search algorithm.
    
    Args:
        start_state: The initial state of the search.
        goal_state: The goal state of the search.
        
    Returns:
        A tuple containing the solution path, the number of nodes expanded, and the total number of nodes expanded.
    '''
    
    depth = 0
    totalnodes = 0 

    while True:
        solution_path, numnodes = DLS(start_state, goal_state, depth)
        totalnodes += numnodes

        if solution_path:
            return solution_path, numnodes, totalnodes
            
        depth += 1
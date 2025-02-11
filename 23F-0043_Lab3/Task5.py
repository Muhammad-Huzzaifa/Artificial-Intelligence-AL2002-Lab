from Task4 import DLS

def IDS(start_state, goal_state):
    depth = 0
    totalnodes = 0 

    while True:
        solution_path, numnodes = DLS(start_state, goal_state, depth)
        totalnodes += numnodes

        if solution_path:
            return solution_path, numnodes, totalnodes
            
        depth += 1
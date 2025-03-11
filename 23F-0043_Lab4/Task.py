import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections import namedtuple
from provided.utils import PriorityQueue, solution

def GBFS(start_state, goal_state, heuristic):
    ''' Greedy Best First Search
    
    Args:
        start_state: The initial state of the search
        goal_state: The state to reach
        heuristic: The heuristic function to use
        
    Returns:
        A tuple containing the solution path and the number of nodes expanded
    '''
    
    Node = namedtuple('Node', ['state', 'parent', 'action'])
    node = Node(start_state, None, None)

    if node.state == goal_state:
        return solution(node), 0
    
    frontier = PriorityQueue()
    reached = set()

    frontier.push(node, heuristic(node.state, goal_state))
    reached.add(node.state)
    numnodes = 0

    while not frontier.is_empty():
        node = frontier.pop()
        
        for next_state, next_action, _ in node.state.successors():
            numnodes += 1

            if next_state == goal_state:
                return solution(Node(next_state, node, next_action)), numnodes
            
            if next_state not in reached:
                frontier.push(Node(next_state, node, next_action), heuristic(next_state, goal_state))
                reached.add(next_state)

    return None, numnodes
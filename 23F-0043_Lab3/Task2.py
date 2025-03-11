import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections import namedtuple
from provided.utils import PriorityQueue, solution

def UCS(start_state, goal_state):
    ''' Uniform Cost Search

    Args:
        start_state: The initial state of the search
        goal_state: The state to reach

    Returns:
        A tuple containing the solution path and the number of nodes expanded
    '''
    
    Node = namedtuple('Node', ['state', 'parent', 'action', 'cost'])
    node = Node(start_state, None, None, 0)
    
    frontier = PriorityQueue()
    expanded = set()
    
    frontier.push(node, node.cost)
    numnodes = 0
    
    while not frontier.is_empty():
        node = frontier.pop()
        
        if node.state in expanded:
             continue
        
        expanded.add(node.state)

        if node.state == goal_state:
                return solution(node), numnodes
        
        for next_state, next_action, next_cost in node.state.successors():
            numnodes += 1
        
            if next_state not in expanded:
                frontier.push(Node(next_state, node, next_action, node.cost + next_cost), node.cost + next_cost)
                
    return None, numnodes
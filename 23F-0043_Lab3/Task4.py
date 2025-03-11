import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections import namedtuple
from provided.utils import Stack, solution

def DLS(start_state, goal_state, limit):
    ''' Depth-limited search algorithm.

    Args:
        start_state: The initial state of the search.
        goal_state: The goal state of the search.
        limit: The maximum depth to search.

    Returns:
        A tuple containing the solution path and the number of nodes expanded.
    '''
    
    Node = namedtuple('Node', ['state', 'parent', 'action', 'depth'])
    node = Node(start_state, None, None, 0)
    
    if node.state == goal_state:
        return solution(node), 0
    
    frontier = Stack()
    reached = set()
    
    frontier.push(node)
    reached.add(node.state)
    numnodes = 0
    
    while not frontier.is_empty():
        node = frontier.pop()
        
        if node.depth < limit:
            for next_state, next_action, _ in node.state.successors():
                numnodes += 1

                if next_state == goal_state:
                    return solution(Node(next_state, node, next_action, node.depth + 1)), numnodes

                if next_state not in reached:
                    frontier.push(Node(next_state, node, next_action,  node.depth + 1))
                    reached.add(next_state)
                
    return None, numnodes
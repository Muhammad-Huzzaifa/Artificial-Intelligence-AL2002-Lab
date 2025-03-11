import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections import namedtuple
from provided.utils import Stack, solution

def DFS(start_state, goal_state):
    ''' Depth-first search algorithm.

    Args:
        start_state: The initial state of the search.
        goal_state: The goal state of the search.

    Returns:
        A tuple containing the solution path and the number of nodes expanded.
    '''
    
    Node = namedtuple('Node', ['state', 'parent', 'action'])
    node = Node(start_state, None, None)
    
    if node.state == goal_state:
        return solution(node), 0
    
    frontier = Stack()
    reached = set()
    
    frontier.push(node)
    reached.add(node.state)
    numnodes = 0
    
    while not frontier.is_empty():
        node = frontier.pop()
        
        for next_state, next_action, _ in node.state.successors():
            numnodes += 1
            
            if next_state == goal_state:
                return solution(Node(next_state, node, next_action)), numnodes
        
            if next_state not in reached:
                frontier.push(Node(next_state, node, next_action))
                reached.add(next_state)
                
    return None, numnodes
from collections import namedtuple
from provided.utils import Stack, solution

def DFS(start_state, goal_state):
    Node = namedtuple('Node', ['state', 'parent', 'action', 'cost'])
    node = Node(start_state, None, None, 0)
    
    if node.state == goal_state:
        return solution(node), 0
    
    frontier = Stack()
    reached = set()
    
    frontier.push(Node(start_state, None, None, 0))
    reached.add(start_state)
    numnodes = 0
    
    while not frontier.is_empty():
        node = frontier.pop()
        
        for next_state, next_action, next_cost in node.state.successors():
            numnodes += 1
            
            if next_state == goal_state:
                return solution(Node(next_state, node, next_action, node.cost + next_cost)), numnodes
        
            if next_state not in reached:
                frontier.push(Node(next_state, node, next_action, node.cost + next_cost))
                reached.add(next_state)
                
    return None, numnodes
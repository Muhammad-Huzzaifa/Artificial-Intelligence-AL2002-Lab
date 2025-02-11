from collections import namedtuple
from provided.utils import Stack, solution

def DLS(start_state, goal_state, limit=30):
    Node = namedtuple('Node', ['state', 'parent', 'action', 'cost', 'depth'])
    node = Node(start_state, None, None, 0, 0)
    
    if node.state == goal_state:
        return solution(node), 0
    
    frontier = Stack()
    reached = set()
    
    frontier.push(Node(start_state, None, None, 0, 0))
    reached.add(start_state)
    numnodes = 0
    
    while not frontier.is_empty():
        node = frontier.pop()
        
        if node.depth < limit:
            for next_state, next_action, next_cost in node.state.successors():
                numnodes += 1

                if next_state == goal_state:
                    return solution(Node(next_state, node, next_action, node.cost + next_cost, node.depth + 1)), numnodes

                if next_state not in reached:
                    frontier.push(Node(next_state, node, next_action, node.cost + next_cost, node.depth + 1))
                    reached.add(next_state)
                
    return None, numnodes
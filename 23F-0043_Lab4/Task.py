from collections import namedtuple
from provided.utils import PriorityQueue, solution

def GBFS(start_state, goal_state, heuristic):
    Node = namedtuple('Node', ['state', 'parent', 'action'])
    node = Node(start_state, None, None)

    frontier = PriorityQueue()
    reached = set()

    frontier.push(node, heuristic(node.state, goal_state))
    reached.add(node.state)
    numnodes = 0

    while not frontier.is_empty():
        node = frontier.pop()

        if node.state == goal_state:
            return solution(node), numnodes
        
        for next_state, next_action, _ in node.state.successors():
            numnodes += 1
        
            if next_state not in reached:
                frontier.push(Node(next_state, node, next_action), heuristic(next_state, goal_state))
                reached.add(next_state)

    return None, numnodes
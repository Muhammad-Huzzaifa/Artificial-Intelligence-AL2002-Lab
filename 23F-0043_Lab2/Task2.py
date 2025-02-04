class WatrerJugProblemAgent:
    '''
    Famous water jug problem is a problem where we have two jugs of water, one of 4L and another of 3L. The goal is to measure 2L of water using these two jugs. And we have to build AI agent that can perform this task using BFS and DFS.
    
    Problem Formulation:
        1. Initial State: Two jug of water, 4L and 3L each with 0L water
        2. Goal State: 2L in 4L jug and any amount of water in 3L jug
        3. Actions: Fill, Drop, Transfer
        4. Transition Model:
            - Fill: (x, y) -> (4, y) or (x, 3)
            - Drop: (x, y) -> (0, y) or (x, 0)
            - Transform: (x, y) -> (x+y, 0) or (0, x+y) if x+y <= 4 and 3 respectively
            - Transform: (x, y) -> (4, y-(4-x)) or (x-(3-y), 3) if x+y > 4 and 3 respectively
        5. Path Cost: 1 for each operation
    
    Actions Sequence:
        1. Fill 4L Jug
        2. Fill 3L Jug
        3. Drop 4L Jug
        4. Drop 3L Jug
        5. Transform water from 4L Jug to 3L Jug
        6. Transform water from 3L Jug to 4L Jug
    '''

    def __init__(self):
        self.jugs = {
            '4l': 0,
            '3l': 0
        }
        self.states = [(self.jugs['4l'], self.jugs['3l'])]


    def reset(self):
        self.jugs = {
            '4l': 0,
            '3l': 0
        }
        self.states = [(self.jugs['4l'], self.jugs['3l'])]


    def fill4l(self):
        x, y = self.jugs['4l'], self.jugs['3l']

        if x == 4:
            return (x, y), False
        
        return (4, y), True
        

    def fill3l(self):
        x, y = self.jugs['4l'], self.jugs['3l']

        if y == 3:
            return (x, y), False
        
        return (x, 3), True


    def drop4l(self):
        x, y = self.jugs['4l'], self.jugs['3l']

        if x == 0:
            return (x, y), False
        
        return (0, y), True


    def drop3l(self):
        x, y = self.jugs['4l'], self.jugs['3l']

        if y == 0:
            return (x, y), False
        
        return (x, 0), True


    def transform4lto3l(self):
        x, y = self.jugs['4l'], self.jugs['3l']

        if x == 0 or y == 3:
            return (x, y), False
        
        if 0 < x+y <= 3:
            return (0, x+y), True
        else:
            return (x-(3-y), 3), True
        

    def transform3lto4l(self):
        x, y = self.jugs['4l'], self.jugs['3l']
        if x == 4 or y == 0:
            return (x, y), False
        
        if 0 < x+y <= 4:
            return (x+y, 0), True
        else:
            return (4, y-(4-x)), True


    def bfs_search(self):
        actionFunctions = [self.fill4l, self.fill3l, self.drop4l, self.drop3l, self.transform4lto3l, self.transform3lto4l]
        actionNames = ['f4', 'f3', 'd4', 'd3', 't43', 't34']
        actionDescriptions = {
            'init': 'Initial state...',
            'f4': 'Filling 4L Jug from tap...',
            'f3': 'Filling 3L Jug from tap...',
            'd4': 'Dropping 4L Jug into ground...',
            'd3': 'Dropping 3L Jug into ground...',
            't43': 'Transforming water from 4L Jug to 3L Jug...',
            't34': 'Transforming water from 3L Jug to 4L Jug...'
        }
        actionsList = ['init']

        parents = [None]
        visited = {(self.jugs['4l'], self.jugs['3l'])}
        index = 0

        while self.jugs['4l'] != 2:
            current_state = self.states[index]
            parent = parents[index]
            currstate_name = actionsList[index]
            index += 1

            print(actionDescriptions[currstate_name])
            print(f' >>Current State: (4L:{current_state[0]}, 3L:{current_state[1]}), Parent State: {parent}\n')

            for i, action in enumerate(actionFunctions):
                newstate, ispossible = action()
                if ispossible and newstate not in visited:
                    self.states.append(newstate)
                    actionsList.append(actionNames[i])
                    parents.append(current_state)
                    visited.add(newstate)
            
            self.jugs['4l'], self.jugs['3l'] = self.states[index]
        
        print(actionDescriptions[actionsList[index]])
        print(f'>>>Goal State: (4L:{self.states[index][0]}, 3L:{self.states[index][1]}), Parent State: {parents[index]}\n\n')


    def dfs_search(self):
        actionFunctions = [self.fill4l, self.fill3l, self.drop4l, self.drop3l, self.transform4lto3l, self.transform3lto4l]
        actionNames = ['f4', 'f3', 'd4', 'd3', 't43', 't34']
        actionDescriptions = {
            'init': 'Initial state...',
            'f4': 'Filling 4L Jug from tap...',
            'f3': 'Filling 3L Jug from tap...',
            'd4': 'Dropping 4L Jug into ground...',
            'd3': 'Dropping 3L Jug into ground...',
            't43': 'Transforming water from 4L Jug to 3L Jug...',
            't34': 'Transforming water from 3L Jug to 4L Jug...'
        }
        actionsList = ['init']

        parents = [None]
        visited = {(self.jugs['4l'], self.jugs['3l'])}

        while self.jugs['4l'] != 2:
            current_state = self.states[0]
            parent = parents[0]
            currstate_name = actionsList[0]

            print(actionDescriptions[currstate_name])
            print(f' >>Current State: (4L:{current_state[0]}, 3L:{current_state[1]}), Parent State: {parent}\n')

            for i, action in enumerate(actionFunctions):
                newstate, ispossible = action()
                if ispossible and newstate not in visited:
                    self.states.insert(0, newstate)
                    actionsList.insert(0, actionNames[i])
                    parents.insert(0, current_state)
                    visited.add(newstate)
            
            self.jugs['4l'], self.jugs['3l'] = self.states[0]
        
        print(actionDescriptions[actionsList[0]])
        print(f'>>>Goal State: (4L:{self.states[0][0]}, 3L:{self.states[0][1]}), Parent State: {parents[0]}\n\n')


def main():
    agent = WatrerJugProblemAgent()

    print('Through BFS Search:')
    agent.bfs_search()

    agent.reset()

    print('Through DFS Search:')
    agent.dfs_search()

if __name__=='__main__':
    main()
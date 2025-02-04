class VacumeCleanerAgent:
    '''
    There are two locations A and B, and both have two conditions (Dirty or Clean). The agent's goal is to check and clean both locations.

    Problem formulation:
        1. Initial State: Both locations are dirty
        2. Goal State: Both locations are clean 
        3. Actions: Suck, Move Right, Move Left
        4. Transition Model: 
            - Suck: (A, B) -> (Clean, B) or (A, Clean)
            - Move Left: (A, B) -> (A, B)
            - Move Right: (A, B) -> (A, B)
        5. Path Cost: 1 for each operation
    '''

    def __init__(self, location):
        self.location = location
        self.environment = {
            'A': 'Dirty',
            'B': 'Dirty'
        }
        self.allchecked = False
    

    def perceive(self):
        return (self.location, self.environment)
    

    def act(self):
        if self.environment[self.location] == 'Dirty':
            print(f'Location {self.location} is dirty. Sucking dirt...')
            self.environment[self.location] = 'Clean'

        elif self.location == 'A':
            print(f'Location {self.location} is clean. Moving right towards B...')
            self.location = 'B'
            self.allchecked = True

        elif self.location == 'B':
            print(f'Location {self.location} is clean. Moving left towards A...')
            self.location = 'A'
            self.allchecked = True


    def run(self):
        print(f'Initial state: {self.perceive()}')

        while not self.allchecked or 'Dirty' in self.environment.values():
            self.act()
            print(f'Current state: {self.perceive()}')


def main():
    agent = VacumeCleanerAgent('B')
    agent.run()

if __name__=='__main__':
    main()
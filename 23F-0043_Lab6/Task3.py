import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt

class LocalBeamSearch:
    ''' Local Beam Search Algorithm
    '''


    def __init__(self, k):
        ''' Constructor for LocalBeamSearch class

        Args:
            k: The number of states to keep
        '''

        self.k = k
        self.history = []


    def search(self, states, maxiterations = 100):
        ''' Search for a solution using Local Beam Search

        Args:
            states: k randomly generated states
            maxiterations: The maximum number of iterations

        Returns:
            Final state of the search
        '''

        current = [(state.conflicts(), state) for state in states]
        current.sort(key=lambda x: x[0])

        self.history.append(current[0][0])
        best = current[0][1]

        currentiter = 0
        while currentiter <= maxiterations:

            best.plot(show_conflicts=True)

            newstates = []
            for _, state in current:
                for neighbor in state.neighbors():
                    if neighbor.conflicts() == 0:
                        self.history.append(0)
                        neighbor.plot(show_conflicts=True)
                        return neighbor
                    newstates.append((neighbor.conflicts(), neighbor))

            newstates.sort(key=lambda x: x[0])
            current = newstates[:self.k]

            best = current[0][1]
            self.history.append(current[0][0])

            currentiter += 1

    
    def plot_hist(self):
        ''' Plot the search history
        '''

        plt.figure(figsize=(12, 4))

        plt.plot(range(len(self.history)), self.history)
        plt.xlabel('Iteration')
        plt.ylabel('Conflicts')
        plt.show()
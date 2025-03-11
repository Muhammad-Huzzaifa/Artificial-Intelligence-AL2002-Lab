import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt

class HillClimbingSearch:
    ''' Hill Climbing Search Algorithm
    '''


    def __init__(self):
        ''' Constructor for HillClimbingSearch class
        '''

        self.history = []


    def search(self, state):
        ''' Search for a solution using Hill Climbing Search

        Args:
            state: The initial state of the search

        Returns:
            Final state of the search
        '''

        current = state

        while True:
            current.plot(show_conflicts=True)

            self.history.append(current.conflicts())

            neighbor = current.best_neighbor()
            if neighbor >= current:
                break
            current = neighbor

        return current
    
    
    def plot_hist(self):
        ''' Plot the search history
        '''

        plt.figure(figsize=(12, 4))

        plt.plot(range(len(self.history)), self.history)
        plt.xlabel('Iteration')
        plt.ylabel('Conflicts')
        plt.show()
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import random
import math

class SeamulatedAnealingSearch:
    ''' Simulated Annealing Search Algorithm
    '''


    def __init__(self):
        ''' Constructor for SimulatedAnealingSearch
        '''

        self.history = []
        self.temperature = []

    
    def search(self, state, initial_temperature = 10, cooling_rate = 0.75, threshhold = 1):
        ''' Search for a solution using Simulated Annealing Search Algorithm

        Args:
            state: The initial state of the search
            initial_temperature: The initial temperature of the search
            cooling_rate: The cooling rate of the temperature
            threshhold: The threshhold of the temperature

        Returns:
            Final state of the search
        '''

        current = state
        T = initial_temperature

        while True:
            current.plot(show_conflicts=True)
            
            self.temperature.append(T)
            self.history.append(current.conflicts())

            if T < threshhold or current.conflicts() == 0:
                break

            neighbor = current.random_neighbor()
            delta = current.conflicts() - neighbor.conflicts()

            if delta > 0:
                current = neighbor
            else:
                if math.exp(delta / T) > random.random():
                    current = neighbor 
            
            T *= cooling_rate

        return current


    def plot_hist_temp(self):
        ''' Plot the search history and temperature
        '''

        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.plot(self.temperature, label='Temperature')
        plt.xlabel('Iteration')
        plt.ylabel('Temperature')
        plt.title('Temperature vs. Iteration')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(self.history, label='Connflicts')
        plt.xlabel('Iteration')
        plt.ylabel('Conflicts')
        plt.title('Conflicts vs. Iteration')
        plt.legend()

        plt.tight_layout()
        plt.show()
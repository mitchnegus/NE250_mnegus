from matplotlib import pyplot as plt
import animhm as ahm
import numpy as np

class Ant:

    def __init__(self):
        self.pathhistory = []

    def findpath(self,spaceshape,anthill,food):
        """
        Find a path from the start to the food on the space.
           
        Parameters
        ----------
        spaceshape : tuple
            The dimensions of the space to be explored by the ant.
        start : tuple
            The location of the anthill (starting position).
        food : tuple
            The location of the food source (ending position).
        """
        antpos = anthill[::-1]
        pathspace = np.zeros(spaceshape)
        stuckcounter = 0
        counter = 0
        while antpos != food: 
            key = [(1,0),(0,1),(-1,0),(0,-1)]
            dx,dy = key[np.random.randint(4)]
            antx,anty = antpos[0]+dx,antpos[1]+dy
            if 0 <= antx < spaceshape[1] and 0 <= anty < spaceshape[0]:
                if pathspace[anty,antx] != 1:
                    #print(antpos,'+ ({},{}) = ({},{})'.format(dx,dy,antx,anty))
                    antpos,pathspace = self._record_move(anthill,food,antx,anty,pathspace)
                elif pathspace[anty,antx] == 1:
                    stuckcounter += 1
                if stuckcounter == 101:
                    antpos,pathspace = self._record_move(anthill,food,antx,anty,pathspace)
                    stuckcounter = 0
            counter += 1
        return pathspace

    def _record_move(self,anthill,food,antx,anty,pathspace):
        antpos = (antx,anty) 
        pathspace[antpos[::-1]] = 1
        pathcopy = pathspace.copy()
        pathcopy[anthill],pathcopy[food] = 2,2
        self.pathhistory.append(pathcopy)
        return  antpos,pathspace


class AntColony:

    def __init__(self,spaceshape,anthill,food):
        self.spaceshape = spaceshape 
        self.anthill = anthill
        self.food = food

    def antwave(self,num_ants):
        """
        Simulate a wave of ants finding the food from the anthill.
           
        Parameters
        ----------
        num_ants : int
            The number of ants leaving the anthill in this wave.
        """
        antpaths = np.zeros(spaceshape)
        for ant_n in range(num_ants):
            thisant = Ant()
            thisantpath = thisant.findpath(spaceshape,anthill,food)
            antpaths += thisantpath
            A = ahm.Animation(spaceshape)
            animation = A.animated(thisant.pathhistory)
            plt.show()
        antpaths[anthill] = num_ants*2
        antpaths[food] = num_ants*2
        return antpaths

spaceshape = (25,25)
anthill = (2,3)
food = (24,23)
num_ants = 1

colony = AntColony(spaceshape,anthill,food)
antpaths = colony.antwave(num_ants)

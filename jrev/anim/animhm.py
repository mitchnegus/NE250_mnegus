from matplotlib import pyplot as plt
from matplotlib import animation as ani
import numpy as np
import seaborn as sns

class Animation:

    def __init__(self,mapshape):
        self.mapshape = mapshape
        self.fig,self.ax = plt.subplots(figsize=(9,6))

    def init(self):
        sns.heatmap(np.zeros(self.mapshape))

    def animate(self,i,data):
        plt.clf()
        print('data',data[i])
        sns.heatmap(data[i],xticklabels=False,yticklabels=False)

    def animated(self,data):
        frames=len(data)
        return ani.FuncAnimation(self.fig, self.animate, init_func=self.init, frames=frames, interval=1, repeat = False,fargs=(data,))

